import base64
import os.path

path=os.path.dirname(__file__)

misha = base64.b64encode(open(os.path.join(path, "../Pics/Miahs.jpg"), "rb").read()).decode("UTF-8")
yaroslav = base64.b64encode(open(os.path.join(path, "../Pics/Yaroslav.jpg"), "rb").read()).decode("UTF-8")
goblin = base64.b64encode(open(os.path.join(path, "../Pics/Goblin.jpg"), "rb").read()).decode("UTF-8")
sanya = base64.b64encode(open(os.path.join(path, "../Pics/Sanya.jpg"), "rb").read()).decode("UTF-8")
artem = base64.b64encode(open(os.path.join(path, "../Pics/Artem.jpg"), "rb").read()).decode("UTF-8")
slava = base64.b64encode(open(os.path.join(path, "../Pics/Slava.jpg"), "rb").read()).decode("UTF-8")
andrew = base64.b64encode(open(os.path.join(path, "../Pics/Andrew.jpg"), "rb").read()).decode("UTF-8")
killreal = base64.b64encode(open(os.path.join(path, "../Pics/KillReal.jpg"), "rb").read()).decode("UTF-8")
mauri = base64.b64encode(open(os.path.join(path, "../Pics/Maury.jpg"), "rb").read()).decode("UTF-8")


online1 = {
    "login": "Artem",
    "img": artem,
}

online2 = {
    "login": "Slava",
    "img": slava,
}

online3 = {
    "login": "Misha",
    "img": misha,
}

online4 = {
    "login": "Andrew",
    "img": andrew,
}

online5 = {
    "login": "Goblin",
    "img": goblin,
}

online6 = {
    "login": "KillReal",
    "img": killreal,
}

online7 = {
    "login": "Mauri",
    "img": mauri,
}

online8 = {
    "login": "Sany0K",
    "img": sanya,
}

online9 = {
    "login": "Yaroslave",
    "img": yaroslav,
}

all_online = [
    online1,
    online2,
    online3,
    online4,
    online5,
    online6,
    online7,
    online8,
    online9,
]



