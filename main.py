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
from habit import Habit
from os.path import isfile
from kivymd.theme_picker import MDThemePicker


class Swappy(App):

    def build(self):

        return Builder.load_file('main.kv')


if __name__ == '__main__':
    Swappy().run()