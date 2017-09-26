import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from system import CalculatorSystem

class OperatorsGrid(Gtk.Grid):
    def __init__(self, display, calc_system):
        Gtk.Grid.__init__(self)
        self.calc_system = calc_system
        self.column_homogeneous=True
        self.display = display
        self.operators_button = []
        self.operators = ['+', '-', '*', '/']
        self.create_operators_grid()
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
                
    def connect_operators(self):
        for button in self.operators_button:
            button.connect('clicked', self.set_op)
    
    def set_op(self, widget):
        self.calc_system.set_operation(widget.get_label())
