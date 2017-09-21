import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class Display(Gtk.Entry):
    def __init__(self):
        Gtk.Entry.__init__(self)
        self.connect('key-release-event', self.on_key_release)
        self.set_editable(False)

    def on_key_release(self, widget, event):
        if event.keyval == 32:
            widget.set_text('foi')