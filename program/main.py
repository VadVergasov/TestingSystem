# -*- coding: utf-8 -*-

# Base imports
import os
import kivy
import gettext
import json
from os import listdir
from os.path import isfile, join

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
Config.set("kivy", "window_icon", "icon.png")
Config.set("graphics", "max_fps", 60)
Config.write()

# List of question and subject
questions = {}
answers = {}
subject = None
php_file = ""
ans = ""

# Manager
sm = ScreenManager()

# All screens
langscreen = Screen(name="Lang")
subscreen = Screen(name="Subject")
makescreen = Screen(name="Making")
editscreen = Screen(name="Edit")
readyscreen = Screen(name="Ready")


def generateFile():
    """Generates final php page."""
    begin = (
        "<?php\ndefine('PROJECT_DIR', realpath('../'));\ndefine('LOCALE_DIR', PROJECT_DIR . '\Locale');\ndefine('DEFAULT_LOCALE', 'en');\n\nrequire('../GetText/gettext.inc');\n\n$encoding = 'UTF-8';\n\n$locale = (isset($_GET['lang'])) ? $_GET['lang'] : DEFAULT_LOCALE;\n\nT_setlocale(LC_MESSAGES, $locale);\n\nT_bindtextdomain($locale, LOCALE_DIR);\nT_bind_textdomain_codeset($locale, $encoding);\nT_textdomain($locale);\n\nrequire('../postgresql.php');\n$number = basename(__FILE__, '.php');\n$title = '';\n$stmt = getTests('"
        + str(subject)
        + "');\nwhile ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {\n    if ($row['id'] == $number) {\n        $title = $row['name'];\n        break;\n    }\n}\nrequire('../Templates/head.php');\n?>\n"
    )
    end = "\n<?php\nrequire('../Templates/foot.php');\n?>"

    # pylint: disable=unused-variable
    doc, tag, text, line = Doc().ttl()
    with tag("form", action="../Pages/checker", method="post", autocomplete="off"):
        doc.line("input", "", type="hidden", name="Lang", value=str(subject))
        doc.line("input", "", type="hidden", name="Name", value=str(Make.name.text))
        num = 0
        for i in questions:
            with tag("fieldset"):
                doc.line(
                    "input",
                    "",
                    type="hidden",
                    name="Count[]",
                    value=str(len(questions[i])),
                )
                doc.line("h2", i)
                with tag("ol"):
                    for j in range(len(questions[i])):
                        with tag("li"):
                            doc.line(
                                "input",
                                questions[i][j],
                                type="checkbox",
                                name=str(num) + "[]",
                                value=str(j),
                            )
            num += 1
        doc.stag("input", type="submit", text="send")
    global php_file
    php_file = begin + indent(doc.getvalue(), indentation="    ", newline="\r") + end


def readyTest(number, imp=False):
    if not imp:
        generateFile()
    out = open(
        os.getcwd()[0 : os.getcwd().find("program")]
        + str(subject)
        + "/"
        + str(number)
        + ".php",
        "wb",
    )
    global php_file
    out.write(php_file.encode("UTF-8"))
    out.close()


def export(*args):
    """Trying to get all fields in base"""
    Ready()
    changeScreen("Ready")
    if Make.name.text == "":
        Ready.label.text = _("Test name can't be blank!")
        Ready.layout.add_widget(Ready.back)
        return
    elif len(questions) == 0:
        Ready.label.text = _("You didn't configure questions!")
        Ready.layout.add_widget(Ready.back)
        return
    generateFile()
    to_export = {}
    to_export["Test_name"] = Make.name.text
    to_export["Test_description"] = Make.description.text
    to_export["subject"] = subject

    global ans
    for i in answers.values():
        for j in i:
            ans += str(int(j))

    to_export["answer"] = ans
    to_export["file"] = php_file
    out = open("tests/" + Make.name.text + ".json", "w")
    out.write(json.dumps(to_export))
    out.close()
    Ready.label.text = "OK!"


def imp(*args):
    all_tests = [f for f in listdir("tests") if isfile(join("tests", f))]
    for i in all_tests:
        input_file = open("tests/" + i, "r")
        to_import = json.loads(input_file.read())
        global subject
        subject = to_import["subject"]
        Make.name.text = to_import["Test_name"]
        Make.description.text = to_import["Test_description"]
        global ans
        ans = to_import["answer"]
        global php_file
        php_file = to_import["file"]
        lastScreen(True)


