'use client';
import styles from '../page.module.scss';

export default function LoadingSpinner() {
  return (
    <div className={styles.heroBg}>
      <div className={styles.centerGlow}>
        <div className={styles.loadingSpinner}>
          <div className={styles.spinner}></div>
          <p>Cargando...</p>
        </div>
      </div>
    </div>
  );
} 