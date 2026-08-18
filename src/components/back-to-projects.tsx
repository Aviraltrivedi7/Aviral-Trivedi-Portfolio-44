"use client";

import { useRouter } from "next/navigation";

/**
 * Returns to the home route at the Projects section without relying on a
 * fixed timeout that can race slow client-side navigation.
 */
export function BackToProjects() {
  const router = useRouter();

  const onClick = () => {
    router.push("/#projects");
  };

  return (
    <button
      onClick={onClick}
      className="inline-flex items-center gap-2 text-sm text-grey-2 transition-colors hover:text-fg"
    >
      <span aria-hidden>←</span> Back to projects
    </button>
  );
}