"use client";

import { useRouter } from "next/navigation";
import axios from "axios";
import { toast } from "react-toastify";

export default function Logout() {
  const router = useRouter(); // Initialize the Next.js router for navigation

  // Handle the logout process
  const handleLogout = async () => {
    // Close the navigation drawer if open
    const inputNav = document.getElementById("my-drawer-3");
    if (inputNav) {
      (inputNav as HTMLInputElement).checked = false;
    }

    try {
      // Call the logout API to delete the token
      await axios.get("/api/auth/logout");

      // Clear the user data from the Redux store

      // Show a success toast message
      toast.success("Logged out successfully");

      // Redirect the user to the login page
      router.push("/auth/login");
    } catch (error: unknown) {
      // Handle errors during the logout process
      if (axios.isAxiosError(error) && error.response?.data?.error) {
        toast.error(error.response.data.error); // Show API error message
      } else {
        toast.error("Failed to logout"); // Show fallback error message
      }
    }
  };

  // Render the logout button
  return (
    <li onClick={handleLogout} className="btn btn-sm font-bold uppercase">
      Logout
    </li>
  );
}
