# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.clock import mainthread
from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.button import MDIconButton
from kivymd.date_picker import MDDatePicker
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.button import MDFlatButton
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, BaseListItem
from kivymd.material_resources import DEVICE_TYPE
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase, NavigationDrawerToolbar,\
    NavigationDrawerDivider, NavigationDrawerIconButton, NavigationDrawerSubheader
from kivymd.selectioncontrols import MDCheckbox
from kivymd.snackbar import Snackbar
from kivymd.theming import ThemeManager
from kivymd.time_picker import MDTimePicker
from kivymd.menu import MDDropdownMenu, MDMenuItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.list import MDList
from kivy.uix.carousel import Carousel
from kivy.properties import ListProperty
from kivy.uix.colorpicker import Color
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.properties import DictProperty
import sqlite3 as lite
from os.path import isfile
from kivymd.theme_picker import MDThemePicker
from db_connection import MVDatabaseConnect

class MovementTracker(App):

    # This acts as the theme manager for the application
    theme_cls = ThemeManager()

    # This function is run when building the app starts
    def build(self):
        return Builder.load_file('main.kv')

    # Generic Navigation Function
    def navigate_to(self, scn_name, scn_direction):
        self.root.ids.scn_base.transition.direction = scn_direction
        self.root.ids.scn_base.current = scn_name

    # Right Hand top side context menu
    def open_help(**kwargs):
        pass
        # TODO Code in the help screen

    def open_about(**kwargs):
        pass
    # TODO Code in the about screen

    # Menu list, in the form of a list of dictionaries, where dict
    # keys are the object attributes.
    r_menu_items = [
        {'viewclass': 'MDMenuItem',
         'text': 'Help',
         'on_release': open_help},
        {'viewclass': 'MDMenuItem',
         'text': 'Change Theme',
         'on_release': lambda: MDThemePicker().open()},
        {'viewclass': 'MDMenuItem',
         'text': 'About',
         'on_release': open_about},
    ]

    # R Menu - this is the top right context menu
    def r_menu(self, caller):
        MDDropdownMenu(items=self.r_menu_items, width_mult=4).open(caller)



if __name__ == '__main__':
    MovementTracker().run()