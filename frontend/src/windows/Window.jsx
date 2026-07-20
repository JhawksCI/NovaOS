import "./window.css";


function Window({title, children, onClose}){

    return (

        <div className="window">

            <div className="window-bar">

                <span>{title}</span>

                <button onClick={onClose}>
                    ×
                </button>

            </div>


            <div className="window-content">

                {children}

            </div>

        </div>

    );

}


export default Window;