def lastScreen(imp=False, *args):
    """Trying to get all fields in base"""
    Ready()
    changeScreen("Ready")
    if Make.name.text == "":
        Ready.label.text = _("Test name can't be blank!")
        Ready.layout.add_widget(Ready.back)
        return
    elif len(questions) == 0 and not imp:
        Ready.label.text = _("You didn't configure questions!")
        Ready.layout.add_widget(Ready.back)
        return
    conn = None
    try:
        conn = psycopg2.connect(
            dbname="Tests",
            user="TestingSystem",
            password="postgresql",
            host="localhost",
        )
    except Exception as e:
        if "could not connect to server" in str(e):
            Ready.label.text += _(
                "Check if server is running. Try again or ask for help."
            )
        else:
            Ready.label.text += str(e)
        Ready.layout.add_widget(Ready.back)
        return
    try:
        cursor = conn.cursor()

        global ans
        if not imp:
            for i in answers.values():
                for j in i:
                    ans += str(int(j))

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
        if "duplicate key value violates unique" in str(e):
            Ready.label.text += _("Test with this name already exists, change the name of the test")
        else:
            Ready.label.text += (
                str(e) + "\n " + _("Check if server is running. Try again or ask for help.")
            )
        Ready.layout.add_widget(Ready.back)
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
        Ready.label.text += (
            str(e) + "\n " + _("Check if server is running. Try again or ask for help.")
        )
        Ready.layout.add_widget(Ready.back)
        return
    readyTest(number, imp)
    conn.close()
    Ready.label.text = "OK!"


def Ready():
    # Clear screen to prevent text-on-text situation
    readyscreen.clear_widgets()

    Ready.layout = FloatLayout(size=(300, 300))
    Ready.label = Label(text="", size_hint=(0.5, 0.1), pos_hint={"x": 0.25, "y": 0.6})
    Ready.back = Button(
        text=_("Back"), size_hint=(0.5, 0.1), pos_hint={"x": 0.25, "y": 0.8}
    )
    Ready.back.bind(on_release=partial(changeScreen, "Making"))

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
    elif sub == _("Geography"):
        subject = "Geo"
    elif sub == _("Informatics"):
        subject = "Inf"
    elif sub == _("Physics"):
        subject = "Phy"
    elif sub == _("Biology"):
        subject = "Bio"


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
    Subject.view = ScrollView(
        size_hint=(1, None), size=(Window.width, Window.height), bar_width=7
    )

    Subject.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
    Subject.layout.bind(minimum_height=Subject.layout.setter("height"))

    # Label
    Subject.label = Label(text=_("Choose subject"), size_hint_y=None, height=60)
    Subject.layout.add_widget(Subject.label)

    # Subject buttons
    Subject.sub1 = Button(text=_("English"), size_hint_y=None, height=60)
    Subject.sub2 = Button(text=_("Russian"), size_hint_y=None, height=60)
    Subject.sub3 = Button(text=_("Belarussian"), size_hint_y=None, height=60)
    Subject.sub4 = Button(text=_("Math"), size_hint_y=None, height=60)
    Subject.sub5 = Button(text=_("Geography"), size_hint_y=None, height=60)
    Subject.sub6 = Button(text=_("Informatics"), size_hint_y=None, height=60)
    Subject.sub7 = Button(text=_("Physics"), size_hint_y=None, height=60)
    Subject.sub8 = Button(text=_("Biology"), size_hint_y=None, height=60)

    # binding subject buttons
    Subject.sub1.bind(on_release=subjectChange)
    Subject.sub2.bind(on_release=subjectChange)
    Subject.sub3.bind(on_release=subjectChange)
    Subject.sub4.bind(on_release=subjectChange)
    Subject.sub5.bind(on_release=subjectChange)
    Subject.sub6.bind(on_release=subjectChange)
    Subject.sub7.bind(on_release=subjectChange)
    Subject.sub8.bind(on_release=subjectChange)

    Subject.back = Button(text=_("Back"), size_hint_y=None, height=60)
    Subject.back.bind(on_release=partial(changeScreen, "Lang"))

    # Adding all widgets to layout
    Subject.layout.add_widget(Subject.sub1)
    Subject.layout.add_widget(Subject.sub2)
    Subject.layout.add_widget(Subject.sub3)
    Subject.layout.add_widget(Subject.sub4)
    Subject.layout.add_widget(Subject.sub5)
    Subject.layout.add_widget(Subject.sub6)
    Subject.layout.add_widget(Subject.sub7)
    Subject.layout.add_widget(Subject.sub8)
    Subject.layout.add_widget(Subject.back)

    Subject.view.add_widget(Subject.layout)

    # Adding screen to ScreenManager
    subscreen.add_widget(Subject.view)


