import npyscreen
from phonebook.extra import notifications, messages


class MultilineForm(npyscreen.ActionPopup):
    def __init__(self, *args, **keywords):
        super(MultilineForm, self).__init__(*args, **keywords)

        y, x = self.useable_space()

        self.show_atx = x
        self.show_aty = y
        self.value = None  # the value passed to the form when the listener is triggered
        self.editable = False
        self.func_res_msg = messages.ACTION_RES_MSG['fail']
        self.record_id = None

    def create(self):

        self.wgName = self.add(npyscreen.TitleText, name="Name:")
        self.wgSurname = self.add(npyscreen.TitleText, name="Surname:")
        self.wgPhone = self.add(npyscreen.TitleText, name="Phone:")
        self.wgBirthday = self.add(npyscreen.TitleText, name="Birthday:")

    def after_press_ok(self, res_msg):

        if self.func_res_msg == messages.ACTION_RES_MSG['ok']:
            self.restore_form()
            self.parentApp.switchFormPrevious()
        elif res_msg == messages.ACTION_RES_MSG['cancel']:
            self.find_parent_app().getForm('MAIN').records_list.display()
        else:
            notifications.spawn_warning_incorrect_input(res_msg)
            self.find_parent_app().getForm('MAIN').records_list.display()

    def on_cancel(self):
        self.clear_form()
        self.restore_form()
        self.parentApp.switchFormPrevious()

    def restore_form(self):
        self.editable = False
        self.value = None
        self.record_id = None
        self.clear_form()

    def clear_form(self):
        self.wgName.value = ""
        self.wgSurname.value = ""
        self.wgPhone.value = ""
        self.wgBirthday.value = ""

    def fill_form(self, record_fields):
        self.wgName.value = record_fields[1]
        self.wgSurname.value = record_fields[2]
        self.wgPhone.value = record_fields[3]
        self.wgBirthday.value = record_fields[4]
