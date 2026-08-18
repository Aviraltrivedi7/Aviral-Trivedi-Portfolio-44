import type { Metadata } from "next";
import { Inter, Space_Grotesk } from "next/font/google";
import "./globals.css";
import { SmoothScroll } from "@/components/smooth-scroll";
import { Nav } from "@/components/nav";
import { Cursor } from "@/components/cursor";

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
});

const spaceGrotesk = Space_Grotesk({
  variable: "--font-space-grotesk",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  metadataBase: new URL("https://aviraltrivedi.in"),
  title: "Aviral Trivedi | Full Stack Developer",
  description:
    "Personal portfolio of Aviral Trivedi — Full Stack Developer building fast, interactive web applications, 3D experiences, and modern UI solutions.",
  alternates: {
    canonical: "/",
  },
  openGraph: {
    title: "Aviral Trivedi | Full Stack Developer",
    description:
      "Personal portfolio of Aviral Trivedi — Full Stack Developer building fast, interactive web applications, 3D experiences, and modern UI solutions.",
    url: "https://aviraltrivedi.in/",
    siteName: "Aviral Trivedi Portfolio",
    images: [
      {
        url: "/profile-card.webp",
        width: 450,
        height: 671,
        alt: "Aviral Trivedi — Full Stack Developer",
      },
    ],
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "Aviral Trivedi | Full Stack Developer",
    description:
      "Personal portfolio of Aviral Trivedi — Full Stack Developer building fast, interactive web applications, 3D experiences, and modern UI solutions.",
    images: ["/profile-card.webp"],
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html
      lang="en"
      className={`${inter.variable} ${spaceGrotesk.variable} antialiased`}
      suppressHydrationWarning
    >
      <body className="min-h-full bg-bg text-fg" suppressHydrationWarning>
        <SmoothScroll>
          <Nav />
          {children}
          <Cursor />
        </SmoothScroll>
      </body>
    </html>
  );
}