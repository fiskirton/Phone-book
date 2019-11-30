import npyscreen
from phonebook.extra import notifications, messages
from phonebook.core import entry
from phonebook.gui.forms import multiline_form


class DeletionNumForm(multiline_form.MultilineForm):
    def create(self):

        self.name = 'Delete(number)'
        self.wgPhone = self.add(npyscreen.TitleText, name="Phone:")

    def beforeEditing(self):

        if not self.editable:
            self.clear_form()
            self.editable = True

    def on_ok(self):

        phone = entry.check_phone(self.wgPhone.value)
        result = self.find_parent_app().book.get_record(phone=phone)
        if not result:
            self.func_res_msg = messages.ACTION_RES_MSG['nf']

        elif len(result) == 1:
            answer = notifications.spawn_notify_confirmation('DELETE THE RECORD')
            if answer:
                self.find_parent_app().book.delete_record(phone=phone, contact_id=result[0][0])
                self.func_res_msg = messages.ACTION_RES_MSG['ok']
            else:
                self.func_res_msg = messages.ACTION_RES_MSG['cancel']

        else:
            self.find_parent_app().getForm('RECORDEDITOR').value = 'Search'
            self.find_parent_app().getForm('RECORDEDITOR').clear_form()
            self.find_parent_app().getForm('RECORDEDITOR').wgPhone.value = self.wgPhone.value
            self.find_parent_app().getForm('RECORDEDITOR').on_ok()
            self.func_res_msg = messages.ACTION_RES_MSG['ok']

        self.after_press_ok(self.func_res_msg)

    def on_cancel(self):
        self.clear_form()
        self.restore_form()
        self.parentApp.switchFormPrevious()

    def restore_form(self):
        self.editable = False

    def clear_form(self):
        self.wgPhone.value = ''
