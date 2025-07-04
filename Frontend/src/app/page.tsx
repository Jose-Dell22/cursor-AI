'use client';
import Link from "next/link";
import styles from "./page.module.scss";
import { CourseListItem } from "../types";

async function getCourses(): Promise<CourseListItem[]> {
  const res = await fetch("http://localhost:8000/courses/", { cache: "no-store" });
  if (!res.ok) throw new Error("Failed to fetch courses");
  return res.json();
}

export default async function Home() {
  const courses = await getCourses();
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
            <Link href={`/courses/${course.slug}`} className={styles.step} key={course.id}>
              <img
                className={styles.icon}
                src={course.thumbnail}
                alt={course.name}
                width={64}
                height={64}
              />
              <h3>{course.name}</h3>
              <p>{course.description}</p>
            </Link>
          ))}
        </div>
      </div>
    </div>
  );
}
