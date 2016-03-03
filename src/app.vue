<template>
   <!-- <router-view></router-view> -->
   <router-view class="view" transition="test" transition-mode="out-in"></router-view>
</template>

<style>
html,body{
    font-family: "微软雅黑";
    margin: 0;
    height: 100%;
    background: #1b3e53;
}
.view {
    background-color: #1b3e53;
  transition: all .5s ease;
}
.test-enter, .test-leave {
  opacity: 0;
  transform: translate3d(20px, 0, 0);
}
a:hover{
  -webkit-tap-highlight-color:rgba(0,0,0,0);
}
[v-cloak] {
  display: none;
}
</style>