# -*- coding: utf-8 -*-

import os
from functools import partial

import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window

from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

import gettext
subject = None
lng = None
_ = None

Config.set('kivy', 'log_dir', os.getcwd() + "\\log")
Config.set('kivy', 'log_level', 'warning')
Config.set('kivy', 'log_maxfiles', 10)
Config.set('kivy', 'desktop', 1)
Config.set('kivy', 'window_icon', os.getcwd() + '\\data\\icon\\favicon.ico')
Config.set('graphics', 'max_fps', 60)
Config.write()

questions = {}

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
        lng = gettext.translation('main', localedir = 'locale', languages = ['en'])
    elif lang == 'Русский':
        lng = gettext.translation('main', localedir = 'locale', languages = ['ru'])
    elif lang == 'Беларуская':
        lng = gettext.translation('main', localedir = 'locale', languages = ['be'])
    lng.install()
    _ = lng.gettext

def changeScreen(screen, *args):
    sm.current = screen

def select(button):
    changeLanguage(button.text)
    subscreen.clear_widgets()
    Subject()
    changeScreen("Subject")

def subjectChange(button):
    changeSubject(button.text)
    makescreen.clear_widgets()
    Make()
    changeScreen("Making")

#All screens
langscreen = Screen(name = "Lang")
subscreen = Screen(name = "Subject")
makescreen = Screen(name = "Making")
editscreen = Screen(name = "Edit")

#First screen
def Lang():
    Lang.layout = FloatLayout()
    Lang.label = Label(text = "Language/Мова/Язык", size_hint = (.5, .1), pos_hint = {'x': .25, 'y': .6})
    Lang.layout.add_widget(Lang.label)
    Lang.lng1 = Button(text = 'English', size_hint = (.5, .1), pos_hint = {'x': .25, 'y': .5})
    Lang.lng1.bind(on_release = select)
    Lang.lng2 = Button(text = 'Беларуская', size_hint = (.5, .1), pos_hint = {'x': .25, 'y': .4})
    Lang.lng2.bind(on_release = select)
    Lang.lng3 = Button(text = 'Русский', size_hint = (.5, .1), pos_hint = {'x': .25, 'y': .3})
    Lang.lng3.bind(on_release = select)
    Lang.layout.add_widget(Lang.lng1)
    Lang.layout.add_widget(Lang.lng2)
    Lang.layout.add_widget(Lang.lng3)
    langscreen.add_widget(Lang.layout)

#Second subject
def Subject():
    Subject.layout = FloatLayout(size = (300, 300))
    
    #Label
    Subject.label = Label(text = _('Choose subject'), size_hint = (.5, .1), pos_hint = {'x': .25, 'y': .9})
    Subject.layout.add_widget(Subject.label)

    #Subject buttons
    Subject.sub1 = Button(text = _('English'), size_hint = (.5, .1), pos_hint = {'x': .25, 'y': .8})
    Subject.sub2 = Button(text = _('Russian'), size_hint = (.5, .1), pos_hint = {'x': .25, 'y': .7})
    Subject.sub3 = Button(text = _('Belarussian'), size_hint = (.5, .1), pos_hint = {'x': .25, 'y': .6})
    Subject.sub4 = Button(text = _('Math'), size_hint = (.5, .1), pos_hint = {'x': .25, 'y': .5})

    #binding subject buttons
    Subject.sub1.bind(on_release = subjectChange)
    Subject.sub2.bind(on_release = subjectChange)
    Subject.sub3.bind(on_release = subjectChange)
    Subject.sub4.bind(on_release = subjectChange)

    Subject.back = Button(text = _('Back'), size_hint = (.5, .1), pos_hint = {'x': .25, 'y': .1})
    Subject.back.bind(on_release = partial(changeScreen, "Lang"))
    Subject.layout.add_widget(Subject.sub1)
    Subject.layout.add_widget(Subject.sub2)
    Subject.layout.add_widget(Subject.sub3)
    Subject.layout.add_widget(Subject.sub4)
    Subject.layout.add_widget(Subject.back)
    subscreen.add_widget(Subject.layout)

def readyQuest(*args):
    for i in range(len(editQuest.input)):
        questions[editQuest.quest.text][i] = editQuest.input[i].text
    changeScreen("Making")

