#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.animation import Animation

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior  

Config.set('kivy', 'log_dir', os.getcwd()+"\\log")
Config.set('kivy', 'desktop', 1)
Config.set('graphics', 'max_fps', 60)
Config.write()

class ImageButton(ButtonBehavior, Image):  
    def on_press(self):  
        print ('pressed')

class Screen(FloatLayout):
    pass

class MaketestApp(App):
    title = 'Making test'

    def build(self):
        return Screen()

    def on_pause(self):
        return True

if __name__ == '__main__':
    MaketestApp().run()