import React, {useEffect, useRef, useState} from "react";
import InputBox from "./chatPane/InputBox.jsx";
import axios from "axios";

function ChatPane({isDoctor}) {

    const messagesEndRef = useRef(null);
    const [messages, setMessages] = useState([]);


    return (
        <div className="chatPaneContainer">
            <div className="introTextContainer">
                {isDoctor ? <>
                        <h1>Welcome doctor, I am <span>M</span>edi<span>M</span>ate!.</h1>
                        <h3>Your personal advisor chatbot</h3>
                    </> :
                    <>
                        <h1>Start a new chat with <span>M</span>edi<span>M</span>ate!.</h1>
                        <h3>Your personal healthcare chatbot</h3>
                    </>
                }
            </div>

            <div className="MessagesContainer">
                <div className="MessagesContainerScroll">
                    {messages}
                </div>
                <div id={"Messageanchor"}/>
            </div>

            <InputBox setMessages={setMessages} isDoctor={isDoctor} />
        </div>
    )
}

export default ChatPane;