def readyQuest(*args):
    """Confirming Question add"""
    for i in range(len(editQuest.input)):
        questions[editQuest.quest.text][i] = editQuest.input[i].text
    for i in range(len(editQuest.check)):
        answers[editQuest.quest.text][i] = editQuest.check[i].active
    changeScreen("Making")


def editQuest(inst):
    """Open view of Question editor"""

    # Clearing current view.
    editscreen.clear_widgets()

    # Adding main view.
    view = ScrollView(
        size_hint=(1, None), size=(Window.width, Window.height), bar_width=7
    )

    # Adding layout.
    layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
    layout.bind(minimum_height=layout.setter("height"))

    # Getting ID from button.
    id = int(inst.id)

    # Back button.
    back = Button(text=_("Back"), size_hint_y=None, height=60)
    back.bind(on_release=partial(changeScreen, "Making"))

    # Question label.
    editQuest.quest = Label(text=inst.text, size_hint_y=None)

    # Adding UI components to layout.
    layout.add_widget(back)
    layout.add_widget(editQuest.quest)

    # All our arrays for generating html file
    editQuest.input = []
    editQuest.check = []
    editQuest.subgrid = []

    # Allocating memory for answers.
    if not editQuest.quest.text in questions:
        questions[editQuest.quest.text] = [""] * len(Make.variants[id])

    # Allocating memory for correct/incorrect fields.
    if not editQuest.quest.text in answers:
        answers[editQuest.quest.text] = [False] * len(Make.variants[id])

    # Displaying all answers.
    for i in range(len(Make.variants[id])):
        # Layout to place checkbox and label in one line.
        subgrid = GridLayout(cols=2, spacing=0, size_hint_y=None, height=50)

        # Input for answer text.
        inp = TextInput(
            height=50, size_hint_y=None, text=questions[editQuest.quest.text][i]
        )

        # Checkbox for correct/incorrect answer flag.
        check = CheckBox(size_hint_x=None, width=50)

        # Label with number of question.
        lbl = Label(text=_("Answer number:") + " " + str(i + 1), height=50)

        # Adding to our arrays.
        editQuest.subgrid.append(subgrid)
        editQuest.input.append(inp)
        editQuest.check.append(check)

        # Adding checkbox and label to subgrid.
        subgrid.add_widget(check)
        subgrid.add_widget(lbl)

        # Adding all UI elements to layout.
        layout.add_widget(subgrid)
        layout.add_widget(inp)

    # Adding to view our layout.
    view.add_widget(layout)

    # Adding view to screen.
    editscreen.add_widget(view)

    # Ready button.
    ready = Button(text=_("Ready"), size_hint_y=None, height=60)
    ready.bind(on_release=readyQuest)

    # Adding button.
    layout.add_widget(ready)

    # Changing current screen.
    changeScreen("Edit")


def addQuestionWithAnswers(txt, num, *args):
    """Our popup for configuring question"""

    # If number is incorrect don't do anything.
    try:
        num = int(num.text)
    except ValueError:
        return

    # If length of question is equal to 0 don't do anything.
    if len(txt.text) == 0:
        return

    # Add array of answers.
    if not hasattr(Make, "variants"):
        Make.variants = []

    # Adding button to edit question.
    btn = Button(text=txt.text, size_hint_y=None, height=60, id=str(len(Make.variants)))
    btn.bind(on_release=editQuest)

    # Adding place for answers.
    Make.variants.append([""] * num)

    # Adding all UI elements to layout.
    Make.layout.add_widget(btn)
    Make.layout.remove_widget(Make.ready)
    Make.layout.remove_widget(Make.export)
    Make.layout.add_widget(Make.export)
    Make.layout.add_widget(Make.ready)

    # Disabling popups.
    addVariants.popup.dismiss()
    addQuest.popup.dismiss()


