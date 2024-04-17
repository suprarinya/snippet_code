import styles from './Modal.module.css'; 



const Modal = ({ isOpen, onClose, children }) => {

  if (!isOpen) {
    return null;
  }

  return (
    <div className={styles.modal} onClick={onClose}>
    <div className={styles.modalContent} onClick={e => e.stopPropagation()}>
      <button className={styles.closeButton} onClick={onClose}>Close</button>
      {children}
    </div>
  </div>
  );
};

export default Modal;
