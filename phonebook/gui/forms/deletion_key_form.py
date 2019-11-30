import npyscreen
from phonebook.extra import notifications, messages
from phonebook.core import entry
from phonebook.gui.forms import multiline_form


class DeletionKeyForm(multiline_form.MultilineForm):
    def create(self):

        self.name = 'Delete(name&surname)'
        self.wgName = self.add(npyscreen.TitleText, name="Name:")
        self.wgSurname = self.add(npyscreen.TitleText, name="Surname:")

    def beforeEditing(self):

        if not self.editable:
            self.clear_form()
            self.editable = True

    def on_ok(self):

        name = entry.check_name(self.wgName.value)
        surname = entry.check_name(self.wgSurname.value)
        result = self.find_parent_app().book.get_record(name=name, surname=surname)
        if not result:
            self.func_res_msg = messages.ACTION_RES_MSG['nf']
        else:
            answer = notifications.spawn_notify_confirmation('DELETE')
            if answer:
                self.find_parent_app().book.delete_record(name=name, surname=surname)
                self.func_res_msg = messages.ACTION_RES_MSG['ok']
            else:
                self.func_res_msg = messages.ACTION_RES_MSG['cancel']

        self.after_press_ok(self.func_res_msg)

    def on_cancel(self):
        self.clear_form()
        self.restore_form()
        self.parentApp.switchFormPrevious()

    def restore_form(self):
        self.editable = False

    def clear_form(self):
        self.wgName.value = ''
        self.wgSurname.value = ''
