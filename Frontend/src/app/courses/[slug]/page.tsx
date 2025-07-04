import styles from "../../page.module.scss";
import { CourseListItem } from "../../../types";
import { use } from "react";

async function getCourse(slug: string): Promise<CourseListItem | null> {
  try {
    const res = await fetch(`http://localhost:8000/courses/${slug}`, {
      cache: 'no-store'
    });
    if (!res.ok) {
      return null;
    }
    return res.json();
  } catch (error) {
    console.error('Error fetching course:', error);
    return null;
  }
}

export default async function CourseDetail({ params }: { params: { slug: Promise<string> } }) {
  const slug = await params.slug;
  const course = await getCourse(slug);

  if (!course) {
    return (
      <div className={styles.heroBg}>
        <div className={styles.centerGlow}>
          <p>Curso no encontrado</p>
          <a href="/" className={styles.primaryBtn}>Volver</a>
        </div>
      </div>
    );
  }

  return (
    <div className={styles.heroBg}>
      <div className={styles.centerGlow}>
        <img src={course.thumbnail} alt={course.name} className={styles.demoImage} />
      </div>
      <div className={styles.stepsSection}>
        <h2>{course.name}</h2>
        <p>{course.description}</p>
        <p><b>Profesor:</b> Jose Fernando Dell</p>
        <img
          src="https://i.imgur.com/td8A0RX.jpeg"
          alt="Profesor Jose Fernando Dell"
          style={{ maxWidth: 320, width: '100%', borderRadius: 12, margin: '16px 0' }}
        />
        <div style={{ marginTop: '20px' }}>
          <a href="/" className={styles.primaryBtn}>Volver</a>
        </div>
      </div>
    </div>
  );
} 