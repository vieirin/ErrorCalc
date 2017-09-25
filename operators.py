import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class OperatorsGrid(Gtk.Grid):
    def __init__(self, display):
        Gtk.Grid.__init__(self)
        self.column_homogeneous=True
        self.display = display
        self.operators_button = []
        self.operators = ['+', '-', '*', '/']
        self.create_operators_grid()
        self.callbacks = [self.sum, self.subtr,
                          self.multiplication, self.division]
        self.op_to_call = {key: value for (key, value) in zip(self.operators, self.callbacks)}
        self.connect_operators()

    def create_operators_grid(self):
        for operator in self.operators:
            self.operators_button.append(Gtk.Button(label='{}'.format(operator)))
        for button in self.operators_button:
            button.set_size_request(50, 25)
        self.attach(self.operators_button[0], 0, 0, 6, 6)
        self.attach(self.operators_button[1], 5, 0, 6, 6)
        self.attach(self.operators_button[2], 0, 6, 5, 5)
        self.attach(self.operators_button[3], 6, 6, 5, 5)
        self.label_to_button = {key: value for (key, value) in zip(self.operators, self.operators_button)}
                
    def connect_operators(self):
        for label, button in self.label_to_button.items():
            button.connect('clicked', self.op_to_call[label])
    
    def sum(self, widget):
        number, error = self.parse_display()
        self.op_and_number = {'+': (number, error)}

    def subtr(self, widget):
        number, error = self.parse_display()
        self.op_and_number = {'-': (number, error)}

    def multiplication(self, widget):
        number, error = self.parse_display()
        self.op_and_number = {'*': (number, error)}

    def division(self, widget):
        number, error = self.parse_display()
        self.op_and_number = {'/': (number, error)}

    def parse_display(self):
        txt_display = self.display.get_text()
        parsed = txt_display.split('±')
        if len(parsed) < 2:
            return parsed, '0'
        return txt_display.split('±')

    def reset_op(self):
        self.op_and_number = {}
        self.display.clear()