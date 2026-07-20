import { Folder, Calculator, Terminal } from "lucide-react";

function AppIcon({name, icon, onOpen}) {

    const icons = {
        files: Folder,
        calculator: Calculator,
        terminal: Terminal
    };

    const Icon = icons[icon];

    return (

        <div 
            className="app-icon"
            onDoubleClick={onOpen}
        >

            <Icon size={42}/>

            <span>{name}</span>

        </div>

    );

}

export default AppIcon;
