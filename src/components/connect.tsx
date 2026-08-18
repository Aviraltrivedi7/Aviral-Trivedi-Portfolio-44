"use client";

import { useState } from "react";
import { socials, SocialIcon } from "@/components/social-icons";
import { scrollToSection } from "@/lib/scroll";

const SOCIAL_LINKS: Partial<Record<string, string>> = {
  whatsapp: "https://wa.me/919219797581?text=Hello!",
  linkedin: "https://www.linkedin.com/in/aviral-trivedi0/",
  github: "https://github.com/Aviraltrivedi7",
};

const EMAIL = "trivediaviral46@gmail.com";

export function Connect() {
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const fd = new FormData(e.currentTarget);
    const subject = encodeURIComponent(
      `Portfolio contact from ${fd.get("name")}`
    );
    const body = encodeURIComponent(
      `${fd.get("message")}\n\nReply to: ${fd.get("email")}`
    );
    setSubmitted(true);
    window.location.href = `mailto:${EMAIL}?subject=${subject}&body=${body}`;
  };

  return (
    <footer className="relative px-6 pt-40 pb-10 md:px-16">
      <section id="connect" className="mb-32">
        <p className="mb-6 text-xs tracking-[0.3em] text-grey-2 uppercase">
          Get in touch
        </p>
        <h2 className="font-display text-7xl font-bold tracking-tight md:text-9xl">
          Let&rsquo;s
          <br />
          Connect
        </h2>

        <div className="mt-16 flex flex-col gap-12 md:flex-row md:items-start md:justify-between">
          <div className="flex flex-col gap-6">
            <div className="space-y-2">
              <a
                href={`mailto:${EMAIL}`}
                className="font-display text-lg text-fg transition-colors hover:text-accent md:text-xl"
              >
                {EMAIL}
              </a>
              <p className="text-sm text-grey-2">Kanpur, Uttar Pradesh, India</p>
            </div>

            <div className="flex gap-3">
              {Object.entries(socials)
                .filter(([name]) => SOCIAL_LINKS[name])
                .map(([name, def]) => (
                <a
                  key={name}
                  href={SOCIAL_LINKS[name]}
                  target="_blank"
                  rel="noopener noreferrer"
                  aria-label={name}
                  className="social-btn grid h-12 w-12 place-items-center rounded-full border border-white/10 transition-[color,box-shadow,border-color] duration-300"
                  style={{ "--brand": def.brand } as React.CSSProperties}
                >
                  <SocialIcon name={name} className="h-5 w-5" />
                </a>
                ))}
            </div>
          </div>

          <form onSubmit={handleSubmit} className="grid w-full max-w-md gap-3">
            <div className="grid grid-cols-2 gap-3">
              <div>
                <label htmlFor="contact-name" className="sr-only">Name</label>
                <input
                  id="contact-name"
                  name="name"
                  required
                  autoComplete="name"
                  placeholder="Name"
                  className="w-full rounded-2xl border border-white/10 bg-grey-1 px-4 py-3 text-sm outline-none placeholder:text-grey-2 focus:border-white/40"
                />
              </div>
              <div>
                <label htmlFor="contact-email" className="sr-only">Email</label>
                <input
                  id="contact-email"
                  name="email"
                  type="email"
                  required
                  autoComplete="email"
                  placeholder="Email"
                  className="w-full rounded-2xl border border-white/10 bg-grey-1 px-4 py-3 text-sm outline-none placeholder:text-grey-2 focus:border-white/40"
                />
              </div>
            </div>
            <div>
              <label htmlFor="contact-message" className="sr-only">Message</label>
              <textarea
                id="contact-message"
                name="message"
                required
                rows={3}
                placeholder="Message"
                className="w-full resize-none rounded-2xl border border-white/10 bg-grey-1 px-4 py-3 text-sm outline-none placeholder:text-grey-2 focus:border-white/40"
              />
            </div>
            <button
              type="submit"
              className="mt-1 rounded-full bg-fg px-6 py-3 text-sm font-medium text-bg transition-colors hover:bg-accent"
            >
              Send
            </button>
            {submitted && (
              <p className="text-sm text-grey-2" role="status">
                Your email app should open with the message prepared. If it does not, email me directly at {EMAIL}.
              </p>
            )}
          </form>
        </div>
      </section>

      <div className="flex flex-col items-center justify-between gap-4 border-t border-white/10 pt-8 text-xs text-grey-2 sm:flex-row">
        <p>© {new Date().getFullYear()} · All rights reserved · Made by Aviral Trivedi</p>
        <button
          onClick={() => scrollToSection("#hero")}
          className="transition-colors hover:text-fg"
        >
          Back to top ↑
        </button>
      </div>
    </footer>
  );
}