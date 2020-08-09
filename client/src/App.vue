<template>
    <div id="app">
        <router-view/>
    </div>
</template>
<script>
export default {
  created(){
    document.title = 'Fuck JP Words' 
  }
};
</script>




<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
html {
  height: 100%;
  overflow-x: hidden; 
  overflow-y: auto; 
  position:relative;
  font-weight:700;
  // margin-left:15%;
}
// ::-webkit-scrollbar {
//     width: 0px;
//     height: 1px;
// }
// ::-webkit-scrollbar-thumb {
//     border-radius: 5px;
//     -webkit-box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
//     background: rgba(0, 0, 0, 0.2);
// } 
// ::-webkit-scrollbar {
// display: none;
// }
html body {
  height: 100%;
}

body {
}

* {
  text-align: left;
  margin: 0;
  padding: 0;
}
#app {
  height: 100%;
  width: 100%;
}
.el-card__body {
  padding: 0;
}
.clear {
  clear: both;
}
.el-button--danger {
  background-color: #666;
  border-color: #666;
}
.el-button--success {
  background-color: #7f7f7f;
  border-color: #7f7f7f;
}
.el-button--primary {
  background-color: #ffa500;
  border-color: #ffa500;
}
.el-button--danger:hover {
  background-color: #888;
  border-color: #888;
}
.el-button--success:hover {
  background-color: #8f8f8f;
  border-color: #8f8f8f;
}
.el-button--primary:hover {
  background-color: #999;
  border-color: #999;
}
.el-tag {
  background-color: #666;
  color: #fff;
}
.el-tag i.el-tag__close {
  color: #fff;
}
.el-tag i.el-tag__close:hover {
  color: #000;
  background: #efefef;
}
</style>
