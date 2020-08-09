import Menu from "@/views/Menu"
import Words from "@/views/Words"

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
  },
  {
    path: "/words",
    name: "Words",
    hidden: true,
    component: Words
  }
];