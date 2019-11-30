import re
from datetime import date
from phonebook.extra import messages


def check_name(value):

    if value is "" or re.search(r'[^a-zA-Z0-9\s]', value) is not None \
            or " " in value.strip() or value[0].isdigit():
        message = messages.ERROR_MSG['name fail']
        return message
    else:
        name = value.lower().capitalize()
        return name


def check_phone(value):

    if len(value) == 12 and value.startswith('+7') or len(value) == 11 and value.startswith('8'):
        phone = value.replace('+7', '8') if value.startswith('+7') else value
        return phone
    else:
        message = messages.ERROR_MSG['phone fail']
        return message


def check_birthday(value, search=False):
    if not value:
        return value

    date_str = [int(i) for i in re.findall(r'[\d]+', value)]
    try:
        if len(date_str) == 2 and search:

            day, month = date_str
            birthday = date(1, month, day).strftime('%m-%d')
        else:
            day, month, year = [int(i) for i in re.findall(r'[\d]+', value)]
            if int(year) < 1800:
                raise ValueError
            birthday = str(date(year, month, day))
        return birthday
    except (TypeError, ValueError):
        message = messages.ERROR_MSG['date fail']
        return message


def check_all_fields(params):
    errors = []
    name_to_record = check_name(params[0])
    surname_to_record = check_name(params[1])
    phone_to_record = check_phone(params[2])
    birthday_to_record = check_birthday(params[3])

    full_record = [name_to_record, surname_to_record, phone_to_record, birthday_to_record]

    for field in full_record:
        if field in messages.ERROR_MSG.values() and field not in errors:
            errors.append(field)

    message = "\n".join(errors)
    return [False, message] if errors else [True, full_record]


def check_int(value):
    return int(value) if value.isdigit() else messages.ERROR_MSG['N']


def check_sign(value):
    return value if len(value) == 1 and value in '<>=' else messages.ERROR_MSG['sign']


def less_more_equal(value, n, sign):
    if sign == '<':
        return value < n
    elif sign == '>':
        return value > n
    else:
        return value == n


def calc_age(value):
    day, month, year = [int(i) for i in re.findall(r'[\d]+', value)]
    birthday = date(year, month, day)
    today = date.today()
    return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
