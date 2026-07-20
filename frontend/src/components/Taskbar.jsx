import "../styles/taskbar.css";
import NovaButton from "./NovaButton";
import Clock from "./Clock";
import Battery from "./Battery";
import Network from "./Network";

import { Folder, Terminal, Settings, ShoppingBag } from "lucide-react";

function Taskbar() {

    return (

        <div className="taskbar">

            <div className="taskbar-left">

                <NovaButton/>

            </div>


            <div className="taskbar-center">

                <Folder size={22}/>
                <Terminal size={22}/>
                <Settings size={22}/>
                <ShoppingBag size={22}/>

            </div>


            <div className="taskbar-right">

                <Network/>

                <Battery/>

                <Clock/>

            </div>

        </div>

    );

}

export default Taskbar;
