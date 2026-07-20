import {
    Folder,
    Terminal,
    Settings,
    ShoppingBag
} from "lucide-react";
import Taskbar from "./Taskbar";
import "../styles/desktop.css";

function Desktop() {
    const apps = [
        { name: "Files", icon: <Folder size={48} /> },
        { name: "Terminal", icon: <Terminal size={48} /> },
        { name: "Settings", icon: <Settings size={48} /> },
        { name: "Nova Store", icon: <ShoppingBag size={48} /> }
    ];

    return (
        <div className="desktop">
            <div className="icons">
                {apps.map((app, index) => (
                    <div key={index} className="app-icon">
                        {app.icon}
                        <span>{app.name}</span>
                    </div>
                ))}
            </div>

            {/* Barre des tâches modularisée */}
            <Taskbar />
        </div>
    );
}

export default Desktop;

