import time
import gi 

from gi.repository import GObject
from gi.repository import Ide

from threading import Thread
from pypresence import Presence 

class BuilderDiscordPresence(GObject.Object, Ide.ApplicationAddin):

    def rich_update(self):
            while self.__rich_start:
                self.__RPC.update(state="Rich Presence using pypresence!", large_image="org_gnome_builder")
                time.sleep(15)

    def do_load(self, application):
        self.__rich_start = True
        self.__client_id = "1144326276816060567"
        self.__RPC = Presence(self.__client_id)
        self.__RPC.connect()
        r_update = Thread(target=self.rich_update)
        r_update.start()
        print("hello")


    def do_unload(self, application):
        self.__rich_start = False
        print("goodbye")
