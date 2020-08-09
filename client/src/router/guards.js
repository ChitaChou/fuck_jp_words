import router from "@/router";

// debugger;
// const whiteList = ["/login"];
// router.beforeEach((to, from, next) => {
// // if user logged in
// let token = localStorage.getItem("USER_ID");
// if (token) {
//  // if it's protected route, check license permission
//  if (to.path.startsWith("/protected")) {
//    let permission = to.meta.permission || 1;
//    let ok = permission & 1;
//    //console.log("ok=", ok);
//    ok ? next() : next("/login");
//  } else {
//    // non protected route
//    next();
//  }
// } else {
//  // if not logged in.
//  if (whiteList.indexOf(to.path) !== -1) {
//    next();
//  } else {
//    next("/login");
//  }
// }
// });

// router.afterEach(() => {});