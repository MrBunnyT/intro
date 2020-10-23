import React from 'react'
import { handleAction } from './lookup'

function ActioBtn(props) {
    const { tweet, perform, action } = props;
    const actionHandler = (id, type) => {
        const data = {
            id: id,
            action: type,
        };
        handleAction(data, (response, status) => {
            if (status === 200) {
                perform(response);
            }
            if (status === 201) {
                perform(true)
            }
        });
    };
    if (action.type === "count") {
        return <button className="action-btn">{tweet.likes}</button>;
    }
    const button = (
        <button
            className="action-btn"
            onClick={() => actionHandler(tweet.id, action.type)}
        >
            {action.display}
        </button>
    );
    return button;
}

export { ActioBtn }