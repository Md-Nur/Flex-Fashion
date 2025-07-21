"use client";
import { FaSun, FaMoon } from "react-icons/fa";
import { useEffect, useState } from "react";

export function ThemeToggle() {
  const [theme, setTheme] = useState<string>("light");
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  if (!mounted) {
    return (
      <button className="hover:bg-transparent">
        <div className="h-10 w-10" />
      </button>
    );
  }

  return (
    <button
      onClick={() => setTheme(theme === "light" ? "dark" : "light")}
      className="group hover:!bg-transparent cursor-pointer transition-all duration-300 ease-in-out"
      data-tooltip-id="theme-toggle"
      aria-label="Toggle theme"
    >
      {theme === "light" ? (
        <FaSun className="h-10 w-10 text-warning group-hover:bg-transparent" />
      ) : (
        <FaMoon className="h-10 w-10 text-primary group-hover:bg-transparent" />
      )}
    </button>
  );
}
