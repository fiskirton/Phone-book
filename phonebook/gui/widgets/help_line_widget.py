import npyscreen


class HelpLine(npyscreen.FixedText):
    def __init__(self, *args, **keywords):
        super(HelpLine, self).__init__(*args, **keywords)
        self.value = ", ".join(['TAB, Arrows - navigation',
                                'Q - exit',
                                'd - delete selected record',
                                'e - edit selected record',
                                'C - restore records list'
                                ])
        self.name = 'Help:'

    def display_value(self, value):
        return value


class HelpLineBox(npyscreen.BoxTitle):
    _contained_widget = HelpLine

    def __init__(self, *args, **kwargs):
        super(HelpLineBox, self).__init__(*args, **kwargs)
        self.name = "Help"
