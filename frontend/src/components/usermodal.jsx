import React, { useState } from 'react';
import Modal from 'react-modal';
import { FaUser } from 'react-icons/fa';

// Set the app element for accessibility (this is important)
Modal.setAppElement('#root');

const UserModal = () => {
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [name, setName] = useState('');
  const [number, setNumber] = useState('');

  const openModal = () => setModalIsOpen(true);
  const closeModal = () => setModalIsOpen(false);

  const handleNameChange = (e) => setName(e.target.value);
  const handleNumberChange = (e) => setNumber(e.target.value);

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission (e.g., save data or send it to a server)
    console.log("Name:", name);
    console.log("Number:", number);
    closeModal();
  };

  return (
    <div>
      <button type="button" onClick={openModal} style={{
        background: 'none',
        border: 'none',
        cursor: 'pointer',
        fontSize: '24px',
        color: 'black'
      }}>
        <FaUser />
      </button>
      <Modal
        isOpen={modalIsOpen}
        onRequestClose={closeModal}
        contentLabel="User Info Modal"
        style={{
          content: {
            top: '50%',
            left: '50%',
            right: 'auto',
            bottom: 'auto',
            marginRight: '-50%',
            transform: 'translate(-50%, -50%)',
            width: '400px',
            height: '300px',
            padding: '20px',
            borderRadius: '15px',
            textAlign: 'center'
          },
        }}
      >
        <h2>User Information</h2>
        <form onSubmit={handleSubmit}>
          <div style={{ marginBottom: '15px' }}>
            <label htmlFor="name" style={{ display: 'block', marginBottom: '5px' }}>Name:</label>
            <input
              type="text"
              id="name"
              value={name}
              onChange={handleNameChange}
              style={{
                width: '100%',
                padding: '8px',
                borderRadius: '5px',
                border: '1px solid #ccc'
              }}
              required
            />
          </div>
          <div style={{ marginBottom: '15px' }}>
            <label htmlFor="number" style={{ display: 'block', marginBottom: '5px' }}>Number:</label>
            <input
              type="tel"
              id="number"
              value={number}
              onChange={handleNumberChange}
              style={{
                width: '100%',
                padding: '8px',
                borderRadius: '5px',
                border: '1px solid #ccc'
              }}
              required
            />
          </div>
          <button type="submit" style={{
            padding: '10px 20px',
            borderRadius: '5px',
            backgroundColor: '#007BFF',
            color: 'white',
            border: 'none',
            cursor: 'pointer'
          }}>
            Submit
          </button>
        </form>
        <p style={{ marginTop: '20px', fontSize: '12px', color: 'gray' }}>
          Your number will only be used for sending alerts.
        </p>
      </Modal>
    </div>
  );
};

export default UserModal;
