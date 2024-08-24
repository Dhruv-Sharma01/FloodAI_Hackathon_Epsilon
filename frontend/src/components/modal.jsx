import React, { useState } from 'react';
import Modal from 'react-modal';

// Set the app element for accessibility (this is important)
Modal.setAppElement('#root');

const MModal = ({Severity = "Normal"}) => {
  const [modalIsOpen, setModalIsOpen] = useState(false);

  const openModal = () => setModalIsOpen(true);
  const closeModal = () => setModalIsOpen(false);

  return (
    // open this when there is severe flood in your area
    <div>
        <button type="button" onClick={openModal}>Open</button>
      <Modal
        isOpen={modalIsOpen}
        onRequestClose={closeModal}
        contentLabel="Example Modal"
        style={{
          content: {
            top: '50%',
            left: '50%',
            right: 'auto',
            bottom: 'auto',
            marginRight: '-50%',
            transform: 'translate(-50%, -50%)',
            width: '400px',
            height: '200px',
            padding: '20px',
            backgroundColor: 'red',
            borderRadius: '15px',
            color: 'white',
            textAlign: 'center'
          },
        }}
      >
        <h2 style={{ fontWeight: 'bold'}}>Severity: {Severity}</h2>
        <p>Content goes here...</p>
        <button onClick={closeModal}>Close Modal</button>
      </Modal>
    </div>
  );
};

export default MModal;
