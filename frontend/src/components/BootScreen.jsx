import { useEffect, useState } from "react";
import "../styles/boot.css";

function BootScreen({ onFinish }) {
    const [lines, setLines] = useState([]);
    const [progress, setProgress] = useState(0);

    const bootLines = [
        "Loading Kernel",
        "Starting Services",
        "Checking Storage",
        "Network Ready"
    ];

    useEffect(() => {
        bootLines.forEach((line, index) => {
            setTimeout(() => {
                setLines(prev => [...prev, line]);
                setProgress(((index + 1) / bootLines.length) * 100);
            }, (index + 1) * 800);
        });

        // Fin du démarrage dynamique
        setTimeout(() => {
            onFinish();
        }, (bootLines.length + 1) * 800);
    }, [onFinish]); // Ajout de onFinish dans le tableau des dépendances

    return (
        <div className="boot-screen">
            <div className="nova-logo">
                {"NOVAOS".split("").map((letter, index) => (
                    <span key={index} style={{ animationDelay: `${index * 0.2}s` }}>
                        {letter}
                    </span>
                ))}
            </div>
            
            <p className="subtitle">Modern System Interface</p>
            
            <div className="boot-log">
                {lines.map((line, index) => (
                    <div key={index}>[✓] {line}</div>
                ))}
            </div>
            
            <div className="loader">
                <div className="progress" style={{ width: `${progress}%` }}></div>
            </div>
        </div>
    );
}

export default BootScreen;

