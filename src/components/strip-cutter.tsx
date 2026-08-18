"use client";

import { useEffect, useRef } from "react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { usePrefersReducedMotion } from "@/lib/media";

gsap.registerPlugin(ScrollTrigger);

const TILES = 7;
const COPIES = 4;

function bandTiles() {
  return Array.from({ length: TILES }).map((_, i) => (
    <span
      key={i}
      aria-hidden
      className="flex items-center gap-[0.3em] px-[0.45em]"
    >
      {Array.from({ length: COPIES }).map((_, j) => (
        <span key={j} className="px-[0.12em]">
          PROJECTS
        </span>
      ))}
    </span>
  ));
}

/**
 * Projects "strip cutter": two black diagonal strips cross at the screen centre
 * forming a tight X. Scrolling DOWN squeezes the X closed (strips rotate inward
 * toward each other); scrolling UP reverses, opening it again. The "PROJECTS"
 * type crawls along each strip. Everything is scrubbed 1:1 to the scroll, so
 * the motion stops the moment you stop scrolling.
 */
export function StripCutter() {
  const reduced = usePrefersReducedMotion();
  const rootRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const root = rootRef.current;
    if (!root || reduced) return;

    const ctx = gsap.context(() => {
      const st = ScrollTrigger.create({
        trigger: root,
        start: "top top",
        end: "bottom bottom",
        scrub: true, // 1:1 — freezes with the scroll
      });

      // The X itself is static (police-tape cross). Only the "PROJECTS" type
      // inside each strip crawls, scrubbed to the scroll.
      root.querySelectorAll<HTMLElement>("[data-hmarq]").forEach((el) => {
        gsap.fromTo(
          el,
          { xPercent: 0 },
          { xPercent: -100 / TILES, ease: "none", scrollTrigger: st }
        );
      });

      return () => st.kill();
    }, root);

    return () => ctx.revert();
  }, [reduced]);

  const SIZE = "clamp(2.6rem, 6.5vw, 5.5rem)";

  return (
    <div
      ref={rootRef}
      className="relative overflow-hidden bg-fg"
      style={{ height: "105vh" }}
    >
      <div className="sticky top-0 h-screen overflow-hidden">
        <div className="pointer-events-none absolute inset-0 flex items-center justify-center">
          {/* Strip A */}
          <div
            data-band-a
            className="absolute h-[16vh] w-[170vw] overflow-hidden bg-bg rotate-[14deg] will-change-transform"
          >
            <div
              data-hmarq
              className="flex w-max items-center whitespace-nowrap font-display font-black uppercase leading-none tracking-[0.12em] text-fg will-change-transform"
              style={{ fontSize: SIZE }}
            >
              {bandTiles()}
            </div>
          </div>
          {/* Strip B — the reverse diagonal, together forming an X */}
          <div
            data-band-b
            className="absolute h-[16vh] w-[170vw] overflow-hidden bg-bg -rotate-[14deg] will-change-transform"
          >
            <div
              data-hmarq
              className="flex w-max items-center whitespace-nowrap font-display font-black uppercase leading-none tracking-[0.12em] text-fg will-change-transform"
              style={{ fontSize: SIZE }}
            >
              {bandTiles()}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}