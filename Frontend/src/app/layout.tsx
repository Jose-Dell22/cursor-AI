import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import NotificationContainer from "./components/NotificationContainer";

export const metadata: Metadata = {
  title: "Mentor Smart",
  description: "Tu plataforma de cursos y mentoría personalizada",
};

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="es">
      <head>
        <link rel="icon" href="/mentor.jpeg" type="image/jpeg" />
      </head>
      <body className={`${geistSans.variable} ${geistMono.variable}`}>
        {children}
        <NotificationContainer />
      </body>
    </html>
  );
}
