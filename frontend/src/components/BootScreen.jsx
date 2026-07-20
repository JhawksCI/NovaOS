import { useEffect, useState } from "react";
import "../styles/boot.css";

function BootScreen({ onBootComplete }) { // Réception du callback
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

        // Déclenche la transition vers le bureau après la fin du boot
        setTimeout(() => {
            onBootComplete();
        }, 4500);
    }, [onBootComplete]);

    return (
        <div className="boot-screen">
            {/* Ton contenu logo, logs et loader inchangé */}
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

