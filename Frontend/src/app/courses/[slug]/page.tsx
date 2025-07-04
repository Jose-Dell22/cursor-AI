'use client';
import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import styles from "../../page.module.scss";
import { CourseListItem } from "../../../types";
import LoadingSpinner from "../../components/LoadingSpinner";
import ErrorMessage from "../../components/ErrorMessage";

import { apiConfig } from "../../../lib/api";

async function getCourse(slug: string): Promise<CourseListItem | "not_found" | null> {
  try {
    const res = await fetch(`${apiConfig.endpoints.courses}/${slug}`, {
      cache: 'no-store'
    });
    if (res.status === 404) return "not_found";
    if (!res.ok) return null;
    return res.json();
  } catch (error) {
    console.error('Error fetching course:', error);
    return null;
  }
}

export default function CourseDetail({ params }: { params: { slug: string } }) {
  const [course, setCourse] = useState<CourseListItem | null>(null);
  const [notFound, setNotFound] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const router = useRouter();

  const fetchCourse = async () => {
    try {
      setLoading(true);
      setError(null);
      setNotFound(false);
      const courseData = await getCourse(params.slug);
      if (courseData === "not_found") {
        setNotFound(true);
        setCourse(null);
      } else if (courseData) {
        setCourse(courseData);
      } else {
        setError("Curso no encontrado");
        setCourse(null);
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : "Error al cargar el curso");
      setCourse(null);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchCourse();
  }, [params.slug]);

  if (loading) {
    return <LoadingSpinner />;
  }

  if (notFound) {
    return (
      <div className={styles.heroBg}>
        <div className={styles.centerGlow}>
          <img src="/mentor.jpeg" alt="Mentor Smart" className={styles.demoImage} style={{ marginBottom: 24 }} />
        </div>
        <div className={styles.centerGlow}>
          <div className={styles.errorMessage}>
            <div className={styles.errorIcon}>🔍</div>
            <h2>Curso no encontrado</h2>
            <p>El curso que buscas no existe o fue eliminado.</p>
            <a href="/" className={styles.primaryBtn}>Volver al inicio</a>
          </div>
        </div>
      </div>
    );
  }

  if (error || !course) {
    return (
      <ErrorMessage 
        message={error || "Curso no encontrado"} 
        onRetry={fetchCourse}
      />
    );
  }

  return (
    <div className={styles.heroBg}>
      <div className={styles.centerGlow}>
        <img 
          src={course.thumbnail || '/placeholder-course.webp'} 
          alt={course.name} 
          className={styles.demoImage}
          onError={(e) => {
            const target = e.target as HTMLImageElement;
            target.src = '/placeholder-course.webp';
          }}
        />
      </div>
      <div className={styles.stepsSection}>
        <h2>{course.name}</h2>
        <p>{course.description || 'Sin descripción disponible'}</p>
        <p><b>Profesor:</b> Jose Fernando Dell</p>
        <img
          src="https://i.imgur.com/td8A0RX.jpeg"
          alt="Profesor Jose Fernando Dell"
          style={{ maxWidth: 320, width: '100%', borderRadius: 12, margin: '16px 0' }}
        />
        <div style={{ marginTop: '20px' }}>
          <button onClick={() => router.back()} className={styles.primaryBtn}>
            Volver
          </button>
        </div>
      </div>
    </div>
  );
} 