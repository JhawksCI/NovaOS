import { useState } from "react";
import BootScreen from "./components/BootScreen";
import Desktop from "./components/Desktop";

function App() {
    const [booted, setBooted] = useState(false);

    return (
        booted ? (
            <Desktop />
        ) : (
            <BootScreen onBootComplete={() => setBooted(true)} />
        )
    );
}

export default App;

