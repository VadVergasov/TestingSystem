# -*- coding: utf-8 -*-

import os, kivy, gettext

# Import library for html generate
from yattag import Doc
from yattag import indent

# Import for working with DB when new test was made
import psycopg2

# This will be used to send parameters when callbacks is called
from functools import partial

kivy.require("1.10.1")

# Basic import
from kivy.app import App

# Import config to set up kivy
from kivy.config import Config

# Import will be need
from kivy.core.window import Window

# UI elemtns import
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox

# Varibles for localization
lng = None
_ = None

# Setting up all configs
Config.set("kivy", "log_dir", os.getcwd() + "\\log")
Config.set("kivy", "log_level", "warning")
Config.set("kivy", "log_maxfiles", 10)
Config.set("kivy", "desktop", 1)
Config.set("kivy", "window_icon", os.getcwd() + "\\data\\icon\\favicon.ico")
Config.set("graphics", "max_fps", 60)
Config.write()

# List of question and subject
questions = {}
answers = {}
subject = None

# Manager
sm = ScreenManager()

# All screens
langscreen = Screen(name="Lang")
subscreen = Screen(name="Subject")
makescreen = Screen(name="Making")
editscreen = Screen(name="Edit")
readyscreen = Screen(name="Ready")


def readyTest(number):
    """Generates final page."""
    begin = "<?php\nrequire('../Templates/head.php');\n$number = basename(__FILE__, '.php');\n$title = '';\n$stmt = getTests('Bel');\nwhile ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {\n    if ($row['ID'] == $number) {\n        $title = $row['Name'];\n        break;\n    }\n}\n?>\n"
    end = "\n<?php\nrequire('../Templates/foot.php');\n?>"
    doc, tag, text, line = Doc().ttl()
    with tag("form", action="check.php", method="post", autocomplete="off"):
        for i in questions:
            with tag("fieldset"):
                doc.line("h2", i)
                with tag("ol"):
                    for j in range(len(questions[i])):
                        with tag("li"):
                            doc.line(
                                "input",
                                questions[i][j],
                                type="checkbox",
                                name=str(j),
                                value=i,
                            )
        doc.stag("input", type="submit", text="send")
        doc.asis(
            "<input type='text' hidden='true' value='<?php echo $number;?>' name='number' />"
        )
    out = open(
        os.getcwd()[0 : os.getcwd().find("program")]
        + str(subject)
        + "/"
        + str(number)
        + ".php",
        "wb",
    )
    out.write((begin + indent(doc.getvalue(), indentation="    ", newline="\r") + end).encode('UTF-8'))
    out.close()


def lastScreen(*args):
    """Trying to get all fields in base"""
    Ready()
    sm.current = "Ready"
    conn = None
    try:
        conn = psycopg2.connect(
            dbname="Tests",
            user="TestingSystem",
            password="postgresql",
            host="localhost",
        )
    except Exception as e:
        Ready.label.text += str(e) + "\n " + _("CheckLabel")
        return
    try:
        cursor = conn.cursor()
        ans = ""
        for i in range(len(editQuest.check)):
            ans += str(int(editQuest.check[i].active))

        cursor.execute(
            "INSERT INTO "
            + str(subject)
            + " (name, description, answer) values ('"
            + str(Make.name.text)
            + "', '"
            + str(Make.description.text)
            + "', '"
            + ans
            + "');"
        )
        cursor.close()
    except Exception as e:
        Ready.label.text += str(e) + "\n " + _("CheckLabel")
        return
    conn.commit()
    number = 0
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM " + str(subject))
        response = cursor.fetchall()
        number = int(response[-1][-1])
        cursor.close()
    except Exception as e:
        Ready.label.text += str(e) + "\n " + _("CheckLabel")
        return
    readyTest(number)
    conn.close()


def Ready():
    Ready.layout = FloatLayout(size=(300, 300))
    Ready.label = Label(text="", size_hint=(0.5, 0.1), pos_hint={"x": 0.25, "y": 0.6})

    Ready.layout.add_widget(Ready.label)
    readyscreen.add_widget(Ready.layout)


def changeSubject(sub):
    """This function changes current subject. It will be used above, when it will generate test"""
    global subject
    if sub == _("Math"):
        subject = "Math"
    elif sub == _("Russian"):
        subject = "Rus"
    elif sub == _("Belarussian"):
        subject = "Bel"
    elif sub == _("English"):
        subject = "Eng"


def changeLanguage(lang):
    """This function defines app language. It is used in gettext function which is defined like _"""
    global lng
    global _
    if lang == "English":
        lng = gettext.translation("main", localedir="locale", languages=["en"])
    elif lang == "Русский":
        lng = gettext.translation("main", localedir="locale", languages=["ru"])
    elif lang == "Беларуская":
        lng = gettext.translation("main", localedir="locale", languages=["be"])
    lng.install()
    _ = lng.gettext


def changeScreen(screen, *args):
    """Changes current screen"""
    sm.current = screen


