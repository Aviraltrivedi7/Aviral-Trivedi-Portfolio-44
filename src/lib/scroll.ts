import type Lenis from "lenis";

let lenis: Lenis | null = null;

export function setLenis(instance: Lenis | null) {
  lenis = instance;
}

export function getLenis() {
  return lenis;
}

export function scrollToSection(target: string) {
  if (lenis) {
    lenis.scrollTo(target, { offset: -96, duration: 1.2 });
  } else {
    const element = document.querySelector<HTMLElement>(target);
    if (!element) return;
    const top = element.getBoundingClientRect().top + window.scrollY - 96;
    window.scrollTo({ top: Math.max(0, top), behavior: "smooth" });
  }
}
