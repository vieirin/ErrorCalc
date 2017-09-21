import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class Display(Gtk.Entry):
    def __init__(self):
        Gtk.Entry.__init__(self)
        self.connect('key-release-event', self.on_key_release)
        self.set_editable(False)

    def on_key_release(self, widget, event):
        acceptable_numbers = [x for x in range(48, 58)] + [x for x in range(65456, 65466)]
        commas_keys = [44, 46, 65454]
        if event.keyval in acceptable_numbers:
            if event.keyval in range(65456, 65466):
                event.keyval -= 65408
            curr_txt = widget.get_text()
            curr_txt += chr(event.keyval) 
            widget.set_text(curr_txt)
        elif event.keyval in commas_keys:
            #convert ',' to '.' and allow only one comma
            old_txt = widget.get_text()
            new_txt = old_txt + '.'
            if not old_txt:
                new_txt = ''
            if new_txt.count('.') > 1: 
                new_txt = new_txt[:-1]
            widget.set_text(new_txt)
        elif event.keyval == 65288:
            #backspace case
            curr_txt = widget.get_text()
            curr_txt = curr_txt[:-1]
            widget.set_text(curr_txt)