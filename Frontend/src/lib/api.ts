// Lista de posibles backends para producción y previews
const BACKEND_DOMAINS = [
  'https://cursor-ai-xi.vercel.app',
  'https://cursor-ai-git-main-jose-dell-22s-projects.vercel.app',
  'https://cursor-ai-jose-dell-22s-projects.vercel.app'
];

// Selecciona el backend según la variable de entorno o usa el primero como fallback
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || BACKEND_DOMAINS[0];

export const apiConfig = {
  baseUrl: API_BASE_URL,
  endpoints: {
    courses: `${API_BASE_URL}/courses`,
    teachers: `${API_BASE_URL}/teachers`,
    classes: `${API_BASE_URL}/classes`,
  }
};

export async function fetchApi(endpoint: string, options?: RequestInit) {
  const url = `${API_BASE_URL}${endpoint}`;
  const response = await fetch(url, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...options?.headers,
    },
  });
  
  if (!response.ok) {
    throw new Error(`API Error: ${response.status}`);
  }
  
  return response.json();
} 