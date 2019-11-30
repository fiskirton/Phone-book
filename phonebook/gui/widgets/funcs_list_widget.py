import npyscreen
import curses
from phonebook.extra import messages, notifications


class FuncMenu(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(FuncMenu, self).__init__(*args, **keywords)
        self.add_handlers({
            curses.KEY_LEFT: self.h_exit_left,

        })
        self.funcs = [
            'Add record',
            'Search',
            'Delete(name&surname)',
            'Delete(number)',
            'Get age',
            'Get near birthdays',
            'Search by age(>, <, = N)',
            'Clear records list'
        ]
        self.values = self.funcs

    def display_value(self, vl):
        return str(vl)

    def actionHighlighted(self, act_on_this, key_press):
        if act_on_this == self.funcs[0]:
            self.find_parent_app().switchForm('RECORDADDER')
        elif act_on_this == self.funcs[1]:
            self.find_parent_app().switchForm('RECORDSEARCHER')
        elif act_on_this == self.funcs[2]:
            self.find_parent_app().switchForm('RECORDDELETERKEY')
        elif act_on_this == self.funcs[3]:
            self.find_parent_app().switchForm('RECORDDELETERNUM')
        elif act_on_this == self.funcs[4]:
            self.find_parent_app().switchForm('GETAGE')
        elif act_on_this == self.funcs[5]:
            self.display_near_birthdays()
        elif act_on_this == self.funcs[6]:
            self.find_parent_app().switchForm('SEARCHAGE')
        elif act_on_this == self.funcs[7]:
            self.clear_records_list()

    def display_near_birthdays(self):
        records = self.find_parent_app().book.get_near_birthdays()
        if records:
            self.find_parent_app().getForm('MAIN').records_list.values = records
            self.find_parent_app().getForm('MAIN').records_list.display()
        else:
            npyscreen.notify_confirm(message=messages.DB_MSG['nf'])

    def clear_records_list(self):
        answer = notifications.spawn_notify_confirmation("DELETE ALL RECORDS")
        if answer:
            self.find_parent_app().book.delete_all()
            self.find_parent_app().getForm('MAIN').records_list.update_list()


class FuncsBox(npyscreen.BoxTitle):

    _contained_widget = FuncMenu

    def __init__(self, *args, **kwargs):
        super(FuncsBox, self).__init__(*args, **kwargs)
        self.name = "Options"

