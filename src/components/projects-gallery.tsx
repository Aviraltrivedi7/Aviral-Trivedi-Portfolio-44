"use client";

import { useEffect, useRef, type CSSProperties } from "react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import Image from "next/image";
import { motion, useReducedMotion } from "framer-motion";
import { projects, type Project } from "@/lib/projects";

gsap.registerPlugin(ScrollTrigger);

function ProjectCard({ project }: { project: Project }) {
  const reduce = useReducedMotion();

  return (
    <motion.article
      initial={reduce ? false : { opacity: 0, y: 36 }}
      whileInView={reduce ? undefined : { opacity: 1, y: 0 }}
      viewport={{ once: true, margin: "-40px" }}
      transition={{ duration: 0.55, ease: [0.16, 1, 0.3, 1] }}
      whileHover={reduce ? undefined : {
        y: -8,
        boxShadow: `0 28px 72px -28px ${project.accent}b3, 0 0 34px -12px ${project.accent}66`,
      }}
      style={{
        "--project-accent": project.accent,
        boxShadow: "0 24px 60px -30px rgba(0,0,0,0.8)",
      } as CSSProperties}
      className="group relative flex min-h-[24rem] w-full flex-col rounded-2xl border border-white/10 bg-[#121215] text-fg transition-[border-color,box-shadow] duration-500 hover:border-[var(--project-accent)] sm:min-h-[26rem] md:h-[88%] md:w-[40vw] md:shrink-0 lg:w-[30vw] xl:w-[26vw]"
    >
      <div
        aria-hidden
        className="pointer-events-none absolute -inset-5 z-0 rounded-[2rem] opacity-0 blur-2xl transition-opacity duration-500 group-hover:opacity-70"
        style={{
          background: `radial-gradient(circle at 50% 35%, ${project.accent}66, transparent 68%)`,
        }}
      />
      <a href={`/projects/${project.slug}.html`} className="relative z-10 flex min-h-0 flex-1 flex-col overflow-hidden rounded-2xl">
        <div
          className="relative min-h-0 flex-1 overflow-hidden"
          style={{
            background: `radial-gradient(120% 120% at 18% 0%, ${project.accent}26, transparent 55%), linear-gradient(160deg, ${project.accent}3a, #101010 75%)`,
          }}
        >
          {/* Mockup Preview Image */}
          <div className="absolute inset-4 overflow-hidden rounded-xl border border-white/10 bg-black/40 shadow-xl transition-transform duration-500 group-hover:scale-[1.02]">
            <Image
              src={project.image}
              alt={`${project.title} interface preview`}
              fill
              sizes="(max-width: 640px) 82vw, (max-width: 768px) 46vw, (max-width: 1024px) 40vw, 26vw"
              className="object-cover object-center"
            />
          </div>

          <span
            className="absolute top-6 left-6 z-10 rounded-full px-3 py-1 text-xs font-medium uppercase tracking-widest backdrop-blur-md"
            style={{
              color: project.accent,
              background: "rgba(0,0,0,0.7)",
              boxShadow: `inset 0 0 0 1px ${project.accent}55`,
            }}
          >
            {project.tagline}
          </span>
        </div>

        <div className="flex shrink-0 items-end justify-between gap-4 p-6 bg-[#121215]">
          <div className="min-w-0">
            <h3 className="font-display text-xl font-bold tracking-tight text-white transition-colors group-hover:text-[var(--project-accent)] md:text-2xl">
              {project.title}
            </h3>
            <p className="mt-1.5 line-clamp-2 text-sm text-grey-2">
              {project.summary}
            </p>
          </div>
          <span className="shrink-0 font-display text-xs text-grey-2 border border-white/10 rounded-full px-2.5 py-1">
            {project.year}
          </span>
        </div>
      </a>
    </motion.article>
  );
}

export function ProjectsGallery() {
  const sceneRef = useRef<HTMLElement>(null);
  const trackRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const section = sceneRef.current;
    const track = trackRef.current;
    if (!section || !track) return;

    if (
      window.matchMedia("(prefers-reduced-motion: reduce)").matches ||
      window.matchMedia("(max-width: 767px)").matches
    ) {
      return;
    }

    const ctx = gsap.context(() => {
      gsap.to(track, {
        x: () => `-${track.scrollWidth - window.innerWidth + 120}px`,
        ease: "none",
        scrollTrigger: {
          trigger: section,
          start: "top top",
          end: "+=320vh",
          pin: true,
          scrub: 0.8,
          invalidateOnRefresh: true,
          anticipatePin: 1,
        },
      });
    }, section);

    return () => ctx.revert();
  }, []);

  return (
    <section
      id="projects"
      ref={sceneRef}
      // No min-height — pin-spacer provides the scroll space (1680vh)
      // Section only needs height for its content (header + track)
      className="relative scroll-mt-28 overflow-hidden bg-bg text-fg"
    >
      {/* Sticky header */}
      <div className="sticky top-0 z-10 shrink-0 px-8 pt-20 pb-2 md:px-16 bg-bg">
        <p className="mb-4 text-xs tracking-[0.3em] text-grey-2 uppercase">
          Selected Work
        </p>
        <h2 className="font-display text-5xl font-bold tracking-tight md:text-6xl lg:text-7xl">
          Projects
        </h2>
      </div>

      <div
        ref={trackRef}
        className="flex w-full flex-col items-stretch gap-6 px-6 py-8 md:h-[calc(100vh-14rem)] md:min-w-max md:flex-row md:flex-nowrap md:items-center md:overflow-hidden md:will-change-transform md:pl-[6vw] md:px-0 md:py-0"
      >
        {projects.map((p) => (
          <ProjectCard key={p.slug} project={p} />
        ))}
        {/* Large trailing spacer ensures last card fully visible */}
        <div className="hidden w-[150vw] shrink-0 md:block" />
      </div>
    </section>
  );
}