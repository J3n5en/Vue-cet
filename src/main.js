var Vue = require('vue')
var VueRouter = require('vue-router')
// var VueAsyncData = require('vue-async-data')
var VueResource = require('vue-resource')
var App = require('./app.vue')
var routerMap = require('./router')

// Vue.broadcast('child-msg')
Vue.use(VueResource);
Vue.use(VueRouter);
// Vue.use(VueAsyncData);
var vueEl = require('vue-el')
Vue.use(vueEl)
// filter
// var filter = require('./filter');

// Object.keys(filter).forEach(function(k) {
//   Vue.filter(k, filter[k]);
// });

//directive
// var directive = require('./directive')

// Object.keys(directive).forEach(function(k) {
//   Vue.directive(k, directive[k]);
// });

var router = new VueRouter()

routerMap(router)
// router.options.canReuse  = false
router.start(App, 'app')
Vue.http.options.emulateJSON = true
