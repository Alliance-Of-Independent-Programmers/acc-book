import misha from "../../../backend/Pics/Miahs.jpg";
import yaroslav from "../../../backend/Pics/Yaroslav.jpg";
import goblin from "../../../backend/Pics/Goblin.jpg";
import sanya from "../../../backend/Pics/Sanya.jpg";
import artem from "../../../backend/Pics/Artem.jpg";

const comment1 = {
  date: new Date(),
  text: "So if we kill the enemy, the one waiting for us on the other side, will we finally be free?",
  author: {
    name: "Misha",
    avatarUrl: misha,
  },
};

const comment2 = {
  date: new Date(),
  text: "у меня дед картой был",
  author: {
    name: "Yaroslave",
    avatarUrl: yaroslav,
  },
};

const comment3 = {
  date: new Date(),
  text: "А? Б...",
  author: {
    name: "Artem",
    avatarUrl: artem,
  },
};

const comment4 = {
  date: new Date(),
  text: "Свою шизофрению на окружающих проецировать не следует.",
  author: {
    name: "Goblin",
    avatarUrl: goblin,
  },
};

const comment5 = {
  date: new Date(),
  text: "Что такое осень? Это рошан...",
  author: {
    name: "Sany0k",
    avatarUrl: sanya,
  },
};

const comments = [comment1, comment2, comment3, comment4, comment5];

export default comments;
