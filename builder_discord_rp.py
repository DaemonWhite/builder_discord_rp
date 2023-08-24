import time
import gi 

from gi.repository import GObject
from gi.repository import Ide

from pypresence import Presence 

class MyAppAddin(GObject.Object, Ide.ApplicationAddin):

    def do_load(self, application):
        print("hello")

    def do_unload(self, application):
        print("goodbye")
