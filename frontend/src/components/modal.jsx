import React, { useState } from 'react';
import Modal from 'react-modal';

// Set the app element for accessibility (this is important)
Modal.setAppElement('#root');

const MModal = ({ Severity = "Risk" }) => {
  const [modalIsOpen, setModalIsOpen] = useState(false);

  const openModal = () => setModalIsOpen(true);
  const closeModal = () => setModalIsOpen(false);

  // Set the color based on severity
  const getBackgroundColor = () => {
    switch (Severity) {
      case "Risk":
        return 'red';
      case "Moderate":
        return 'orange';
      case "Normal":
      default:
        return 'green';
    }
  };

    // Set the message based on severity
    const getMessage = () => {
      switch (Severity) {
        case "Risk":
          return 'Evacuate to safe areas as quickly as possible.';
        case "Moderate":
          return 'Your area is probable to be flooded, take the necessary precautions.';
        case "Normal":
        default:
          return 'You are in a safe zone.';
      }
    };

  return (
    <div>
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
            backgroundColor: getBackgroundColor(),
            borderRadius: '15px',
            color: 'white',
            textAlign: 'center'
          },
        }}
      >
        <div className="headTitle">
          <h2 className='modtitle'>Severity: {Severity}</h2>
          <span className='cross' onClick={closeModal}> &#10005; </span>
        </div>
        <p className='message'>{getMessage()}</p>
      </Modal>
    </div>
  );
};

export default MModal;
