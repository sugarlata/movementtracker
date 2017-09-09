# -*- coding: utf-8 -*-
from kivy.app import App
from random import random
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.colorpicker import Color
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Ellipse, Rectangle
from kivymd.button import MDIconButton
from kivy.properties import StringProperty, NumericProperty, DictProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from math import ceil
from kivymd.label import MDLabel
from math import sin
from random import random
from kivy.core.window import Window
from kivy.clock import mainthread
from kivy.animation import Animation
from kivy.uix.gridlayout import GridLayout
from functools import partial
from kivy.properties import ObjectProperty
from kivy.utils import get_color_from_hex as rgb
import itertools
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.properties import ListProperty
from kivymd.dialog import MDDialog
from kivymd.menu import MDDropdownMenu
from kivymd.date_picker import MDDatePicker
import datetime
import sqlite3 as lite

# TODO Code up login screen
Builder.load_string('''

<LoginScreen>

    MDLabel:
        halign: 'center'
        valign: 'center'
        font_style: 'Display2'
        text: 'Welcome to MovementTracker'

''')


class LoginScreen(Screen):

    app_class = ObjectProperty()
