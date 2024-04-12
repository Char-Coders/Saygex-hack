import React, {useRef} from "react";
import ChatPane from "./chat/ChatPane.jsx";
import ChatSelectPane from "./chat/ChatSelectPane.jsx";
import "./chat/mainChatCSS.css"
import {useLocation, useParams} from "react-router-dom";

function MainChat() {
    const chatType = useRef(useParams().chatType === "doctor");

    return (
        <div style={{display: "flex", height: "100vh"}}>
            <div className="mainChatContainer" style={{height: "inherit"}}>
                {/*<ChatSelectPane />*/}
                <ChatPane isDoctor={chatType.current} />
            </div>
        </div>

    )
}

export default MainChat;