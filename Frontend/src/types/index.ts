// Types generados a partir de Backend/specs/00_contracts.md

export type Course = {
  id: number;
  name: string;
  description: string;
  thumbnail: string;
  slug: string;
  created_at: string;
  updated_at: string;
  deleted_at: string;
  teacher_id: number[];
};

export type Clase = {
  id: number;
  course_id: number;
  name: string;
  description: string;
  slug: string;
  video_url: string;
  created_at: string;
  updated_at: string;
  deleted_at: string;
};

export type Teacher = {
  id: number;
  name: string;
  email: string;
  created_at: string;
  updated_at: string;
  deleted_at: string;
};

// Respuesta de GET /courses
export type CourseListItem = Pick<Course, 'id' | 'name' | 'description' | 'thumbnail' | 'slug'>;

// Respuesta de GET /courses/:slug
export type CourseDetail = Omit<Course, 'created_at' | 'updated_at' | 'deleted_at'> & {
  teacher_id: number[];
  classes: Array<Pick<Clase, 'id' | 'name' | 'description' | 'slug'>>;
};

// Respuesta de GET /courses/:slug/classes/:id
export type ClaseDetail = Clase; 