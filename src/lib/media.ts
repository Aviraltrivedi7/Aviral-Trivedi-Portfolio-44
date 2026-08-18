import { useSyncExternalStore } from "react";

function subscribe(callback: () => void) {
  const mq = window.matchMedia("(pointer: fine)");
  mq.addEventListener("change", callback);
  return () => mq.removeEventListener("change", callback);
}

/**
 * True when the device has a fine pointer (mouse). Consumers combine this
 * with usePrefersReducedMotion() when motion should also be disabled.
 */
export function useFinePointer() {
  return useSyncExternalStore(
    subscribe,
    () => window.matchMedia("(pointer: fine)").matches,
    () => true
  );
}

function subscribeReduced(callback: () => void) {
  const mq = window.matchMedia("(prefers-reduced-motion: reduce)");
  mq.addEventListener("change", callback);
  return () => mq.removeEventListener("change", callback);
}

export function usePrefersReducedMotion() {
  return useSyncExternalStore(
    subscribeReduced,
    () => window.matchMedia("(prefers-reduced-motion: reduce)").matches,
    () => false
  );
}

function subscribeNoop() {
  return () => {};
}

/** True only after hydration, without a cascading state update in an effect. */
export function useMounted() {
  return useSyncExternalStore(
    subscribeNoop,
    () => true,
    () => false
  );
}