'use client';
import { useState, useEffect } from 'react';
import styles from '../page.module.scss';

interface NotificationProps {
  message: string;
  type: 'success' | 'error' | 'info';
  duration?: number;
  onClose?: () => void;
}

export default function Notification({ message, type, duration = 5000, onClose }: NotificationProps) {
  const [isVisible, setIsVisible] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => {
      setIsVisible(false);
      onClose?.();
    }, duration);

    return () => clearTimeout(timer);
  }, [duration, onClose]);

  if (!isVisible) return null;

  const getIcon = () => {
    switch (type) {
      case 'success': return '✅';
      case 'error': return '❌';
      case 'info': return 'ℹ️';
      default: return 'ℹ️';
    }
  };

  return (
    <div className={`${styles.notification} ${styles[`notification${type.charAt(0).toUpperCase() + type.slice(1)}`]}`}>
      <span className={styles.notificationIcon}>{getIcon()}</span>
      <span className={styles.notificationMessage}>{message}</span>
      <button 
        onClick={() => {
          setIsVisible(false);
          onClose?.();
        }}
        className={styles.notificationClose}
      >
        ×
      </button>
    </div>
  );
} 