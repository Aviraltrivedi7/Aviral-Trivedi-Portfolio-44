"use client";

import { useEffect, useRef } from "react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import Link from "next/link";
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
      className="group relative flex h-[88%] w-[82vw] shrink-0 flex-col overflow-hidden rounded-2xl border border-white/10 bg-[#121215] text-fg shadow-[0_24px_60px_-30px_rgba(0,0,0,0.8)] transition-all duration-300 hover:border-white/20 sm:w-[46vw] md:w-[40vw] lg:w-[30vw] xl:w-[26vw]"
    >
      <Link href={`/projects/${project.slug}`} prefetch={true} className="flex min-h-0 flex-1 flex-col">
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
            <h3 className="font-display text-xl font-bold tracking-tight md:text-2xl text-white group-hover:text-cyan-400 transition-colors">
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
      </Link>
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

    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
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
      className="relative overflow-hidden bg-bg text-fg"
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
        className="flex flex-nowrap items-center gap-6 overflow-hidden will-change-transform pl-[6vw]"
        style={{ 
          height: "calc(100vh - 14rem)",
          minWidth: "max-content"
        }}
      >
        {projects.map((p) => (
          <ProjectCard key={p.slug} project={p} />
        ))}
        {/* Large trailing spacer ensures last card fully visible */}
        <div className="w-[150vw] shrink-0" />
      </div>
    </section>
  );
}