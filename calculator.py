import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from numbers import NumbersGrid

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='Calculator')

        self.numbers_grid = NumbersGrid()
        self.add(self.numbers_grid)


win = MainWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()

Gtk.main()
