#!/usr/bin/env python3

import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from numbers import NumbersGrid
from display import Display
from operators import OperatorsGrid
from actions import Actions
from system import CalculatorSystem

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='Calculator')
        self.set_resizable(False)

        #creates box which handles all childs
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.box)
        self.buttons_box = Gtk.Box()
        self.operators_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        
        #objects to be added to main box
        self.numbers_grid = NumbersGrid()
        self.display = Display()
        self.calc_system = CalculatorSystem(self.display)
        self.operators_grid = OperatorsGrid(self.display, self.calc_system)
        self.actions = Actions(self.display, self.calc_system)
        
        #add objects to box
        self.box.add(self.display)
        self.box.add(self.buttons_box)
        self.buttons_box.pack_start(self.numbers_grid, False, True, 0)
        self.buttons_box.pack_start(self.operators_box, False, True, 0)
        self.operators_box.pack_start(self.actions, False, True, 0)
        self.operators_box.add(self.operators_grid)

        #connect numbers buttons to display
        self.numbers_grid.connect_to_display(self.display)
        self.connect('key-release-event', self.on_key_release)

    def on_key_release(self, widget, event):
        self.display.on_key_release(self.display, event)

win = MainWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()

Gtk.main()
