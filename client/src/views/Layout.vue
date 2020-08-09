<template>
  <router-view></router-view>
</template>

<script>
import "../assets/css/header.css";
import qs from "qs";
import axios from 'axios'
export default {
  name: "layout",
  components: {
    sideBar
  },
  methods: {
    GoBack() {
      this.$router.push({
        path: "/login"
      });
    },
    handleCommand(command) {
      if (command === "logout") {
        this.$confirm("Logout?", "Confirm", {
          confirmButtonText: "Yes",
          cancelButtonText: "No",
          type: "warning"
        }).then(
          () => {
            localStorage.setItem("USER_ID", "");
            let auth_data = "current_username=" + sessionStorage.getItem("current_username");
            sessionStorage.removeItem("current_username");
            axios.post('api/user_logout', auth_data)
              .then(res=>{
                if (res.data == "logout_success") {
                  this.$message({
                    type: 'success',
                    message: 'Logout Success.'
                  })
                  this.GoBack();
                }
                else{
                  this.$message({
                    type: 'error',
                    message: 'Logout Failed.'
                  })
                }
              })
              .catch(err => {
                console.log(err);
                this.$message({
                  type: 'error',
                  message: 'Error occured.'
                })
            });
          },
          () => {
            //Cancel
          }
        );
      }
    }
  },
  data() {
    return {
      isCollapse: false,
      currentUserName: "",
      activeIndex:"1"
    };
  },
  computed: {
    currentUser() {
      let username = localStorage.getItem("USER_ID");
      return username;
    }
  }
};
</script>

<style scoped lang="css">
.home_container {
  height: 100%;
  position: absolute;
  top: 0px;
  left: 0px;
  width: 100%;
}

.el-header {
  background-color: #20a0ff;
  color: #333;
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: white;
}

.el-aside {
  background-color: #ececec;
}

.el-main {
  background-color: #fff;
  color: #000;
  text-align: center;
}

.home_title {
  color: #fff;
  font-size: 22px;
  display: inline;
}

.home_userinfo {
  color: black;
  cursor: pointer;
}
.tool-dropdown-link,
.tool-dropdown-sub-link {
  font-family: "Open Sans", sans-serif;
  color: #333333;
  cursor: pointer;
}
.tool-dropdown-sub-link {
  text-decoration: none;
}
/*下拉菜单样式文字颜色及过渡动画，需单独设定*/
.tool-dropdown-link {
  transition: all 300ms linear;
}
.tool-dropdown-link:hover {
  color: #ffa500;
}

.nav > li:after {
  content: "";
  display: block;
  position: absolute;
  width: 100%;
  height: 0;
  top: 0;
  z-index: 0;
  background: blue;
}
.el-menu-item{
  padding: 0 27px;
  font-size: 16px;
}
.el-menu {
  margin-top:16px;
}

.submenuStyle {
   font-size: 16px;
}
.submenuStyle {
   font-size: 16px;
}
.submenutitle {
   font-size: 14px;
}
</style>