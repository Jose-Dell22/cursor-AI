'use client';
import styles from '../page.module.scss';

interface ErrorMessageProps {
  message?: string;
  onRetry?: () => void;
}

export default function ErrorMessage({ message = "Algo salió mal", onRetry }: ErrorMessageProps) {
  return (
    <div className={styles.heroBg}>
      <div className={styles.centerGlow}>
        <div className={styles.errorMessage}>
          <div className={styles.errorIcon}>⚠️</div>
          <h2>Error</h2>
          <p>{message}</p>
          {onRetry && (
            <button onClick={onRetry} className={styles.primaryBtn}>
              Intentar de nuevo
            </button>
          )}
          <a href="/" className={styles.secondaryBtn}>
            Volver al inicio
          </a>
        </div>
      </div>
    </div>
  );
} 