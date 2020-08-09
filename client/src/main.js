import Vue from "vue";
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
import "font-awesome/css/font-awesome.min.css";
// only import the icons you use to reduce bundle size
import "vue-awesome/icons/angle-left";
import "vue-awesome/icons/bars";
import "vue-awesome/icons/dashboard";
import "vue-awesome/icons/github";
import "vue-awesome/icons/bar-chart";
import "vue-awesome/icons/upload";
import "vue-awesome/icons/file-text-o";
import Icon from "vue-awesome/components/Icon";
import App from "./App.vue";
import router from "@/router/index";
import "@/router/guards";
import locale from "element-ui/lib/locale/lang/ja";
import Sortable from "sortablejs";
import draggable from "vuedraggable";
import Axios from "axios";
import qs from "qs";
import echarts from "echarts";
import Meta from 'vue-meta'
// import echarts from "./plugins/echarts";
import './plugins/ant-design-vue.js';
import './plugins/xml2json.js';
// import VueI18n from 'vue-i18n';
import i18n from './i18n'
let axios = Axios.create({
    // baseURL: "http://localhost:8000/"
});
//挂载到原型上
Vue.prototype.$axios = axios;
Vue.prototype.$echarts = echarts;
Vue.prototype.i18n = i18n;
Vue.config.productionTip = false;
Vue.use(Meta)
Vue.use(ElementUI, {
  locale
});
Vue.use(ElementUI, {
  size: "small"
});
Vue.component("icon", Icon);
// property defined in data is reactive
// convert to normal object
Vue.prototype.clone = function (src) {
  return JSON.parse(JSON.stringify(src));
};

Vue.prototype.ok = function (message, duration) {
  return this.$message({
    type: "success",
    message: message || "Success.",
    showClose: true,
    duration: duration || 2000
  });
};
Vue.prototype.info = function (message, duration) {
  return this.$message({
    type: "info",
    message: message || "",
    showClose: true,
    duration: duration || 2000
  });
};
Vue.prototype.warn = function (message, duration) {
  return this.$message({
    type: "warning",
    message: message || "Success",
    showClose: true,
    duration: duration || 2000
  });
};

Vue.prototype.error = function (message, duration) {
  if (message.length > 200) {
    console.log(message);
    message = message.slice(0, 200) + "...";
  }
  return this.$message({
    type: "error",
    message,
    showClose: true,
    duration: duration || 5000
  });
};

// 登陆查询
Vue.prototype.LoginStatus = function(){
	this.$axios({
		url:'api/login_status',
		method:'get'
	}).then(res=>{
		if (res.data === '0'){
			this.$router.push({
				path:'/login'
			})

		}else{
			this.$User = res.data
		}
	}).catch(err=>{
		this.$message({
			type:'error',
			message:'Login status check failed.'
		})
	})
}

Vue.component("draggable", draggable);
Vue.component("Sortable", Sortable);

new Vue({
  router,
  render: h => h(App),
  i18n,
}).$mount("#app");

