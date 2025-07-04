'use client';
import styles from '../page.module.scss';

export default function CourseSkeleton() {
  return (
    <div className={styles.step}>
      <div className={styles.skeletonImage}></div>
      <div className={styles.skeletonTitle}></div>
      <div className={styles.skeletonDescription}></div>
      <div className={styles.skeletonDescription} style={{ width: '80%' }}></div>
    </div>
  );
} 