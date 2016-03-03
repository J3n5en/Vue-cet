module.exports = function(router){
      function is_weixin(){ var ua = navigator.userAgent.toLowerCase(); if(ua.match(/MicroMessenger/i)=="micromessenger") { return true; } else { return false; } }
    window.onload=function(){
        if(!is_weixin()){
          // alert("//入口不是微信")
            router.go({path:"404"});
        }
    },
	router.map({
		'*': {
            component: require('./components/haveTicket.vue')
        },
        '/': {
            component: require('./components/haveTicket.vue')
        },
        '/find': {
            component: function (resolve) {
              require(['./components/findTicket.vue'], resolve)
          }
            },
        '/404': {
            component: function (resolve) {
              require(['./components/404.vue'], resolve)
          }
            },            
        '/score': {
            component: function (resolve) {
              require(['./components/score.vue'], resolve)
            },            
        }
    })
//   router.afterEach(function (transition) {
//     var qq = self 
//     console.log(self.$data)
//   // console.log(this.$parent.$data.score)
// })
	
}