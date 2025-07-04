'use client';
import { useState, useEffect } from "react";
import Link from "next/link";
import styles from "./page.module.scss";
import { CourseListItem } from "../types";
import LoadingSpinner from "./components/LoadingSpinner";
import ErrorMessage from "./components/ErrorMessage";
import CourseCard from "./components/CourseCard";
import CourseSkeleton from "./components/CourseSkeleton";

async function getCourses(): Promise<CourseListItem[]> {
  const res = await fetch("http://localhost:8000/courses/", { cache: "no-store" });
  if (!res.ok) throw new Error("Failed to fetch courses");
  return res.json();
}

export default function Home() {
  const [courses, setCourses] = useState<CourseListItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchCourses = async () => {
    try {
      setLoading(true);
      setError(null);
      const coursesData = await getCourses();
      setCourses(coursesData);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Error al cargar los cursos");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchCourses();
  }, []);

  if (loading) {
    return (
      <div className={styles.heroBg}>
        <div className={styles.topButtons}>
          <a
            href="https://wa.me/573213460838"
            target="_blank"
            rel="noopener noreferrer"
            className={styles.primaryBtn}
          >
            WhatsApp
          </a>
          <a
            href="https://www.instagram.com/josefernandodell?igsh=MWczMnQ1dDA3cnYybA=="
            target="_blank"
            rel="noopener noreferrer"
            className={styles.secondaryBtn}
          >
            Instagram
          </a>
        </div>
        <div className={styles.centerGlow}>
          <img src="/mentor.jpeg" alt="Mentor Smart" className={styles.demoImage} />
        </div>
        <div className={styles.stepsSection}>
          <h2>Cursos y Servicios Disponibles</h2>
          <div className={styles.stepsGrid}>
            {[1, 2, 3, 4, 5, 6].map((i) => (
              <CourseSkeleton key={i} />
            ))}
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return <ErrorMessage message={error} onRetry={fetchCourses} />;
  }

  return (
    <div className={styles.heroBg}>
      <div className={styles.topButtons}>
        <a
          href="https://wa.me/573213460838"
          target="_blank"
          rel="noopener noreferrer"
          className={styles.primaryBtn}
        >
          WhatsApp
        </a>
        <a
          href="https://www.instagram.com/josefernandodell?igsh=MWczMnQ1dDA3cnYybA=="
          target="_blank"
          rel="noopener noreferrer"
          className={styles.secondaryBtn}
        >
          Instagram
        </a>
      </div>
      <div className={styles.centerGlow}>
        <img src="/mentor.jpeg" alt="Mentor Smart" className={styles.demoImage} />
      </div>
      <div className={styles.stepsSection}>
        <h2>Cursos y Servicios Disponibles</h2>
        <div className={styles.stepsGrid}>
          {courses.map((course) => (
            <CourseCard key={course.id} course={course} />
          ))}
        </div>
      </div>
    </div>
  );
}
