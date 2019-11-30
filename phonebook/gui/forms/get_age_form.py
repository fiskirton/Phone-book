import npyscreen
from phonebook.extra import messages
from phonebook.core import entry
from phonebook.gui.forms import deletion_key_form


class GetAgeForm(deletion_key_form.DeletionKeyForm):

    def on_ok(self):

        name = entry.check_name(self.wgName.value)
        surname = entry.check_name(self.wgSurname.value)
        result = self.find_parent_app().book.get_record(name=name, surname=surname)
        if not result:
            self.func_res_msg = messages.ACTION_RES_MSG['nf']
        else:
            if result[0][-1]:
                age = entry.calc_age(result[0][-1])
                npyscreen.notify_confirm(message="{} {} age - {}".format(name, surname, age), title="")
                self.func_res_msg = messages.ACTION_RES_MSG['ok']
            else:
                self.func_res_msg = messages.ERROR_MSG['empty']

        self.after_press_ok(self.func_res_msg)
