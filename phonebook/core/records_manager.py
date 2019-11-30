import sqlite3
import os
from phonebook.core import entry
from phonebook.extra import messages


class RecordsManager:
    
    def __init__(self, database_name='/book.sqlite'):
        PATH = os.path.dirname(os.path.relpath(__file__)) + '/../data'
        if not os.path.exists(PATH):
            os.makedirs(PATH)
        self.database_name = PATH + database_name
        db = sqlite3.connect(self.database_name)
        cursor = db.cursor()
        cursor.execute("""
                                    CREATE TABLE if not exists records (
                                    Contact_id INTEGER PRIMARY KEY ,
                                    Name,
                                    Surname,
                                    Phone,
                                    Birthday, 
                                    UNIQUE (Name, Surname))""")
        db.commit()
        cursor.close()

    def add_edit_record(self, record, contact_id=""):
        db = sqlite3.connect(self.database_name)
        cursor = db.cursor()
        res = entry.check_all_fields(record)
        if not res[0]:  # if incorrect input
            return res[1]   # return error message

        try:
            if not contact_id:
                cursor.execute("INSERT INTO records(Name, Surname, Phone, Birthday) "
                               "VALUES (?, ?, ?, ?);", res[1])
            else:
                res[1].append(contact_id)

                cursor.execute('UPDATE records SET Name = ?, Surname = ? , Phone = ?, Birthday = ?'
                               ' WHERE Contact_id = ?', res[1])
        except sqlite3.DatabaseError:
            db_message = messages.DB_MSG['existed']
            return db_message
        else:
            db.commit()
            cursor.close()

        return messages.DB_MSG['ok']

    def delete_record(self, **kwargs):
        name = kwargs.get('name')
        surname = kwargs.get('surname')
        phone = kwargs.get('phone')
        contact_id = kwargs.get('contact_id')
        db = sqlite3.connect(self.database_name)
        cursor = db.cursor()

        try:
            if name and surname:
                cursor.execute('DELETE FROM records'
                               ' WHERE Name = ? AND  Surname = ?', (name, surname))
            elif phone:
                cursor.execute('DELETE FROM records'
                               ' WHERE Contact_id = ?', [contact_id])
        except sqlite3.DatabaseError:
            db_message = messages.DB_MSG['fail']
            return db_message
        else:
            db.commit()
            cursor.close()

    def get_all_records(self):
        db = sqlite3.connect(self.database_name)
        cursor = db.cursor()
        cursor.execute('SELECT Name, Surname, Phone, strftime("%d-%m-%Y", Birthday) '
                       'FROM records ORDER BY Name, Surname ')
        records = cursor.fetchall()
        cursor.close()
        return records

    def get_record(self, **kwargs):
        name = kwargs.get('name')
        surname = kwargs.get('surname')
        phone = kwargs.get('phone')
        birthday = kwargs.get('birthday')
        db = sqlite3.connect(self.database_name)
        cursor = db.cursor()
        record = []
        try:
            if name and surname:
                cursor.execute('SELECT Contact_id, Name, Surname, Phone, strftime("%d-%m-%Y",Birthday) FROM records '
                               'WHERE Name = ? AND  Surname = ?', (name, surname))

                record = cursor.fetchall()

            elif phone:
                cursor.execute('SELECT Contact_id, Name, Surname, Phone, Birthday FROM records '
                               'WHERE Phone = ? '
                               'ORDER BY Name, Surname', [phone])
                record = cursor.fetchall()
        except sqlite3.DatabaseError:
            db_message = messages.DB_MSG['fail']
            return db_message
        else:
            cursor.close()
            return record if len(record) else 0

    def get_records_by_fields(self, params):
        db = sqlite3.connect(self.database_name)
        cursor = db.cursor()
        query = self.generate_query(params)

        if messages.DB_MSG.get(query):
            return query, 0
        try:
            cursor.execute(query)
        except sqlite3.DatabaseError:
            db_message = messages.DB_MSG['fail']
            return query, db_message
        else:
            res = cursor.fetchall()
            cursor.close()
            return (messages.DB_MSG['ok'], res) if len(res) else (messages.DB_MSG['nf'], res)

    @staticmethod
    def generate_query(record):
        body = "SELECT Name, Surname, Phone, strftime('%d-%m-%Y', Birthday) FROM records \
                WHERE "
        keys = ['Name', 'Surname', 'Phone', 'Birthday']
        params = dict(zip(keys, record))
        fields = []
        for key in params:
            if params[key] and params[key] not in messages.ERROR_MSG.values():
                if key == 'Birthday':
                    fields.append("{} LIKE '%{}%'".format(key, params[key]))
                else:
                    fields.append("{} = '{}'".format(key, params[key]))

        if not fields:
            message = messages.DB_MSG['empty']
            return message
        else:
            query = body + " AND ".join(fields) + ' ORDER By Name, Surname'
            return query

    def get_near_birthdays(self):
        db = sqlite3.connect(self.database_name)
        cursor = db.cursor()
        try:
            cursor.execute('SELECT '
                           'Name, Surname, Phone, strftime("%d-%m-%Y",Birthday) '
                           'FROM records '
                           'WHERE strftime("%m-%d", Birthday) '
                           'BETWEEN strftime("%m-%d", "now") '
                           'AND strftime("%m-%d", "now", "+30 day") '
                           'ORDER BY Name, Surname')
        except sqlite3.DatabaseError:
            db_message = messages.DB_MSG['fail']
            return db_message
        else:
            records = cursor.fetchall()
            cursor.close()
            return records

    def get_records_n_age(self, entered_n, entered_sign):
        db = sqlite3.connect(self.database_name)
        cursor = db.cursor()

        errors = []
        n, sign = entry.check_int(entered_n), entry.check_sign(entered_sign)
        if n in messages.ERROR_MSG.values():
            errors.append(n)
        if sign in messages.ERROR_MSG.values():
            errors.append(sign)
        if errors:
            message = "\n".join(errors)
            return message, 0

        try:
            cursor.execute('SELECT Name, Surname, Phone, strftime("%d-%m-%Y",Birthday) '
                           'FROM records '
                           'WHERE Birthday != "" '
                           'ORDER BY Name, Surname')
        except sqlite3.DatabaseError:
            db_message = messages.DB_MSG['fail']
            return db_message
        else:
            records_to_check = cursor.fetchall()
            records_to_display = []
            for record in records_to_check:
                age = entry.calc_age(record[-1])
                if entry.less_more_equal(age, n, sign):
                    records_to_display.append(record)

            cursor.close()
            return (messages.DB_MSG['ok'], records_to_display) if len(records_to_display)\
                else (messages.DB_MSG['nf'], records_to_display)

    def delete_all(self):
        db = sqlite3.connect(self.database_name)
        cursor = db.cursor()

        try:
            cursor.execute('DELETE FROM records')
        except sqlite3.DatabaseError:
            db_message = messages.DB_MSG['fail']
            return db_message
        else:
            db.commit()
            cursor.close()
