import { BatteryCharging } from "lucide-react";

function Battery() {

    return (

        <div className="status-item">

            <BatteryCharging size={18}/>
            <span>17%</span>

        </div>

    );

}

export default Battery;
