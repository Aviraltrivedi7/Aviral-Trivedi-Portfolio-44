export type Project = {
  slug: string;
  title: string;
  tagline: string;
  year: string;
  role: string;
  summary: string;
  problem: string;
  solution: string;
  stack: string[];
  live?: string;
  github?: string;
  accent: string;
};

export const projects: Project[] = [
  {
    slug: "kanpur-metro-safar-guide",
    title: "Kanpur Metro Safar Guide",
    tagline: "Metro Navigation PWA · React",
    year: "2025 - 2026",
    role: "Lead Frontend & PWA Developer",
    summary:
      "An independent guide and real-time route planner app to navigate the Kanpur Metro with station timings, interactive maps, fare calculator, and offline PWA capability.",
    problem:
      "Daily commuters and visitors in Kanpur needed a fast, reliable, bilingual route navigation and fare calculation tool that works seamlessly even in low-network underground stations.",
    solution:
      "Built a Progressive Web App (PWA) using React and Tailwind CSS featuring dynamic station-to-station route computation (IIT Kanpur to Kanpur Central), interactive line maps, Hindi/English localization, and instant offline caching.",
    stack: ["React.js", "Tailwind CSS", "PWA (Service Workers)", "Lucide Icons", "Vercel"],
    live: "https://kanpur-metro-safar-guide.vercel.app/",
    github: "https://github.com/Aviraltrivedi7/kanpur-metro-safar-guide",
    accent: "#06b6d4",
  },
  {
    slug: "smartbudget-ai",
    title: "SmartBudget AI",
    tagline: "AI Finance Tracker · React & Charts",
    year: "2026",
    role: "Full-stack Developer",
    summary:
      "An intelligent personal finance and budgeting dashboard featuring interactive expenditure analytics, income/expense tracking, and AI-driven saving recommendations.",
    problem:
      "Users often struggle to maintain consistency in manual expense logging and lack automated insights into their spending habits and category breakdowns.",
    solution:
      "Developed a comprehensive financial tracking web app with interactive Chart.js visualizations, net balance calculations, categorized logs, and smart insights for budgeting efficiency.",
    stack: ["React.js", "Tailwind CSS", "Chart.js", "AI Insights", "Vercel"],
    live: "https://smartbudget-ai-enhanced7.vercel.app/",
    github: "https://github.com/Aviraltrivedi7",
    accent: "#10b981",
  },
  {
    slug: "cryptodashboard",
    title: "CryptoDashboard",
    tagline: "Real-time Crypto Console · React",
    year: "2026",
    role: "Frontend Developer",
    summary:
      "A real-time cryptocurrency portfolio tracker and market data console displaying global stats, interactive candlestick charts, and top token performance metrics.",
    problem:
      "Crypto investors require high-frequency live market data, historical charts, and portfolio breakdown in a fast, responsive interface without clutter.",
    solution:
      "Built a real-time console with market cap metrics, live candlestick graphs, 24h price trend charts, search filtering, and responsive currency tables.",
    stack: ["React.js", "REST APIs", "Tailwind CSS", "Chart.js", "TradingView Widgets"],
    live: "https://cryptodashboard11425.vercel.app/",
    github: "https://github.com/Aviraltrivedi7",
    accent: "#f59e0b",
  },
  {
    slug: "aviral-cyber-os-portfolio",
    title: "3D Cyber OS Portfolio",
    tagline: "Interactive 3D Portfolio · Three.js",
    year: "2025",
    role: "Creator & 3D Developer",
    summary:
      "An interactive 3D portfolio experience featuring Three.js canvas, retro CLI terminal (Aviral Cyber OS v3.0), theme switchers, and dynamic project showcase decks.",
    problem:
      "Traditional static portfolio resumes often fail to showcase interactive graphics skills, creative engineering, and command-line mastery.",
    solution:
      "Designed and deployed an immersive web portfolio featuring custom 3D mesh rendering, an interactive command-line interface with custom commands, and keyboard shortcut search.",
    stack: ["React.js", "Three.js", "Tailwind CSS", "GSAP", "Vite"],
    live: "https://aviraltrivedi.in/",
    github: "https://github.com/Aviraltrivedi7",
    accent: "#ec4899",
  },
];

export function getProject(slug: string): Project | undefined {
  return projects.find((p) => p.slug === slug);
}