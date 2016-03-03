<template>
<div class="container" v-el="bg">
&nbsp;&nbsp;
<div class="page404">
    <p>①.点击识别二维码关注公众号</p>
    <!-- <img class="qcode" src="../assets/img/qcode.png"> -->
    <img class="qcode" src="../assets/img/qcode.png" height="156" width="156" alt="">
    <p>②.点击“工具栏”->“四六级”</p>
    <p>即可查成绩</p>
</div> 
<p class="copyright404">版权所有:网园资讯工作室</p>
    <canvas style="display:none;" v-el="experiment" width="{{canvas_width}}" height="{{canvas_height}}" id="canvas">你的瀏覽器版本太低，請及時更新</canvas>

</div> 
</template>
<style scoped>
    .container{
        width: 100%;
        position: absolute;
        top: 0;
    }
    .page404 {
        height: 350px;
        /*background: red;*/
        font-size: 20px;
        position:absolute;
        top:50%;
        margin-top: -175px;
/*        top:50%;
        left:50%;*/
/*        transform:translateY(-50%);
        -webkit-transform:translateY(-50%);
        -webkit-transform-origin:50% 50%;
        -webkit-transform:translate3d(-50%,-42%,0);*/
        opacity: 1;
        width: 100%;
        color: #fff;
        text-align: center;
    }
    .qcode{
        margin: 20px;
    }
    .copyright404{
        width: 100%;
        text-align: center;
        color: #fff;
        position: absolute;
        bottom: 30px;
    }
</style>
<script>
    export default{
        ready:function(){
            var canvas = this.$$.experiment;
            var cxt = canvas.getContext("2d");
            cxt.fillStyle="#34495e";
            cxt.beginPath();
            cxt.moveTo(0,0);
            cxt.lineTo(canvas.width*14/15,0);
            cxt.lineTo(0,canvas.height/3);
            // cxt.stroke();
            cxt.closePath();
            cxt.fill();
            cxt.fillStyle="#72c0ca";
            cxt.beginPath();
            cxt.moveTo(canvas.width,canvas.height*1.5/12);
            cxt.lineTo(0,canvas.height*5.7/12);
            cxt.lineTo(0,canvas.height*7/12);
            cxt.lineTo(canvas.width,canvas.height*10.5/12);
            cxt.closePath();
            cxt.fill();
            // cxt.fillStyle="#fff";
            // cxt.font = canvas.width/20+"px '黑体'"
            // cxt.fillText("①.点击识别二维码关注公众号",canvas.width/7,canvas.height*1.8/6)
            // cxt.fillText("②.点击“工具栏”->“四六级”",canvas.width/7,canvas.height*4.5/6)
            // cxt.fillText("即可查成绩",canvas.width/2.6,canvas.height*4.8/6)
            // cxt.fillText("版权所有:网园资讯工作室",canvas.width/5,canvas.height*5.5/6)
            


            this.$$.bg.style.backgroundImage = 'url("' + cxt.canvas.toDataURL() + '")';
        },
        computed: {
            canvas_width: function () {
              return window.innerWidth
            },
            canvas_height:function(){
                return window.innerHeight
            }
          },
    }
</script>