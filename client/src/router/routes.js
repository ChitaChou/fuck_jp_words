import Menu from "@/views/Menu"
import Words from "@/views/Words"
import Groups from "@/views/Groups"

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
  },
  {
    path: "/groups",
    name: "Groups",
    hidden: true,
    component: Groups
  }
];