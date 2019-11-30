import npyscreen
import sys
from phonebook.gui.widgets.funcs_list_widget import FuncsBox
from phonebook.gui.widgets.records_list_widget import RecordsBox
from phonebook.gui.widgets.help_line_widget import HelpLineBox


class MainForm(npyscreen.FormBaseNew):
    def __init__(self, *args, **keywords):
        super(MainForm, self).__init__(*args, **keywords)
        self.add_handlers({
            'Q': self.close_app,
            'C': self.records_list.update_list

        })

    def create(self):
        y, x = self.useable_space()
        self.records_list = self.add(RecordsBox, rely=1, max_width=int(x * 0.80), max_height=int(y * 0.89))
        self.add(FuncsBox, rely=1, relx=int(x*0.80)+2, max_height=int(y * 0.89))
        self.add(HelpLineBox, rely=y - 5, max_height=3)

    def beforeEditing(self):
        npyscreen.notify_confirm(message=self.find_parent_app().book.database_name)
        self.records_list.update_list()

    def close_app(self, *args, **keywords):
        answer = npyscreen.notify_yes_no(message="Confirm exit", title='Exit')
        if answer:
            sys.exit(0)