def editQuest(inst):
    editscreen.clear_widgets()
    view = ScrollView(size_hint = (1, None), size = (Window.width, Window.height), bar_width = 7)
    layout = GridLayout(cols = 1, spacing = 10, size_hint_y = None)
    layout.bind(minimum_height = layout.setter('height'))
    id = int(inst.id)
    back = Button(text = _('Back'), size_hint_y = None, height = 60)
    back.bind(on_release = partial(changeScreen, "Making"))
    layout.add_widget(back)
    editQuest.quest = Label(text = inst.text, size_hint_y = None)
    layout.add_widget(editQuest.quest)
    editQuest.input = []
    if not editQuest.quest.text in questions:
        questions[editQuest.quest.text] = [""] * len(Make.variants[id])
    for i in range(len(Make.variants[id])):
        inp = TextInput(height = 50, size_hint_y = None, text=questions[editQuest.quest.text][i])
        lbl = Label(text = _('Answer number:') + " " + str(i + 1), height = 50, size_hint_y = None)
        editQuest.input.append(inp)
        layout.add_widget(lbl)
        layout.add_widget(inp)
    view.add_widget(layout)
    editscreen.add_widget(view)
    ready = Button(text = _('Ready'), size_hint_y = None, height = 60)
    ready.bind(on_release=readyQuest)
    layout.add_widget(ready)
    changeScreen("Edit")

def addQuestionWithAnswers(txt, num, *args):
    try:
        num = int(num.text)
    except ValueError:
        return
    if len(txt.text) == 0:
        return
    if not hasattr(Make, "variants"):
        Make.variants = []
    btn = Button(text = txt.text, size_hint_y = None, height = 60, id = str(len(Make.variants)))
    btn.bind(on_release = editQuest)
    Make.variants.append([""] * num)
    Make.layout.add_widget(btn)
    Make.layout.remove_widget(Make.ready)
    Make.layout.add_widget(Make.ready)
    addVariants.popup.dismiss()
    addQuest.popup.dismiss()

def addVariants(btn):
    addVariants.layout = GridLayout(cols = 1, rows = 6, spacing = 5)
    addVariants.popup = Popup(title = _('Configuring question'), content = addVariants.layout, size_hint = (None, None), size = (600, 400), auto_dismiss = False)
    addVariants.label = Label(text = _('Write question here:'), size_hint = (1, .2))
    addVariants.text = TextInput()
    addVariants.number = Label(text = _('Number of answers:'), size_hint = (1, .2))
    addVariants.num = TextInput(input_filter = 'int', size_hint = (1, .4), multiline=False)
    addVariants.button = Button(text = _('Close'), size_hint = (1, .5))
    addVariants.button.bind(on_release = addVariants.popup.dismiss)
    addVariants.nxt = Button(text = _('Next'), size_hint = (1, .5))
    addVariants.nxt.bind(on_release = partial(addQuestionWithAnswers, addVariants.text, addVariants.num))
    addVariants.layout.add_widget(addVariants.label)
    addVariants.layout.add_widget(addVariants.text)
    addVariants.layout.add_widget(addVariants.number)
    addVariants.layout.add_widget(addVariants.num)
    addVariants.layout.add_widget(addVariants.nxt)
    addVariants.layout.add_widget(addVariants.button)
    addVariants.popup.open()

def addQuest(btn):
    addQuest.layout = GridLayout(cols = 1, spacing = 5, size_hint_y = None)
    addQuest.popup = Popup(title = _('Choose type'), content = addQuest.layout, size_hint = (None, None), size = (400, 400), auto_dismiss = False)
    addQuest.button = Button(text = _('Close'), size_hint_y = None, height = 40)
    addQuest.button.bind(on_release = addQuest.popup.dismiss)
    addQuest.variants = Button(text = _('Question with answer variants'), size_hint_y = None, height = 40)
    addQuest.variants.bind(on_release = addVariants)
    addQuest.layout.add_widget(addQuest.variants)
    addQuest.layout.add_widget(addQuest.button)
    addQuest.popup.open()

def Make():
    Make.view = ScrollView(size_hint = (1, None), size = (Window.width, Window.height), bar_width = 7)
    Make.layout = GridLayout(cols = 1, spacing = 10, size_hint_y = None)
    Make.layout.bind(minimum_height = Make.layout.setter('height'))
    Make.back = Button(text = _('Back'), size_hint_y = None, height = 60)
    Make.back.bind(on_release = partial(changeScreen, "Subject"))
    Make.layout.add_widget(Make.back)
    Make.new = Button(text = _('More'), size_hint_y = None, height = 60)
    Make.new.bind(on_release = addQuest)
    Make.ready = Button(text = _('Ready'), size_hint_y = None, height = 60)
    Make.layout.add_widget(Make.new)
    Make.layout.add_widget(Make.ready)
    Make.view.add_widget(Make.layout)
    makescreen.add_widget(Make.view)

Lang()

#Adding screens to Screen manager
sm.add_widget(subscreen)
sm.add_widget(langscreen)
sm.add_widget(makescreen)
sm.add_widget(editscreen)

class MaketestApp(App):
    title = 'Making test'

    def build(self):
        sm.current = "Lang"
        return sm

    def on_pause(self):
        return True

if __name__ == '__main__':
    MaketestApp().run()