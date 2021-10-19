import React from 'react';
import {CommentView} from "./comment_view";
import './styles.css';

import ReactDOM from "react-dom";
import misha from "./Pics/Miahs.jpg";
import slava from "./Pics/Slava.jpg";
import artem from "./Pics/Artem.jpg";





function CommentPage(props) {
    return (
        <div className="CommentPage">
            <header className="header">
                <nav className="nav_links">
                    <nav className="nav_link_left">
                        <a className="nav_link" href="#">Форум |</a>
                        <a className="nav_link" href="#">Сообщество |</a>
                        <a className="nav_link" href="#">еще что-то </a>
                    </nav>
                    <nav className="nav_link_right">
                        <a className="nav_link" href="#">Вход |</a>
                        <a className="nav_link" href="#"> Регистрация</a>
                    </nav>
                </nav>
            </header>
            <div className="container">
                <div className="left">
                    <h3>Online</h3>
                    <p>Misha</p>
                    <p>Andrew</p>
                    <p>Perfest</p>
                    <p>Vova</p>
                    <p>Dima</p>
                </div>
                <div className="right">
                    <CommentView
                        comments = {comments}
                    />
                </div>
            </div>
        </div>);
}

const comment1 = {
    date: new Date(),
    text: '1 comment misha',
    author: {
        name: 'Misha',
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

ReactDOM.render(
    <CommentPage
    />,
    document.getElementById('root')
);