def select(button):
    """This function changes current screen to subject selection"""
    changeLanguage(button.text)
    subscreen.clear_widgets()
    Subject()
    changeScreen("Subject")


def subjectChange(button):
    """This function changes current screen to making test"""
    changeSubject(button.text)
    makescreen.clear_widgets()
    Make()
    changeScreen("Making")


def Lang():
    """First screen. Language select"""
    Lang.layout = FloatLayout()
    Lang.label = Label(
        text="Language/Мова/Язык", size_hint=(0.5, 0.1), pos_hint={"x": 0.25, "y": 0.6}
    )
    Lang.layout.add_widget(Lang.label)
    Lang.lng1 = Button(
        text="English", size_hint=(0.5, 0.1), pos_hint={"x": 0.25, "y": 0.5}
    )
    Lang.lng1.bind(on_release=select)
    Lang.lng2 = Button(
        text="Беларуская", size_hint=(0.5, 0.1), pos_hint={"x": 0.25, "y": 0.4}
    )
    Lang.lng2.bind(on_release=select)
    Lang.lng3 = Button(
        text="Русский", size_hint=(0.5, 0.1), pos_hint={"x": 0.25, "y": 0.3}
    )
    Lang.lng3.bind(on_release=select)

    # Adding all widgets to layout
    Lang.layout.add_widget(Lang.lng1)
    Lang.layout.add_widget(Lang.lng2)
    Lang.layout.add_widget(Lang.lng3)
    langscreen.add_widget(Lang.layout)


def Subject():
    """Second screen. Subject selection"""
    Subject.layout = FloatLayout(size=(300, 300))

    # Label
    Subject.label = Label(
        text=_("Choose subject"), size_hint=(0.5, 0.1), pos_hint={"x": 0.25, "y": 0.9}
    )
    Subject.layout.add_widget(Subject.label)

    # Subject buttons
    Subject.sub1 = Button(
        text=_("English"), size_hint=(0.5, 0.1), pos_hint={"x": 0.25, "y": 0.8}
    )
    Subject.sub2 = Button(
        text=_("Russian"), size_hint=(0.5, 0.1), pos_hint={"x": 0.25, "y": 0.7}
    )
    Subject.sub3 = Button(
        text=_("Belarussian"), size_hint=(0.5, 0.1), pos_hint={"x": 0.25, "y": 0.6}
    )
    Subject.sub4 = Button(
        text=_("Math"), size_hint=(0.5, 0.1), pos_hint={"x": 0.25, "y": 0.5}
    )

    # binding subject buttons
    Subject.sub1.bind(on_release=subjectChange)
    Subject.sub2.bind(on_release=subjectChange)
    Subject.sub3.bind(on_release=subjectChange)
    Subject.sub4.bind(on_release=subjectChange)

    Subject.back = Button(
        text=_("Back"), size_hint=(0.5, 0.1), pos_hint={"x": 0.25, "y": 0.1}
    )
    Subject.back.bind(on_release=partial(changeScreen, "Lang"))

    # Adding all widgets to layout
    Subject.layout.add_widget(Subject.sub1)
    Subject.layout.add_widget(Subject.sub2)
    Subject.layout.add_widget(Subject.sub3)
    Subject.layout.add_widget(Subject.sub4)
    Subject.layout.add_widget(Subject.back)

    # Adding screen to ScreenManager
    subscreen.add_widget(Subject.layout)


def readyQuest(*args):
    """Confirming Question add"""
    for i in range(len(editQuest.input)):
        questions[editQuest.quest.text][i] = editQuest.input[i].text
    for i in range(len(editQuest.check)):
        answers[editQuest.quest.text][i] = editQuest.check[i].active
    changeScreen("Making")


def editQuest(inst):
    """Open view of Question editor"""
    editscreen.clear_widgets()
    view = ScrollView(
        size_hint=(1, None), size=(Window.width, Window.height), bar_width=7
    )
    layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
    layout.bind(minimum_height=layout.setter("height"))
    id = int(inst.id)
    back = Button(text=_("Back"), size_hint_y=None, height=60)
    back.bind(on_release=partial(changeScreen, "Making"))
    layout.add_widget(back)
    editQuest.quest = Label(text=inst.text, size_hint_y=None)
    layout.add_widget(editQuest.quest)

    # All our arrays for generating html file
    editQuest.input = []
    editQuest.check = []
    editQuest.subgrid = []
    if not editQuest.quest.text in questions:
        questions[editQuest.quest.text] = [""] * len(Make.variants[id])
    if not editQuest.quest.text in answers:
        answers[editQuest.quest.text] = [False] * len(Make.variants[id])
    for i in range(len(Make.variants[id])):
        subgrid = GridLayout(cols=2, spacing=0, size_hint_y=None, height=50)
        inp = TextInput(
            height=50, size_hint_y=None, text=questions[editQuest.quest.text][i]
        )
        check = CheckBox(size_hint_x=None, width=50)
        lbl = Label(text=_("Answer number:") + " " + str(i + 1), height=50)
        editQuest.subgrid.append(subgrid)
        editQuest.input.append(inp)
        editQuest.check.append(check)
        subgrid.add_widget(check)
        subgrid.add_widget(lbl)
        layout.add_widget(subgrid)
        layout.add_widget(inp)
    view.add_widget(layout)
    editscreen.add_widget(view)
    ready = Button(text=_("Ready"), size_hint_y=None, height=60)
    ready.bind(on_release=readyQuest)
    layout.add_widget(ready)
    changeScreen("Edit")


