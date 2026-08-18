"use client";

import { motion } from "framer-motion";

const EDUCATION = [
  {
    institution: "Indian Institute of Technology (IIT), Madras",
    degree: "Software Engineering & Web Applications",
    period: "2025 – 2029",
    highlight: "Comprehensive program focusing on software architecture, full-stack web development, and algorithms.",
    badge: "Undergraduate",
  },
  {
    institution: "Kendriya Vidyalaya Mati Akbarpur, Kanpur Dehat",
    degree: "Senior Secondary School (Class XII)",
    period: "Completed",
    highlight: "Graduated with an outstanding 87.2% aggregate score in the Science stream.",
    badge: "Class XII",
  },
];

const CERTIFICATIONS = [
  {
    title: "Advanced Cybersecurity & Cyber Awareness 2025",
    issuer: "IIT Kanpur",
    tag: "Security",
  },
  {
    title: "Google Technical Support Fundamentals",
    issuer: "Google / Coursera",
    tag: "IT & Systems",
  },
  {
    title: "Oracle Certified Professional",
    issuer: "Oracle",
    tag: "Cloud & DB",
  },
  {
    title: "Frontend Web Development Internship",
    issuer: "AICTE / EduSkills / SmartBridge",
    tag: "Development",
  },
  {
    title: "Microsoft Office Specialist Certification",
    issuer: "Microsoft",
    tag: "Productivity",
  },
  {
    title: "Gemini Certified Student",
    issuer: "Google for Education",
    tag: "AI Tools",
  },
];

export function Testimonials() {
  return (
    <section
      id="education"
      className="relative px-6 py-28 md:px-16"
    >
      <div className="mx-auto max-w-6xl">
        <p className="mb-4 text-xs tracking-[0.3em] text-grey-2 uppercase">
          Academic & Credentials
        </p>
        <h2 className="mb-14 font-display text-5xl font-bold tracking-tight md:text-7xl">
          Education &<br />
          Achievements
        </h2>

        {/* Education Cards */}
        <div className="mb-16 grid grid-cols-1 gap-6 md:grid-cols-2">
          {EDUCATION.map((edu, idx) => (
            <motion.div
              key={idx}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.5, delay: idx * 0.1 }}
              className="relative flex flex-col justify-between overflow-hidden rounded-3xl border border-white/10 bg-grey-1 p-8 transition-all duration-300 hover:border-white/20 hover:shadow-[0_12px_40px_-15px_rgba(0,0,0,0.7)]"
            >
              <div>
                <div className="flex items-center justify-between gap-4">
                  <span className="rounded-full border border-accent/30 bg-accent/10 px-3 py-1 text-xs font-semibold tracking-wider text-accent uppercase">
                    {edu.badge}
                  </span>
                  <span className="font-display text-xs text-grey-2">
                    {edu.period}
                  </span>
                </div>
                <h3 className="mt-5 font-display text-2xl font-bold text-fg">
                  {edu.institution}
                </h3>
                <p className="mt-1 text-sm font-medium text-accent">
                  {edu.degree}
                </p>
                <p className="mt-4 text-sm leading-relaxed text-grey-2">
                  {edu.highlight}
                </p>
              </div>
            </motion.div>
          ))}
        </div>

        {/* Certifications Grid */}
        <div>
          <h3 className="mb-6 font-display text-xl font-semibold tracking-tight text-fg">
            Featured Certifications
          </h3>
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {CERTIFICATIONS.map((cert, idx) => (
              <motion.div
                key={idx}
                initial={{ opacity: 0, y: 15 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.4, delay: idx * 0.06 }}
                className="flex flex-col justify-between rounded-2xl border border-white/10 bg-white/[0.02] p-5 backdrop-blur-sm transition-colors hover:border-white/25 hover:bg-white/[0.04]"
              >
                <div>
                  <div className="flex items-center justify-between text-xs text-grey-2">
                    <span>{cert.issuer}</span>
                    <span className="rounded-md bg-white/5 px-2 py-0.5 text-[10px] text-white/70">
                      {cert.tag}
                    </span>
                  </div>
                  <h4 className="mt-3 font-display text-base font-semibold text-fg">
                    {cert.title}
                  </h4>
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}