import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk


class NumbersGrid(Gtk.Grid):
    def __init__(self):
        Gtk.Grid.__init__(self)
        self.column_homogeneous=True
        self.numbers = []
        self.create_numbers_grid()
        self.create_lastline()

    def create_numbers_grid(self):
        for i in range(3):
            for j in range(3):
                self.numbers.append(Gtk.Button(label='{}'.format(3*i+j+1)))
                self.attach(self.numbers[3*i+j], j, i, 1, 1)

    def create_lastline(self):
        zero_button = Gtk.Button(label='0')
        comma_button = Gtk.Button(label='.')
        plus_minus_button = Gtk.Button(label='±')
        
        self.numbers.append(zero_button)
        self.numbers.append(comma_button)
        self.numbers.append(plus_minus_button)

        self.attach(zero_button, 0, 3, 1, 1)
        self.attach(comma_button, 1, 3, 1, 1)
        self.attach(plus_minus_button, 2, 3, 1, 1)

    def connect_to_display(self, display):
        #connect all grid buttons to main display
        self.display = display
        for button in self.numbers:
            button.connect('clicked', self.on_number_clicked, self.display)

    def on_number_clicked(self, widget, display):
        curr_text = display.get_text()
        curr_text+=widget.get_label()
        display.set_text(curr_text)