def addQuestionWithAnswers(txt, num, *args):
    """Our popup for configuring question"""
    try:
        num = int(num.text)
    except ValueError:
        return
    if len(txt.text) == 0:
        return
    if not hasattr(Make, "variants"):
        Make.variants = []
    btn = Button(text=txt.text, size_hint_y=None, height=60, id=str(len(Make.variants)))
    btn.bind(on_release=editQuest)
    Make.variants.append([""] * num)
    Make.layout.add_widget(btn)
    Make.layout.remove_widget(Make.ready)
    Make.layout.add_widget(Make.ready)
    addVariants.popup.dismiss()
    addQuest.popup.dismiss()


def addVariants(btn):
    addVariants.layout = GridLayout(cols=1, rows=6, spacing=5)
    addVariants.popup = Popup(
        title=_("Configuring question"),
        content=addVariants.layout,
        size_hint=(None, None),
        size=(600, 400),
        auto_dismiss=False,
    )
    addVariants.label = Label(text=_("Write question here:"), size_hint=(1, 0.2))
    addVariants.text = TextInput()
    addVariants.number = Label(text=_("Number of answers:"), size_hint=(1, 0.2))
    addVariants.num = TextInput(input_filter="int", size_hint=(1, 0.4), multiline=False)
    addVariants.button = Button(text=_("Close"), size_hint=(1, 0.5))
    addVariants.button.bind(on_release=addVariants.popup.dismiss)
    addVariants.nxt = Button(text=_("Next"), size_hint=(1, 0.5))
    addVariants.nxt.bind(
        on_release=partial(addQuestionWithAnswers, addVariants.text, addVariants.num)
    )
    addVariants.layout.add_widget(addVariants.label)
    addVariants.layout.add_widget(addVariants.text)
    addVariants.layout.add_widget(addVariants.number)
    addVariants.layout.add_widget(addVariants.num)
    addVariants.layout.add_widget(addVariants.nxt)
    addVariants.layout.add_widget(addVariants.button)
    addVariants.popup.open()


def addQuest(btn):
    addQuest.layout = GridLayout(cols=1, spacing=5, size_hint_y=None)
    addQuest.popup = Popup(
        title=_("Choose type"),
        content=addQuest.layout,
        size_hint=(None, None),
        size=(400, 400),
        auto_dismiss=False,
    )
    addQuest.button = Button(text=_("Close"), size_hint_y=None, height=40)
    addQuest.button.bind(on_release=addQuest.popup.dismiss)
    addQuest.variants = Button(
        text=_("Question with answer variants"), size_hint_y=None, height=40
    )
    addQuest.variants.bind(on_release=addVariants)
    addQuest.layout.add_widget(addQuest.variants)
    addQuest.layout.add_widget(addQuest.button)
    addQuest.popup.open()


def Make():
    """Screen for configuring test"""
    Make.view = ScrollView(
        size_hint=(1, None), size=(Window.width, Window.height), bar_width=7
    )
    Make.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
    Make.layout.bind(minimum_height=Make.layout.setter("height"))

    Make.back = Button(text=_("Back"), size_hint_y=None, height=60)
    Make.back.bind(on_release=partial(changeScreen, "Subject"))

    Make.name_text = Label(text=_("Name of test"), size_hint_y=None, height=40)

    Make.name = TextInput(size_hint_y=None, height=40)

    Make.description_text = Label(
        text=_("Test description"), size_hint_y=None, height=40
    )

    Make.description = TextInput(size_hint_y=None, height=60)

    Make.new = Button(text=_("More"), size_hint_y=None, height=60)
    Make.new.bind(on_release=addQuest)

    Make.ready = Button(text=_("Ready"), size_hint_y=None, height=60)
    Make.ready.bind(on_release=lastScreen)

    Make.layout.add_widget(Make.back)
    Make.layout.add_widget(Make.name_text)
    Make.layout.add_widget(Make.name)
    Make.layout.add_widget(Make.description_text)
    Make.layout.add_widget(Make.description)
    Make.layout.add_widget(Make.new)
    Make.layout.add_widget(Make.ready)

    Make.view.add_widget(Make.layout)
    makescreen.add_widget(Make.view)


# Function call
Lang()

# Adding screens to Screen manager
sm.add_widget(subscreen)
sm.add_widget(langscreen)
sm.add_widget(makescreen)
sm.add_widget(editscreen)
sm.add_widget(readyscreen)


class MaketestApp(App):
    """Main class"""

    title = "Making test"

    def build(self):
        sm.current = "Lang"
        return sm

    def on_pause(self):
        return True


if __name__ == "__main__":
    MaketestApp().run()
