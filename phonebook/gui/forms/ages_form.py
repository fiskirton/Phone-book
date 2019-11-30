import npyscreen
from phonebook.extra import messages
from phonebook.gui.forms import multiline_form


class AgeSearchForm(multiline_form.MultilineForm):
    def create(self):

        self.name = "Search"
        self.wgN = self.add(npyscreen.TitleText, name="N:")
        self.wgSign = self.add(npyscreen.TitleText, name="Sign:")

    def beforeEditing(self):

        if not self.editable:
            self.clear_form()
            self.editable = True
            self.func_res_msg = []

    def on_ok(self):

        self.func_res_msg, res = self.find_parent_app().book.get_records_n_age(self.wgN.value, self.wgSign.value)
        if self.func_res_msg == messages.ACTION_RES_MSG['ok']:
            self.find_parent_app().getForm('MAIN').records_list.values = res
            self.find_parent_app().getForm('MAIN').records_list.action_type = 'Search'

        self.after_press_ok(self.func_res_msg)

    def on_cancel(self):
        self.clear_form()
        self.restore_form()
        self.parentApp.switchFormPrevious()

    def restore_form(self):
        self.editable = False

    def clear_form(self):
        self.wgN.value = ''
        self.wgSign.value = ''