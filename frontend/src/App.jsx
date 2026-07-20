import { useState } from "react";

import BootScreen from "./components/BootScreen";
import Desktop from "./desktop/Desktop";
import Taskbar from "./components/Taskbar";


function App() {

    const [booted, setBooted] = useState(false);


    return (

        booted ? (

            <>
                <Desktop />
                <Taskbar />
            </>

        ) : (

            <BootScreen 
                onFinish={() => setBooted(true)}
            />

        )

    );

}


export default App;
