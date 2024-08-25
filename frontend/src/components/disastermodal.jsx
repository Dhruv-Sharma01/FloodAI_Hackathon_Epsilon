// DisasterContactModal.js
import React from 'react';
import Modal from 'react-modal';
import './disaster.css'

// Ensure that the app element is set for accessibility
Modal.setAppElement('#root');

const DisasterContactModal = ({ isOpen, onClose }) => {
  return (
    <Modal
      isOpen={isOpen}
      onRequestClose={onClose}
      contentLabel="Disaster Management Contacts"
      className="modal"
      overlayClassName="overlay"
    >
      <h2>Disaster Management Contacts - Mumbai</h2>
      <ul>
        <li><strong>Mumbai Fire Brigade:</strong> 101</li>
        <li><strong>Mumbai Police:</strong> 100</li>
        <li><strong>Mumbai Municipal Corporation (BMC):</strong> 1916</li>
        <li><strong>National Disaster Response Force (NDRF):</strong> 1078</li>
        <li><strong>Ambulance Service:</strong> 102</li>
        <li><strong>Indian Red Cross Society:</strong> +91 22 2204 1627</li>
        <li><strong>Child Helpline:</strong> 1098</li>
      </ul>
      <button onClick={onClose}>Close</button>
    </Modal>
  );
};

export default DisasterContactModal;
