import npyscreen
from phonebook.core.records_manager import RecordsManager
from phonebook.gui.forms.main_form import MainForm
from phonebook.gui.forms.edit_record_form import EditRecordForm
from phonebook.gui.forms.add_record_form import AddRecordForm
from phonebook.gui.forms.search_record_form import SearchRecordForm
from phonebook.gui.forms.deletion_key_form import DeletionKeyForm
from phonebook.gui.forms.deletion_num_form import DeletionNumForm
from phonebook.gui.forms.get_age_form import GetAgeForm
from phonebook.gui.forms.ages_form import AgeSearchForm


class PhoneBookApp(npyscreen.NPSAppManaged):
    def onStart(self):
        self.book = RecordsManager()
        self.addForm("MAIN", MainForm, name="PhoneBook")
        self.addForm("RECORDADDER", AddRecordForm)
        self.addForm("RECORDEDITOR", EditRecordForm)
        self.addForm("RECORDSEARCHER", SearchRecordForm)
        self.addForm("RECORDDELETERKEY", DeletionKeyForm)
        self.addForm("RECORDDELETERNUM", DeletionNumForm)
        self.addForm("GETAGE", GetAgeForm)
        self.addForm("SEARCHAGE", AgeSearchForm)