"use client";
import Link from "next/link";
import { ReactNode } from "react";
import NavRoutes from "./NavRoutes";
import { IoMdMenu } from "react-icons/io";

// import { ThemeToggle } from "./ThemeToggle";

export default function Navbar({ children }: { children?: ReactNode }) {
  const user = { id: "123", name: "John Doe" }; // Mock user data, replace with actual user context or state

  return (
    <div className="drawer">
      <input id="my-drawer-3" type="checkbox" className="drawer-toggle" />
      <div className="drawer-content flex flex-col">
        {/* Navbar */}
        <div
          className={`w-full z-50 sticky top-0 bg-base-100/95 transition-all`}
        >
          <div className="navbar w-full max-w-6xl mx-auto">
            <div className="flex-none lg:hidden">
              <label
                htmlFor="my-drawer-3"
                aria-label="open sidebar"
                className="btn btn-square btn-ghost"
              >
                <IoMdMenu className="w-7 h-7" />
              </label>
            </div>
            <div className="mx-2 flex-1 px-2">
              <Link
                href={user?.id ? "/dashboard" : "/"}
                className="text-lg font-bold"
              >
                <span className="inline-block">Flex Fashion</span>
              </Link>
            </div>
            <div className="hidden flex-none lg:block">
              <ul className="menu menu-horizontal">
                <NavRoutes />
              </ul>
            </div>
            {/* <ThemeToggle /> */}
          </div>
        </div>
        {children}
      </div>
      <div className="drawer-side z-20">
        <label
          htmlFor="my-drawer-3"
          aria-label="close sidebar"
          className="drawer-overlay"
        ></label>
        <ul className="menu bg-base-200 min-h-full w-80 p-4">
          <NavRoutes />
        </ul>
      </div>
    </div>
  );
}
