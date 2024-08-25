import './footer.css'

function Footer(){
    return(
        <div className="footer-section">
            <div className="logo">
                Epsilon Solutions
                <div className="sub">A new way to Predict Disaster</div>
            </div>
            <div className="verline"></div>
            <div className="emergencies">
                <h1>Emergency Contact</h1>
                <ul>
                    <li className='headnum'>Mumbai Police</li>
                    <li className='number'>Traffic WhatsApp Helpline : 8454999999</li>
                    <li className='headnum'>Mumbai Fire Service</li>
                    <li className='number'>Phone: 022 26677555</li>
                    <li className='headnum'>Disaster Management</li>
                    <li className='number'>Tel: +91 22 22694725 / 27</li>
                </ul>
            </div>
        </div>
    )
}

export default Footer