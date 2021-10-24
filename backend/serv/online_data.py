import base64
import json
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
  "author": {
    "name": "Artem",
    "avatarUrl": artem,
  },
}

online2 = {
  "author": {
    "name": "Slava",
    "avatarUrl": slava,
  },
}

online3 = {
  "author": {
    "name": "Misha",
    "avatarUrl": misha,
  },
}

online4 = {
  "author": {
    "name": "Andrew",
    "avatarUrl": andrew,
  },
}

online5 = {
  "author": {
    "name": "Goblin",
    "avatarUrl": goblin,
  },
}

online6 = {
  "author": {
    "name": "KillReal",
    "avatarUrl": killreal,
  },
}

online7 = {
  "author": {
    "name": "Mauri",
    "avatarUrl": mauri,
  },
}

online8 = {
  "author": {
    "name": "Sany0K",
    "avatarUrl": sanya,
  },
}

online9 = {
  "author": {
    "name": "Yaroslave",
    "avatarUrl": yaroslav,
  },
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



