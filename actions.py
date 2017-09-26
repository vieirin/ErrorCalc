import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from system import CalculatorSystem

class Actions(Gtk.Box):
    def __init__(self, display, calc_system):
        Gtk.Box.__init__(self)
        self.display = display
        self.calc_system = calc_system
        self.buttons_grid = Gtk.Grid()
        self.buttons_label = ['←', 'CA', 'Enter']
        self.buttons = []
        self.create_buttons()
        self.add(self.buttons_grid)
        self.connect_buttons()

    def create_buttons(self):
        for label in self.buttons_label:
            self.buttons.append(Gtk.Button(label='{}'.format(label)))
        self.buttons_grid.attach(self.buttons[1], 0, 0, 6, 1)
        self.buttons_grid.attach(self.buttons[0], 6, 0, 12, 6)
        self.buttons_grid.attach(self.buttons[2], 2, 1, 1, 1)

        self.buttons[0].set_size_request(55, 40)
        
    def connect_buttons(self):
        self.buttons[0].connect('clicked', self.backspace_clicked)
        self.buttons[1].connect('clicked', self.ca_clicked)
        self.buttons[2].connect('clicked', self.enter_clicked)

    def backspace_clicked(self, widget):
        self.display.set_text(self.display.get_text()[:-1])
    
    def ca_clicked(self, widget):
       self.calc_system.reset()

    def enter_clicked(self, widget):
        self.calc_system.operate()