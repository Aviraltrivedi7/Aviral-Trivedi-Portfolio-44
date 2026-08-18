"use client";

import { useEffect, useRef } from "react";
import Image from "next/image";
import { gsap } from "gsap";

const NAME = "Aviral Trivedi";
const ROLE = "Full Stack Developer";

export function Hero() {
  const rootRef = useRef<HTMLElement>(null);
  const colorLayerRef = useRef<HTMLDivElement>(null);
  const ringRef = useRef<HTMLDivElement>(null);

  const handleMove = (e: React.MouseEvent<HTMLDivElement>) => {
    const wrap = e.currentTarget;
    const rect = wrap.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const radius = 72;
    const mask = `radial-gradient(circle ${radius}px at ${x}px ${y}px, #000 0 ${radius - 8}px, transparent ${radius}px)`;
    const colorLayer = colorLayerRef.current;
    if (colorLayer) {
      colorLayer.style.opacity = "1";
      colorLayer.style.maskImage = mask;
      (colorLayer.style as CSSStyleDeclaration & { webkitMaskImage: string }).webkitMaskImage = mask;
    }
    const ring = ringRef.current;
    if (ring) {
      ring.style.transform = `translate(${x}px, ${y}px) translate(-50%, -50%)`;
      ring.style.opacity = "1";
    }
  };

  const handleLeave = () => {
    if (colorLayerRef.current) colorLayerRef.current.style.opacity = "0";
    if (ringRef.current) ringRef.current.style.opacity = "0";
  };

  useEffect(() => {
    const ctx = gsap.context(() => {
      const reduced = window.matchMedia(
        "(prefers-reduced-motion: reduce)"
      ).matches;

      const tl = gsap.timeline({ defaults: { ease: "power3.out" } });
      tl.fromTo(
        "[data-wordmark]",
        { y: 60, opacity: 0 },
        { y: 0, opacity: 1, duration: 1.1, ease: "power2.out" }
      );
      tl.fromTo(
        "[data-photo]",
        { y: 140, opacity: 0 },
        { y: 0, opacity: 1, duration: 1.2, ease: "elastic.out(1, 0.7)" },
        "-=0.5"
      );
      tl.fromTo(
        "[data-scrollcue]",
        { opacity: 0 },
        { opacity: 1, duration: 0.8 },
        "-=0.4"
      );

      if (reduced) tl.progress(1);
    }, rootRef);
    return () => ctx.revert();
  }, []);

  return (
    <section
      id="hero"
      ref={rootRef}
      suppressHydrationWarning
      className="relative flex h-dvh flex-col items-center justify-center overflow-hidden bg-bg"
    >
      <div className="relative flex w-fit flex-col items-center" suppressHydrationWarning>
        {/* Name — small, left-aligned with the wordmark */}
        <span className="mb-3 w-full self-start font-display text-lg font-semibold tracking-tight text-fg md:text-2xl">
          {NAME}
        </span>

        {/* Wordmark + portrait overlay (photo sits IN FRONT of the text) */}
        <div className="relative" suppressHydrationWarning>
          <h1
            data-wordmark
            aria-hidden
            className="pointer-events-none z-0 whitespace-nowrap text-center font-display font-bold leading-none text-white/[0.09]"
            style={{ fontSize: "clamp(3.5rem, 12vw, 12rem)" }}
          >
            DEVELOPER
          </h1>

          <div
            data-photo
            suppressHydrationWarning
            onMouseMove={handleMove}
            onMouseLeave={handleLeave}
            className="absolute top-1/2 left-1/2 z-10 mb-20 h-[80vh] w-[min(60vw,360px)] -translate-x-1/2 -translate-y-1/2 cursor-none will-change-transform"
          >
            <Image
              src="/images/hero-cutout.png"
              alt="Aviral Trivedi"
              fill
              priority
              sizes="(max-width: 768px) 88vw, 360px"
              className="object-contain grayscale contrast-[1.05] drop-shadow-[0_24px_36px_rgba(0,0,0,0.45)]"
            />
            <div
              ref={colorLayerRef}
              aria-hidden
              className="pointer-events-none absolute inset-0 opacity-0 transition-opacity duration-150"
            >
              <Image
                src="/images/hero-cutout.png"
                alt=""
                fill
                priority
                sizes="(max-width: 768px) 88vw, 360px"
                className="object-contain"
              />
            </div>
            <div
              ref={ringRef}
              aria-hidden
              suppressHydrationWarning
              className="pointer-events-none absolute top-0 left-0 h-24 w-24 rounded-full border border-white/40 opacity-0 shadow-[0_0_30px_rgba(255,255,255,0.15)] transition-opacity duration-300 will-change-transform"
            />
          </div>
        </div>

        {/* Role — small, right-aligned with the wordmark (under the "R") */}
        <span className="mt-4 w-full max-w-[40vw] self-end text-right font-display text-xs tracking-wide text-grey-2 md:text-sm">
          {ROLE}
        </span>
      </div>

      <div
        data-scrollcue
        suppressHydrationWarning
        className="absolute bottom-8 z-10 flex h-10 w-6 items-start justify-center rounded-full border border-white/25 p-1.5"
      >
        <span className="h-2 w-1 animate-bounce rounded-full bg-grey-2" />
      </div>
    </section>
  );
}