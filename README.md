# Aviral Trivedi Portfolio

A cinematic, scroll-driven developer portfolio built with Next.js App Router, TypeScript, Tailwind CSS, GSAP, Lenis, Framer Motion, and React Three Fiber.

## Requirements

Use Node.js 20 or newer and npm. The project uses `src/app` as the App Router source directory.

## Local development

```bash
npm ci
npm run dev
```

Open [http://localhost:3000](http://localhost:3000). The main editable entry point is `src/app/page.tsx`; reusable UI lives under `src/components`, and project content lives in `src/lib/projects.ts`.

## Quality checks

```bash
npm run lint
npm run build
npm audit
```

The build generates the home page and the four static project routes under `src/app/projects/[slug]`.

## Static export

For plain static hosting, build with:

```bash
NEXT_STATIC_EXPORT=true npm run build
```

The exported files are written to `out/`. Configure the host to serve clean project URLs such as `/projects/kanpur-metro-safar-guide` and to fall back to the matching generated HTML file where required. Vercel can deploy the normal Next.js build directly without static-export mode.

## Content and links

Project titles, descriptions, live demos, source links, accent colors, and image paths are maintained in `src/lib/projects.ts`. Only verified public source repositories should receive a `View GitHub Source Code` CTA. Private or unavailable repositories should leave the `github` field empty.

The CV is served from `public/cv.pdf`. The contact form currently prepares a `mailto:` message for `trivediaviral46@gmail.com`; a transactional email provider can be added later without changing the page structure.

## Project structure

| Path | Purpose |
|---|---|
| `src/app/page.tsx` | Home page composition |
| `src/app/projects/[slug]/page.tsx` | Static project detail pages and metadata |
| `src/app/layout.tsx` | Fonts, global metadata, navigation shell |
| `src/components/` | Hero, transitions, gallery, skills, contact, and 3D UI |
| `src/lib/projects.ts` | Project content and verified links |
| `src/lib/media.ts` | Pointer, reduced-motion, and hydration-safe media hooks |
| `public/` | Images, project mockups, favicon, and CV |
