import base64
import json

misha = base64.b64encode(open("../Pics/Miahs.jpg", "rb").read()).decode("UTF-8")
yaroslav = base64.b64encode(open("../Pics/Yaroslav.jpg", "rb").read()).decode("UTF-8")
goblin = base64.b64encode(open("../Pics/Goblin.jpg", "rb").read()).decode("UTF-8")
sanya = base64.b64encode(open("../Pics/Sanya.jpg", "rb").read()).decode("UTF-8")
artem = base64.b64encode(open("../Pics/Artem.jpg", "rb").read()).decode("UTF-8")


comment1 = {
    "text": "So if we kill the enemy, the one waiting for us on the other side, will we finally be free?",
    "author": {
        "name": "Misha",
        "avatarUrl": misha,
    },
  }


comment2 = {
  "text": "у меня дед картой был",
  "author": {
    "name": "Yaroslave",
    "avatarUrl": yaroslav,
  },
}

comment3 = {
  "text": "А? Б...",
  "author": {
    "name": "Artem",
    "avatarUrl": artem,
  },
}

comment4 = {
  "text": "Свою шизофрению на окружающих проецировать не следует.",
  "author": {
    "name": "Goblin",
    "avatarUrl": goblin,
  },
}

comment5 = {
  "text": "Что такое осень? Это рошан...",
  "author": {
    "name": "Sany0k",
    "avatarUrl": sanya,
  },
}

comments = [comment1, comment2, comment3, comment4, comment5]
filename = "comments.json"
with open(filename, "w", encoding="utf-8") as write_file:
    json.dump(comments, write_file, ensure_ascii=False)
    print("OK")

