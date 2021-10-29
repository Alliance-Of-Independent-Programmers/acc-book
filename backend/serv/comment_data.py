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


comment1 = {
    "text": "So if we kill the enemy, the one waiting for us on the other side, will we finally be free?",
    "author": {
        "name": "Misha",
        "img": misha,
    },
  }


comment2 = {
  "text": "у меня дед картой был",
  "author": {
    "name": "Yaroslave",
    "img": yaroslav,
  },
}

comment3 = {
  "text": "А? Б...",
  "author": {
    "name": "Artem",
    "img": artem,
  },
}

comment4 = {
  "text": "Свою шизофрению на окружающих проецировать не следует.",
  "author": {
    "name": "Goblin",
    "img": goblin,
  },
}

comment5 = {
  "text": "Что такое осень? Это рошан...",
  "author": {
    "name": "Sany0k",
    "img": sanya,
  },
}

all_comment = [comment1, comment2, comment3, comment4, comment5]


