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
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

import gettext

Config.set('kivy', 'log_dir', os.getcwd()+"\\log")
Config.set('kivy', 'desktop', 1)
Config.set('kivy', 'window_icon', os.getcwd()+'\\data\\icon\\favicon.ico')
Config.set('graphics', 'max_fps', 60)
Config.write()

class ImageButton(ButtonBehavior, Image):
    pass

class MaketestApp(App):
    title = 'Making test'

    def build(self):
        layout = FloatLayout(size=(300, 300))
        button = Button(text='Language/Мова/Язык', size_hint=(.5, .1), pos_hint={'x': .25, 'y': .5})
        dropdown = DropDown()
        lng1 = Button(text='English', size_hint_y=None, height=48)
        lng1.bind(on_release=lambda lng1: dropdown.select(lng1.text))
        lng2 = Button(text='Беларуская', size_hint_y=None, height=48)
        lng2.bind(on_release=lambda lng2: dropdown.select(lng2.text))
        lng3 = Button(text='Русский', size_hint_y=None, height=48)
        lng3.bind(on_release=lambda lng3: dropdown.select(lng3.text))
        dropdown.add_widget(lng1)
        dropdown.add_widget(lng2)
        dropdown.add_widget(lng3)
        button.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(button, 'text', x))
        layout.add_widget(button)
        return layout

    def on_pause(self):
        return True

if __name__ == '__main__':
    MaketestApp().run()