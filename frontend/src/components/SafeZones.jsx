import './SafeZone.css'

function SafeZone() {
    return (
        <div className="prediction">
            <div className="alert-notifcation">
                <div className="heading">Alerts</div>
            </div>

            <div className="safeareas">
                <div className="heading">Nearby Safe Areas</div>
                <div className="safe-maps"></div>
            </div>

            <div className="Emergency">
                <div className="heading">Guidelines</div>
                <p className='guidelines'>
                <ul>
        <li>Monitor weather updates and emergency alerts.</li>
        <li>Pack an emergency kit with essential supplies.</li>
        <li>Plan and know your evacuation routes.</li>
        <li>Secure your home and turn off utilities.</li>
        <li>Evacuate immediately if advised by authorities.</li>
        <li>Avoid walking or driving through floodwaters.</li>
        <li>Move to higher ground if trapped.</li>
        <li>If driving, turn around and find a safe route.</li>
        <li>Keep your phone charged and stay in touch.</li>
        <li>Listen to and follow official instructions.</li>
        <li>Avoid contact with contaminated floodwater.</li>
        <li>Wear protective clothing and prevent hypothermia.</li>
        <li>Return home only when it's declared safe.</li>
        <li>Document property damage for insurance.</li>
        <li>Clean up safely and dispose of hazardous items.</li>
        <li>Seek assistance from disaster relief services.</li>
        <li>Watch for secondary hazards like landslides.</li>
        <li>Continue monitoring local news for updates.</li>
      </ul>
                </p>
            </div>
        </div>
    )
}

export default SafeZone