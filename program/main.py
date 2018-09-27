#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from functools import partial

import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.config import Config
from kivy.animation import Animation
from kivy.core.window import Window

from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label

import gettext
subject = None
lng = None
_ = None

Config.set('kivy', 'log_dir', os.getcwd()+"\log")
Config.set('kivy', 'desktop', 1)
Config.set('kivy', 'window_icon', os.getcwd()+'\\data\\icon\\favicon.ico')
Config.set('graphics', 'max_fps', 60)
Config.write()

sm = ScreenManager()

def changeSubject(sub):
    global subject
    if sub == _('Math'):
        subject = 'Math'
    elif sub == _('Russian'):
        subject = 'Rus'
    elif sub == _('Belarussian'):
        subject = 'Bel'
    elif sub == _('English'):
        subject = 'Eng'

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

def select(button):
    changeLanguage(button.text)
    changeScreen("Subject")
    Subject()

def subjectChange(button):
    changeSubject(button.text)
    changeScreen("Making")
    Make()

#All screens
langscreen = Screen(name="Lang")
subscreen = Screen(name="Subject")
makescreen = Screen(name="Making")

#First screen
def Lang():
    selected = None
    layout = FloatLayout()
    label = Label(text="Language/Мова/Язык", size_hint=(.5, .1), pos_hint={'x': .25, 'y': .6})
    layout.add_widget(label)
    lng1 = Button(text='English', size_hint=(.5, .1), pos_hint={'x': .25, 'y': .5})
    lng1.bind(on_release=select)
    lng2 = Button(text='Беларуская', size_hint=(.5, .1), pos_hint={'x': .25, 'y': .4})
    lng2.bind(on_release=select)
    lng3 = Button(text='Русский', size_hint=(.5, .1), pos_hint={'x': .25, 'y': .3})
    lng3.bind(on_release=select)
    layout.add_widget(lng1)
    layout.add_widget(lng2)
    layout.add_widget(lng3)
    langscreen.add_widget(layout)

#Second subject
def Subject():
    layout = FloatLayout(size=(300, 300))
    
    label = Label(text=_("Choose subject"), size_hint=(.5, .1), pos_hint={'x': .25, 'y': .9})
    layout.add_widget(label)

    #Subject buttons
    sub1 = Button(text=_('English'), size_hint=(.5, .1), pos_hint={'x': .25, 'y': .8})
    sub2 = Button(text=_('Russian'), size_hint=(.5, .1), pos_hint={'x': .25, 'y': .7})
    sub3 = Button(text=_('Belarussian'), size_hint=(.5, .1), pos_hint={'x': .25, 'y': .6})
    sub4 = Button(text=_('Math'), size_hint=(.5, .1), pos_hint={'x': .25, 'y': .5})

    #binding subject buttons
    sub1.bind(on_release=subjectChange)
    sub2.bind(on_release=subjectChange)
    sub3.bind(on_release=subjectChange)
    sub4.bind(on_release=subjectChange)

    back = Button(text=_('Back'), size_hint=(.5, .1), pos_hint={'x': .25, 'y': .1})
    back.bind(on_release=partial(changeScreen, "Lang"))
    layout.add_widget(sub1)
    layout.add_widget(sub2)
    layout.add_widget(sub3)
    layout.add_widget(sub4)
    layout.add_widget(back)
    subscreen.add_widget(layout)

def addQuest(btn):
    layout = GridLayout(cols=1, spacing=5, size_hint_y=None)
    popup = Popup(title=_('Choose type'), content=layout, size_hint=(None, None), size=(400, 400), auto_dismiss=False)
    button = Button(text=_('Close'), size_hint_y=None, height=40)
    button.bind(on_release=popup.dismiss)
    variants = Button(text=_('Question with answer variants'), size_hint_y=None, height=40)
    layout.add_widget(variants)
    layout.add_widget(button)
    popup.open()

def Make():
    view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
    layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
    layout.bind(minimum_height=layout.setter('height'))
    new = Button(text=_('More'), size_hint_y=None, height=40)
    new.bind(on_release=addQuest)
    layout.add_widget(new)
    view.add_widget(layout)
    makescreen.add_widget(view)

Lang()

#Adding screens to Screen manager
sm.add_widget(subscreen)
sm.add_widget(langscreen)
sm.add_widget(makescreen)

class MaketestApp(App):
    title = 'Making test'

    def build(self):
        sm.current = "Lang"
        return sm

    def on_pause(self):
        return True

if __name__ == '__main__':
    MaketestApp().run()