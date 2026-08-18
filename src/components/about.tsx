"use client";

import dynamic from "next/dynamic";
import { TextOutline } from "@/components/text-outline";

const TechObject = dynamic(
  () => import("@/components/tech-object").then((m) => m.TechObject),
  {
    ssr: false,
    loading: () => (
      <div className="h-full w-full animate-pulse rounded-2xl bg-grey-1" />
    ),
  }
);

export function About() {
  return (
    <section className="grid h-full min-h-screen w-full grid-cols-1 items-center gap-6 bg-fg px-6 py-12 text-bg sm:px-10 md:grid-cols-2 md:px-16 md:py-0">
      {/* Left: intro + scroll-responsive outline heading */}
      <div className="flex flex-col justify-center max-w-xl">
        <p className="mb-3 text-xs tracking-[0.3em] text-black/50 uppercase font-semibold">
          About Me
        </p>
        {/* Scroll-responsive outline fill */}
        <TextOutline className="font-display font-extrabold tracking-tight text-[clamp(2.4rem,5vw,5.2rem)] leading-[1.04]">
          Building fast,
          <br />
          modern web.
        </TextOutline>
        <p className="mt-5 text-sm leading-relaxed text-black/80 sm:text-base sm:leading-7 md:text-[17px] md:leading-8">
          I’m a <strong className="font-semibold text-black">Full Stack Developer</strong> with a passion for building robust web applications, interactive 3D web interfaces, and production-ready digital products. From progressive web apps like <span className="font-medium text-black">Kanpur Metro Safar Guide</span> to AI-integrated financial dashboards, I craft systems that blend clean engineering with seamless user experiences.
        </p>
      </div>

      {/* Right: realistic 3D tech object */}
      <div className="relative flex h-[320px] sm:h-[400px] md:h-[480px] items-center justify-center overflow-hidden">
        <div className="h-full w-full max-w-[480px]">
          <TechObject />
        </div>
      </div>
    </section>
  );
}