import AppIcon from "../components/AppIcon";
import "./desktop.css";


function Desktop(){

    function openApp(app){

        console.log("Opening:", app);

    }


    return (

        <div className="desktop">


            <div className="icons">


                <AppIcon
                    name="Files"
                    icon="files"
                    onOpen={() => openApp("Files")}
                />


                <AppIcon
                    name="Calculator"
                    icon="calculator"
                    onOpen={() => openApp("Calculator")}
                />


                <AppIcon
                    name="Terminal"
                    icon="terminal"
                    onOpen={() => openApp("Terminal")}
                />


            </div>


        </div>

    );

}


export default Desktop;
