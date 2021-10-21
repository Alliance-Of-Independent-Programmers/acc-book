import misha from "./Pics/Miahs.jpg";
import slava from "./Pics/Slava.jpg";
import artem from "./Pics/Artem.jpg";

const comment1 = {
  date: new Date(),
  text: "1 comment misha",
  author: {
    name: "Misha",
    avatarUrl: misha,
  },
};

const comment2 = {
  date: new Date(),
  text: "2 comment Slava",
  author: {
    name: "Slava",
    avatarUrl: slava,
  },
};

const comment3 = {
  date: new Date(),
  text: "3 comment Artem",
  author: {
    name: "Artem",
    avatarUrl: artem,
  },
};

const comments = [comment1, comment2, comment3];

export default comments;
