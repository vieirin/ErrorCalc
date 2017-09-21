import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from numbers import NumbersGrid
from display import Display


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='Calculator')
        self.set_resizable(False)
        
        #creates box which handles all childs
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)
        
        #objects to be added to main box
        self.numbers_grid = NumbersGrid()
        self.display = Display()
        
        #add objects to box
        self.box.pack_start(self.display, True, True, 0)
        self.box.pack_start(self.numbers_grid, True, True, 0)

        #connect numbers buttons to display
        self.numbers_grid.connect_to_display(self.display)

win = MainWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()

Gtk.main()
