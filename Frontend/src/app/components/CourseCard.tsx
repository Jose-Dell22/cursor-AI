'use client';
import Link from 'next/link';
import styles from '../page.module.scss';
import { CourseListItem } from '../../types';

interface CourseCardProps {
  course: CourseListItem;
}

export default function CourseCard({ course }: CourseCardProps) {
  return (
    <Link href={`/courses/${course.slug}`} className={styles.step}>
      <div className={styles.courseImageContainer}>
        <img
          className={styles.courseImage}
          src={course.thumbnail || '/placeholder-course.webp'}
          alt={course.name}
          onError={(e) => {
            const target = e.target as HTMLImageElement;
            target.src = '/placeholder-course.webp';
          }}
        />
      </div>
      <h3>{course.name}</h3>
      <p>{course.description || 'Sin descripción disponible'}</p>
    </Link>
  );
} 