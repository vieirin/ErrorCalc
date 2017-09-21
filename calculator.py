import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from numbers import NumbersGrid

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='Calculator')
        self.set_resizable(False)
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.numbers_grid = NumbersGrid()
        self.add(self.box)
        self.box.pack_start(self.numbers_grid, True, True, 0)


win = MainWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()

Gtk.main()
