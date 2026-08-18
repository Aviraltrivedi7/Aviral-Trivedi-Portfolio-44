import { skills } from "@/lib/skills";
import { BrandMark } from "@/components/brand-mark";

export function Skills() {
  return (
    <section id="skills" className="px-6 py-32 md:px-16">
      <p className="mb-4 text-xs tracking-[0.3em] text-grey-2 uppercase">
        Toolkit
      </p>
      <h2 className="mb-14 font-display text-5xl font-bold tracking-tight text-fg md:text-7xl">
        Skills
      </h2>

      <div className="grid grid-cols-3 gap-3 md:gap-4">
        {skills.map((s) => (
          <button
            key={s.name}
            type="button"
            className="skill-pill group relative grid h-16 place-items-center rounded-full border border-white/10 bg-grey-1 text-fg transition-[border-color,box-shadow,background-color,color] duration-300"
            style={
              {
                "--skill-bg": s.bg,
                "--skill-logo": s.logoColor,
              } as React.CSSProperties
            }
          >
            <span className="skill-label font-display text-sm font-semibold tracking-wide md:text-base">
              {s.name}
            </span>
            <span className="skill-logo text-white">
              <BrandMark name={s.name} size={24} />
            </span>
          </button>
        ))}
      </div>
    </section>
  );
}