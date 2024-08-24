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
                <div className="heading">Emergency Number</div>
            </div>
        </div>
    )
}

export default SafeZone