def addVariants(btn):
    """Question with some answers. Primitive."""

    # Main layout.
    addVariants.layout = GridLayout(cols=1, rows=6, spacing=5)

    # Our popup with input fields.
    addVariants.popup = Popup(
        title=_("Configuring question"),
        content=addVariants.layout,
        size_hint=(None, None),
        size=(600, 400),
        auto_dismiss=False,
    )

    # Label which inidicates where input for question is located.
    addVariants.label = Label(text=_("Write question here:"), size_hint=(1, 0.2))

    # Text input for question.
    addVariants.text = TextInput()

    # Label which indicates where input for number of answer is located.
    addVariants.number = Label(text=_("Number of answers:"), size_hint=(1, 0.2))

    # Text input for number of question.
    addVariants.num = TextInput(input_filter="int", size_hint=(1, 0.4), multiline=False)

    # Close button.
    addVariants.button = Button(text=_("Close"), size_hint=(1, 0.5))
    addVariants.button.bind(on_release=addVariants.popup.dismiss)

    # Button to continue.
    addVariants.nxt = Button(text=_("Next"), size_hint=(1, 0.5))
    addVariants.nxt.bind(
        on_release=partial(addQuestionWithAnswers, addVariants.text, addVariants.num)
    )

    # Adding all UI componets to layout.
    addVariants.layout.add_widget(addVariants.label)
    addVariants.layout.add_widget(addVariants.text)
    addVariants.layout.add_widget(addVariants.number)
    addVariants.layout.add_widget(addVariants.num)
    addVariants.layout.add_widget(addVariants.nxt)
    addVariants.layout.add_widget(addVariants.button)

    # Showing popup.
    addVariants.popup.open()


def addQuest(btn):
    """Popun where we can select type of question."""
    # Main layout.
    addQuest.layout = GridLayout(cols=1, spacing=5, size_hint_y=None)

    # Popup window.
    addQuest.popup = Popup(
        title=_("Choose type"),
        content=addQuest.layout,
        size_hint=(None, None),
        size=(400, 400),
        auto_dismiss=False,
    )

    # Close button.
    addQuest.button = Button(text=_("Close"), size_hint_y=None, height=40)
    addQuest.button.bind(on_release=addQuest.popup.dismiss)

    # Our types of question.
    addQuest.variants = Button(
        text=_("Question with answer variants"), size_hint_y=None, height=40
    )
    addQuest.variants.bind(on_release=addVariants)

    # Adding all to layout.
    addQuest.layout.add_widget(addQuest.variants)
    addQuest.layout.add_widget(addQuest.button)

    # Showing popup.
    addQuest.popup.open()


def Make():
    """Screen for configuring test"""
    # ScrollView, so you can see a lot of questions in window.
    Make.view = ScrollView(
        size_hint=(1, None), size=(Window.width, Window.height), bar_width=7
    )

    # Main layout where all UI objects will be placed.
    Make.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
    # Option for ScrollView.
    Make.layout.bind(minimum_height=Make.layout.setter("height"))

    # Import button.
    Make.imp = Button(text=_("Import"), size_hint_y=None, height=70)
    Make.imp.bind(on_release=imp)

    # Back button.
    Make.back = Button(text=_("Back"), size_hint_y=None, height=60)
    Make.back.bind(on_release=partial(changeScreen, "Subject"))

    # Label which indicates where test name input locates.
    Make.name_text = Label(text=_("Name of test"), size_hint_y=None, height=40)

    # Test name input.
    Make.name = TextInput(size_hint_y=None, height=40)

    # Label which indicates where test description input locates.
    Make.description_text = Label(
        text=_("Test description"), size_hint_y=None, height=40
    )

    # Test description input.
    Make.description = TextInput(size_hint_y=None, height=60)

    # More button.
    Make.new = Button(text=_("More"), size_hint_y=None, height=60)
    Make.new.bind(on_release=addQuest)

    # Ready button to finish test "baking".
    Make.ready = Button(text=_("Ready"), size_hint_y=None, height=60)
    Make.ready.bind(on_release=partial(lastScreen, False))

    Make.export = Button(text=_("Export"), size_hint_y=None, height=60)
    Make.export.bind(on_release=export)

    # Adding all UI elements to UI. Order is important, for more info read Kivy docs.
    Make.layout.add_widget(Make.imp)
    Make.layout.add_widget(Make.back)
    Make.layout.add_widget(Make.name_text)
    Make.layout.add_widget(Make.name)
    Make.layout.add_widget(Make.description_text)
    Make.layout.add_widget(Make.description)
    Make.layout.add_widget(Make.new)
    Make.layout.add_widget(Make.export)
    Make.layout.add_widget(Make.ready)

    # Adding layout to view.
    Make.view.add_widget(Make.layout)

    # Adding view to screen.
    makescreen.add_widget(Make.view)


# Function call, to initialize program (generate first screen)
Lang()

# Adding screens to Screen manager
sm.add_widget(subscreen)
sm.add_widget(langscreen)
sm.add_widget(makescreen)
sm.add_widget(editscreen)
sm.add_widget(readyscreen)


class MaketestApp(App):
    """Main class. Default App class in Kivy."""

    title = "Making test"

    def build(self):
        self.icon = "icon.png"
        sm.current = "Lang"
        return sm

    def on_pause(self):
        return True


if __name__ == "__main__":
    """Run!"""
    MaketestApp().run()
