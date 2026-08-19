"use client";

import Image from "next/image";
import { useEffect, useState, type CSSProperties } from "react";

type Certificate = {
  title: string;
  issuer: string;
  tag: string;
  preview: string;
  file: string;
  accent?: string;
};

export function CertificateCard({ certificate }: { certificate: Certificate }) {
  const [open, setOpen] = useState(false);
  const accent = certificate.accent ?? "#67e8f9";

  useEffect(() => {
    if (!open) return;
    const onKeyDown = (event: KeyboardEvent) => {
      if (event.key === "Escape") setOpen(false);
    };
    document.addEventListener("keydown", onKeyDown);
    document.body.style.overflow = "hidden";
    return () => {
      document.removeEventListener("keydown", onKeyDown);
      document.body.style.overflow = "";
    };
  }, [open]);

  return (
    <>
      <button
        type="button"
        onClick={() => setOpen(true)}
        className="group relative flex min-h-52 w-full flex-col justify-between overflow-hidden rounded-2xl border border-white/10 bg-white/[0.02] p-5 text-left backdrop-blur-sm transition-[border-color,background-color,box-shadow,transform] duration-500 hover:-translate-y-1 hover:border-[var(--cert-accent)] hover:bg-white/[0.055] hover:shadow-[0_0_32px_var(--cert-accent)] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--cert-accent)]"
        style={{ "--cert-accent": accent } as CSSProperties}
        aria-label={`Open ${certificate.title} certificate`}
      >
        <span
          aria-hidden
          className="pointer-events-none absolute -right-12 -top-16 h-40 w-40 rounded-full opacity-0 blur-3xl transition-opacity duration-500 group-hover:opacity-70"
          style={{ background: accent }}
        />
        <span
          aria-hidden
          className="pointer-events-none absolute inset-x-5 top-0 h-px opacity-0 transition-opacity duration-500 group-hover:opacity-100"
          style={{ background: `linear-gradient(90deg, transparent, ${accent}, transparent)` }}
        />
        <div className="relative z-10">
          <div className="flex items-start justify-between gap-4 text-xs text-grey-2">
            <span>{certificate.issuer}</span>
            <span className="rounded-md bg-white/5 px-2 py-0.5 text-[10px] text-white/70">
              {certificate.tag}
            </span>
          </div>
          <h4 className="mt-3 font-display text-base font-semibold text-fg">
            {certificate.title}
          </h4>
        </div>
        <span className="relative z-10 mt-5 text-xs font-semibold tracking-wider text-accent uppercase transition-all group-hover:translate-x-1 group-hover:text-[var(--cert-accent)]">
          View certificate ↗
        </span>
      </button>

      {open && (
        <div
          className="fixed inset-0 z-[100] grid place-items-center bg-black/85 p-4 backdrop-blur-md"
          role="dialog"
          aria-modal="true"
          aria-label={certificate.title}
          onClick={() => setOpen(false)}
        >
          <div
            className="relative flex max-h-[92vh] w-full max-w-5xl flex-col overflow-hidden rounded-3xl border border-white/15 bg-[#111116] shadow-2xl"
            style={{
              "--cert-accent": accent,
              boxShadow: `0 0 70px -20px ${accent}`,
            } as CSSProperties}
            onClick={(event) => event.stopPropagation()}
          >
            <div className="flex items-center justify-between gap-4 border-b border-white/10 px-5 py-4">
              <div>
                <p className="text-xs tracking-[0.2em] text-accent uppercase">{certificate.issuer}</p>
                <h3 className="mt-1 font-display text-lg font-semibold text-fg">{certificate.title}</h3>
              </div>
              <button
                type="button"
                onClick={() => setOpen(false)}
                className="grid h-10 w-10 shrink-0 place-items-center rounded-full border border-white/15 text-xl text-grey-2 transition-all hover:border-[var(--cert-accent)] hover:text-[var(--cert-accent)] hover:shadow-[0_0_20px_var(--cert-accent)]"
                aria-label="Close certificate preview"
              >
                ×
              </button>
            </div>
            <div className="relative min-h-0 flex-1 overflow-auto bg-black/30 p-3 sm:p-6">
              <Image
                src={certificate.preview}
                alt={`${certificate.title} certificate preview`}
                width={1600}
                height={1100}
                className="mx-auto h-auto max-h-[68vh] w-auto max-w-full rounded-xl object-contain"
              />
            </div>
            <div className="flex justify-end border-t border-white/10 px-5 py-3">
              <a
                href={certificate.file}
                target="_blank"
                rel="noopener noreferrer"
                className="rounded-full bg-fg px-4 py-2 text-xs font-semibold text-bg transition-colors hover:bg-accent"
              >
                Open original file ↗
              </a>
            </div>
          </div>
        </div>
      )}
    </>
  );
}
