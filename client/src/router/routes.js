
import Menu from "@/views/Menu"

export const pagesRoutes = [
  
];

export default [
  {
    path: "/",
    redirect: "/home"
  },
  {
    path: "/home",
    name: "Home",
    hidden: true,
    component: Menu
  }
];