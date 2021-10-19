import React from 'react';
import {Comment} from "./comment";

import misha from "./Pics/Miahs.jpg";
import slava from "./Pics/Slava.jpg";
import artem from "./Pics/Artem.jpg";

export function CommentView(props){
    return(
        <>{props.comments.map((comment)=>{
            return <Comment
                date={comment.date}
                text={comment.text}
                author={comment.author}
            />
        })}
            {/*<Comment*/}
            {/*date={props.comment1.date}*/}
            {/*text={props.comment1.text}*/}
            {/*author={props.comment1.author}*/}
            {/*/>*/}
            {/*<Comment*/}
            {/*date={props.comment2.date}*/}
            {/*text={props.comment2.text}*/}
            {/*author={props.comment2.author}*/}
            {/*/>*/}
        </>
    )
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

// ReactDOM.render(
//     <CommentView
//         comments = {comments}
//     />,
//     document.getElementById('root')
// );
