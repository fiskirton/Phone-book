from phonebook.gui.forms import multiline_form


class AddRecordForm(multiline_form.MultilineForm):

    def beforeEditing(self):

        self.name = "New record"
        if not self.editable:
            self.clear_form()
            self.editable = True

    def on_ok(self):

        record = [self.wgName.value, self.wgSurname.value, self.wgPhone.value, self.wgBirthday.value]

        self.func_res_msg = self.parentApp.book.add_edit_record(record)
        self.find_parent_app().getForm('MAIN').records_list.action_type = self.value

        self.after_press_ok(self.func_res_msg)