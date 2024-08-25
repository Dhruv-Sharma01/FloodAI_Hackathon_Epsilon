import React, { useState } from 'react';
import DisasterContactModal from './disastermodal';
import './navbar.css'
import UserModal from './usermodal'

function Navbar(){
    const [modalIsOpen, setModalIsOpen] = useState(false);
    return(
        <nav>
            <div className="site-name">Epsilon Solutions</div>
            <div className="btn-section">
                <button type='button' className='btn' onClick={() => setModalIsOpen(true)}>Call Help</button>
                <DisasterContactModal isOpen={modalIsOpen} 
        onClose={() => setModalIsOpen(false)}  />
                <UserModal />
            </div>
        </nav>
    )
}

export default Navbar