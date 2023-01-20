'''
Created on 24-10-2012

@author: Krzysiek
'''
import gtk
 
class HelloWorld(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)
        self.connect("delete_event", gtk.main_quit)
        self.set_border_width(10)
        self.set_title("Hello World!")
        button = gtk.Button("Press me")
        button.connect("clicked", self.button_pressed_cb)
        self.add(button)
 
    def button_pressed_cb(self, button):
        print "Hello again - the button was pressed"
 
if __name__ == "__main__":
    win = HelloWorld()
    win.show_all()
    gtk.main()