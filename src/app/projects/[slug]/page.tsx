import type { Metadata } from "next";
import { notFound } from "next/navigation";
import Image from "next/image";
import { getProject, projects } from "@/lib/projects";
import { BackToProjects } from "@/components/back-to-projects";

type Props = { params: Promise<{ slug: string }> };

export function generateStaticParams() {
  return projects.map((p) => ({ slug: p.slug }));
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { slug } = await params;
  const project = getProject(slug);
  if (!project) return { title: "Not found" };
  return {
    title: `${project.title} — Projects | Aviral Trivedi`,
    description: project.summary,
  };
}

export default async function ProjectPage({ params }: Props) {
  const { slug } = await params;
  const project = getProject(slug);
  if (!project) notFound();

  let imgPath = `/projects/${project.slug}.png`;
  if (project.slug === "kanpur-metro-safar-guide") imgPath = "/projects/kanpur-metro.png";
  if (project.slug === "smartbudget-ai") imgPath = "/projects/smartbudget.png";
  if (project.slug === "cryptodashboard") imgPath = "/projects/cryptodashboard.png";
  if (project.slug === "aviral-cyber-os-portfolio") imgPath = "/projects/cyber-os.png";

  return (
    <article className="relative min-h-screen bg-bg text-fg px-6 pt-24 pb-20 md:px-16">
      <BackToProjects />

      <div className="mx-auto mt-6 max-w-5xl">
        <div className="flex flex-wrap items-center justify-between gap-4">
          <p
            className="text-xs font-semibold tracking-[0.25em] uppercase"
            style={{ color: project.accent }}
          >
            {project.tagline} · {project.year}
          </p>

          {project.live && (
            <a
              href={project.live}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-2 rounded-full border px-4 py-1.5 text-xs font-semibold tracking-wider uppercase transition-all duration-300 hover:scale-105"
              style={{
                borderColor: `${project.accent}66`,
                color: project.accent,
                backgroundColor: `${project.accent}15`,
              }}
            >
              <span className="h-2 w-2 rounded-full animate-ping" style={{ backgroundColor: project.accent }} />
              Live Project Demo ↗
            </a>
          )}
        </div>

        <h1 className="mt-4 max-w-3xl font-display text-4xl font-black tracking-tight md:text-6xl lg:text-7xl">
          {project.title}
        </h1>

        <p className="mt-5 max-w-2xl text-base leading-8 text-grey-2 md:text-lg">
          {project.summary}
        </p>

        {/* Big Showcase Visual Box with Rich Mockup */}
        <div
          className="group relative mt-10 aspect-[16/9] w-full overflow-hidden rounded-3xl border border-white/15 bg-[#121218] shadow-[0_30px_90px_-20px_rgba(0,0,0,0.9)] transition-all duration-500 hover:border-white/30"
          style={{
            boxShadow: `0 20px 60px -15px ${project.accent}25`,
          }}
        >
          {/* Subtle accent glow in background */}
          <div
            aria-hidden
            className="pointer-events-none absolute -top-24 -left-24 h-96 w-96 rounded-full opacity-20 blur-3xl"
            style={{ backgroundColor: project.accent }}
          />

          {/* Real Mockup Image */}
          <img
            src={imgPath}
            alt={`${project.title} Interface Showcase`}
            className="h-full w-full object-cover object-center transition-transform duration-700 group-hover:scale-[1.01]"
          />

          {/* Overlay Tag */}
          <div className="absolute bottom-4 right-4 rounded-xl border border-white/10 bg-black/60 px-3 py-1.5 backdrop-blur-md">
            <span className="text-xs font-medium text-white/80">Interactive Web Product</span>
          </div>
        </div>

        {/* Details Grid */}
        <div className="mt-14 grid grid-cols-1 gap-12 md:grid-cols-3">
          <section className="md:col-span-2 space-y-10">
            <div className="rounded-3xl border border-white/10 bg-white/[0.02] p-8 backdrop-blur-sm">
              <h2 className="mb-3 font-display text-2xl font-bold tracking-tight text-fg flex items-center gap-2">
                <span className="h-2 w-2 rounded-full" style={{ backgroundColor: project.accent }} />
                The Challenge
              </h2>
              <p className="text-base leading-relaxed text-grey-2">
                {project.problem}
              </p>
            </div>

            <div className="rounded-3xl border border-white/10 bg-white/[0.02] p-8 backdrop-blur-sm">
              <h2 className="mb-3 font-display text-2xl font-bold tracking-tight text-fg flex items-center gap-2">
                <span className="h-2 w-2 rounded-full bg-emerald-400" />
                The Solution & Architecture
              </h2>
              <p className="text-base leading-relaxed text-grey-2">
                {project.solution}
              </p>
            </div>
          </section>

          <aside className="space-y-8">
            <div className="rounded-3xl border border-white/10 bg-white/[0.02] p-6 backdrop-blur-sm">
              <h3 className="mb-2 text-xs tracking-[0.25em] text-grey-2 uppercase font-semibold">
                My Role
              </h3>
              <p className="font-display text-lg font-bold text-fg">{project.role}</p>
            </div>

            <div className="rounded-3xl border border-white/10 bg-white/[0.02] p-6 backdrop-blur-sm">
              <h3 className="mb-3 text-xs tracking-[0.25em] text-grey-2 uppercase font-semibold">
                Technologies & Tools
              </h3>
              <ul className="flex flex-wrap gap-2">
                {project.stack.map((s) => (
                  <li
                    key={s}
                    className="rounded-full border border-white/10 bg-white/[0.04] px-3.5 py-1 text-xs font-medium text-grey-2 transition-colors hover:border-white/30 hover:text-fg"
                  >
                    {s}
                  </li>
                ))}
              </ul>
            </div>

            <div className="flex flex-col gap-3">
              {project.live && (
                <a
                  href={project.live}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="rounded-full bg-fg px-6 py-3 text-center text-sm font-semibold text-bg transition-transform duration-200 hover:scale-[1.02] hover:bg-accent"
                >
                  Launch Live Application ↗
                </a>
              )}
              {project.github && (
                <a
                  href={project.github}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="rounded-full border border-white/15 bg-white/[0.02] px-6 py-3 text-center text-sm font-semibold text-grey-2 transition-all duration-200 hover:border-white/40 hover:text-fg hover:bg-white/[0.05]"
                >
                  View GitHub Source Code ↗
                </a>
              )}
            </div>
          </aside>
        </div>
      </div>
    </article>
  );
}