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
    <div className={styles.page}>
      <h1>Platzi Flix</h1>
      <main className={styles.main}>
        <div className={styles.coursesGrid}>
          {courses.map((course) => (
            <Link href={`/courses/${course.slug}`} className={styles.card} key={course.id}>
              <img
                className={styles.cardImage}
                src={course.thumbnail}
                alt={course.name}
                width={180}
                height={120}
              />
              <div className={styles.cardTitle}>{course.name}</div>
              <div className={styles.cardDesc}>{course.description}</div>
            </Link>
          ))}
        </div>
      </main>
    </div>
  );
}
