#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from functools import partial

import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.animation import Animation

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

import gettext
lng = None
_ = None

Config.set('kivy', 'log_dir', os.getcwd()+"\\log")
Config.set('kivy', 'desktop', 1)
Config.set('kivy', 'window_icon', os.getcwd()+'\\data\\icon\\favicon.ico')
Config.set('graphics', 'max_fps', 60)
Config.write()

sm = ScreenManager()

def changeLanguage(lang):
    global lng
    global _
    if lang == 'English':
        lng = gettext.translation('main', localedir='locale', languages=['en'])
    elif lang == 'Русский':
        lng = gettext.translation('main', localedir='locale', languages=['ru'])
    elif lang == 'Беларуская':
        lng = gettext.translation('main', localedir='locale', languages=['be'])
    lng.install()
    _ = lng.gettext

def changeScreen(screen, *args):
    sm.current = screen

def select(button, *args):
    changeLanguage(button.text)
    changeScreen("Subject")
    Subject()

#All screens
langscreen = Screen(name="Lang")
subscreen = Screen(name="Subject")

#First screen
def Lang():
    selected = None
    layout = FloatLayout()
    lng1 = Button(text='English', size_hint=(.5, .1), pos_hint={'x': .25, 'y': .5})
    lng1.bind(on_release=partial(select, lng1))
    lng2 = Button(text='Беларуская', size_hint=(.5, .1), pos_hint={'x': .25, 'y': .4})
    lng2.bind(on_release=partial(select, lng2))
    lng3 = Button(text='Русский', size_hint=(.5, .1), pos_hint={'x': .25, 'y': .3})
    lng3.bind(on_release=partial(select, lng3))
    layout.add_widget(lng1)
    layout.add_widget(lng2)
    layout.add_widget(lng3)
    langscreen.add_widget(layout)

#Second subject
def Subject():
    layout = FloatLayout(size=(300, 300))
    sub1 = Button(text=_('English'), size_hint=(.5, .1), pos_hint={'x': .25, 'y': .9})
    sub2 = Button(text=_('Russian'), size_hint=(.5, .1), pos_hint={'x': .25, 'y': .8})
    sub3 = Button(text=_('Belarussian'), size_hint=(.5, .1), pos_hint={'x': .25, 'y': .7})
    sub4 = Button(text=_('Math'), size_hint=(.5, .1), pos_hint={'x': .25, 'y': .6})
    back = Button(text=_('Back'), size_hint=(.5, .1), pos_hint={'x': .25, 'y': .1})
    back.bind(on_release=partial(changeScreen, "Lang"))
    layout.add_widget(sub1)
    layout.add_widget(sub2)
    layout.add_widget(sub3)
    layout.add_widget(sub4)
    layout.add_widget(back)
    subscreen.add_widget(layout)

from pprint import pprint

Lang()

#Adding screens to Screen manager
sm.add_widget(subscreen)
sm.add_widget(langscreen)

class ImageButton(ButtonBehavior, Image):
    pass

class MaketestApp(App):
    title = 'Making test'

    def build(self):
        sm.current = "Lang"
        return sm

    def on_pause(self):
        return True

if __name__ == '__main__':
    MaketestApp().run()