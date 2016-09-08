#! /usr/bin/python
"""
#import os
#### Checks environment of desktop session ####
#env = os.environ.get('XDG_CURRENT_DESKTOP')
#print env ### Prints "Unity" ###
"""
from gi.repository import Gtk, Gio
import datetime

class wallpaperAutomator():

    SCHEMA = 'org.gnome.desktop.background'
    KEY = 'picture-uri'

    def __init__(self):
        """Initialize time interval variables in here"""

    def on_time_interval(self, time):
        gsettings = Gio.Settings.new(self.SCHEMA)


