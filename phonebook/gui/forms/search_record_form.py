from phonebook.core import entry
from phonebook.gui.forms import multiline_form
from phonebook.extra import messages


class SearchRecordForm(multiline_form.MultilineForm):

    def beforeEditing(self):

        self.name = "Search"
        if not self.editable:
            self.clear_form()
            self.editable = True

    def on_ok(self):

        name = entry.check_name(self.wgName.value)
        surname = entry.check_name(self.wgSurname.value)
        phone = entry.check_phone(self.wgPhone.value)
        birthday = entry.check_birthday(self.wgBirthday.value, search=True)
        record = [name, surname, phone, birthday]
        self.func_res_msg, res = self.parentApp.book.get_records_by_fields(record)
        if self.func_res_msg == messages.ACTION_RES_MSG['ok']:
            self.find_parent_app().getForm('MAIN').records_list.values = res
            self.find_parent_app().getForm('MAIN').records_list.action_type = 'Search'

        self.after_press_ok(self.func_res_msg)
