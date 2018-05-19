from appJar import gui
import os

path = os.getcwd()

lng = ""
sub = ""

lngset = {
    "ru": {
        "bel" : "Белорусский",
        "rus" : "Русский",
        "eng" : "Английский",
        "subject" : "Выберете предмет",
        "crtst" : "Создание теста для ",
        "RusS" : "русского",
        "BelS" : "белорусского",
        "EngS" : "английского"
    },
    "en": {
        "bel" : "Belarussian",
        "rus" : "Russian",
        "eng" : "English",
        "subject" : "Choose subject",
        "crtst" : "Creating test for ",
        "RusS" : "russian",
        "BelS" : "belarussian",
        "EngS" : "english"
    },
    "by" : {
        "bel" : "Беларускi",
        "rus" : "Рускi",
        "eng" : "Анлельскi",
        "subject" : "Выбярыце прадмет",
        "crtst" : "Зрабленне теста для ",
        "RusS" : "русскага",
        "BelS" : "беларускага",
        "EngS" : "ангельская"
    }
}

def add():
    print("add")

def setLng(button):
    global lng
    if button == "ru":
        lng = "ru"
    elif button == "by":
        lng = "by"
    else:
        lng = "en"
    
    #choosing subject
    app.startSubWindow(lngset[lng]["subject"])

    app.addButton(lngset[lng]["bel"], setSub)
    app.addButton(lngset[lng]["rus"], setSub)
    app.addButton(lngset[lng]["eng"], setSub)

    app.stopSubWindow()

    app.showSubWindow(lngset[lng]["subject"])
    app.destroySubWindow("Choose language")

def setSub(button):
    global sub
    if button == lngset[lng]["bel"]:
        sub = "Bel"
    if button == lngset[lng]["rus"]:
        sub = "Rus"
    if button == lngset[lng]["eng"]:
        sub = "Eng"

    app.startSubWindow("crt", title=lngset[lng]["crtst"] + lngset[lng][sub+"S"])

    app.addButton("Add", add)

    app.stopSubWindow()

    app.destroySubWindow(lngset[lng]["subject"])
    app.showSubWindow("crt")

app = gui("1920x1080")

app.setFont(20)

app.setIcon(path+r"\favico.ico")

#choosing language
app.startSubWindow("Choose language")

app.addIconButton("ru", setLng, path+"\\ru")
app.addIconButton("by", setLng, path+"\\by")
app.addIconButton("en", setLng, path+"\\en")

app.stopSubWindow()

app.go(startWindow="Choose language")