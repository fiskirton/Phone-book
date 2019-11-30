from phonebook.extra import notifications, messages
from phonebook.gui.forms import multiline_form


class EditRecordForm(multiline_form.MultilineForm):

    def beforeEditing(self):

        self.name = "Edit record"
        name, surname = self.value
        editable_record = self.parentApp.book.get_record(name=name, surname=surname)[0]
        self.record_id = editable_record[0]
        if not self.editable:
            self.fill_form(editable_record)
            self.editable = True

    def on_ok(self):

        record = [self.wgName.value, self.wgSurname.value, self.wgPhone.value, self.wgBirthday.value]

        answer = notifications.spawn_notify_confirmation("EDIT")

        if answer:
            self.func_res_msg = self.parentApp.book.add_edit_record(record, self.record_id)
            self.find_parent_app().getForm('MAIN').records_list.action_type = self.value

        else:
            self.func_res_msg = messages.ACTION_RES_MSG['cancel']

        self.after_press_ok(self.func_res_msg)
