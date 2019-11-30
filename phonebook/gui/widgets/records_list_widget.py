import npyscreen
import curses
from phonebook.extra import notifications


class RecordsList(npyscreen.GridColTitles):
    def __init__(self, *args, **keywords):
        super(RecordsList, self).__init__(*args, **keywords)
        self.add_handlers({
            curses.KEY_RIGHT: self.h_exit_right,
            "d": self.delete_record_listener,
            "e": self.edit_record_listener,
            "c": self.restore_list_listener,
            "l": self.stub,
        })
        self.values = []
        self.columns = 4
        self.col_titles = ['Name', 'Surname', 'Phone', 'Birthday']
        self.select_whole_line = True

    def delete_record_listener(self, *args, **keywords):
        if self.values:
            selected = self.selected_row()
            answer = notifications.spawn_notify_confirmation("DELETE THE RECORD")
            if answer:
                self.find_parent_app().book.delete_record(name=selected[0], surname=selected[1])
                self.update_list()

    def edit_record_listener(self, *args, **keywords):
        if self.values:
            selected = self.selected_row()
            unique_key = [selected[0], selected[1]]
            self.find_parent_app().getForm('RECORDEDITOR').value = unique_key
            self.find_parent_app().switchForm('RECORDEDITOR')

    def restore_list_listener(self, *args, **keyword):
        self.update_list()

    def stub(self, *args, **keywords):
        pass

    def update_list(self):
        self.values = self.find_parent_app().book.get_all_records()
        self.display()


class RecordsBox(npyscreen.BoxTitle):
    _contained_widget = RecordsList

    def __init__(self, *args, **kwargs):
        super(RecordsBox, self).__init__(*args, **kwargs)
        self.add_handlers({
            curses.KEY_RIGHT: self.h_exit_right,
        })
        self.name = "Records"
        self.action_type = ''

    def update_list(self, *args, **keywords):

        if self.action_type != 'Search':
            self.values = self.find_parent_app().book.get_all_records()
        else:
            self.action_type = ''
        self.display()
