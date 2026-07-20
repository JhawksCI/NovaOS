import { useState } from "react";
import Window from "../windows/Window";
import "./desktop.css";


function Desktop(){

    const [windows, setWindows] = useState([]);


    function openWindow(name){

        if(!windows.includes(name)){

            setWindows([
                ...windows,
                name
            ]);

        }

    }


    function closeWindow(index){

        setWindows(
            windows.filter((_, i) => i !== index)
        );

    }


    return (

        <div className="desktop">


            <div 
                className="desktop-icon"
                onClick={() => openWindow("Files")}
            >
                📁 Files
            </div>


            <div 
                className="desktop-icon"
                onClick={() => openWindow("Terminal")}
            >
                💻 Terminal
            </div>


            <div 
                className="desktop-icon"
                onClick={() => openWindow("Calculator")}
            >
                🧮 Calculator
            </div>



            {
                windows.map((win, index) => (

                    <Window
                        key={index}
                        title={win}
                        onClose={() => closeWindow(index)}
                    >

                        <p>
                            {win} application
                        </p>

                    </Window>

                ))
            }


        </div>

    );

}


export default Desktop;
