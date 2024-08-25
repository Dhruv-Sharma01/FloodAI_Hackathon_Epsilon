import './navbar.css'
import UserModal from './usermodal'

function Navbar(){
    
    return(
        <nav>
            <div className="site-name">Epsilon Solutions</div>
            <div className="btn-section">
                <button type='button' className='btn'>Call Help</button>
                <UserModal />
            </div>
        </nav>
    )
}

export default Navbar