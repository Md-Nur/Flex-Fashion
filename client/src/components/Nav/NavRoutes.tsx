"use client";
import NavDropdown from "./NavDropdown";
import NavLink from "./NavLink";
import Logout from "./Logout";

const NavRoutes = () => {
  const user = {
    id: false, // Mock user data, replace with actual user context or state
    isAdmin: true, // Mock admin status, replace with actual user context or state
  };
  return (
    <>
      {/* {user?.isAdmin && <NavLink name="Admin" route="/admin" />} */}
      {user?.id ? (
        <>
          <NavLink name="Home" route="/" />
          <NavDropdown
            name="Add Question"
            routes={[
              { name: "MCQ", url: "/add/mcq" },
              { name: "Short Question", url: "/add/short" },
              { name: "Creative Question", url: "/add/cq" },
            ]}
          />
          <NavDropdown
            name="Show Question"
            routes={[
              { name: "MCQ", url: "/show/mcq" },
              { name: "Short Question", url: "/show/short" },
              { name: "Creative Question", url: "/show/cq" },
            ]}
          />
          {/* <NavLink name="leaderboard" route="/leaderboard" /> */}
          <Logout />
        </>
      ) : (
        <>
          <NavLink name="home" route="/" />
          <NavLink name="login" route="/auth/login" />
          <NavLink name="signup" route="/auth/signup/1" />
        </>
      )}
    </>
  );
};

export default NavRoutes;
