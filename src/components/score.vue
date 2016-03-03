<template>
    <canvas @click="text" id="score" v-el="score" style="width:{{canvas_width}}px;height:{{canvas_height}}" width="{{canvas_width*2}}" height="{{canvas_height*2}}"> 
        浏览器版本过低，不支持Canvas。
    </canvas>
</template>
<style scoped>
    #score{
        background: #fff;
    }
</style>
<script>
    export default{
        // props: ['score'],
        data(){
            return{
                error:false,
            }
        },
        methods:{
            text:function(){
            },
        },
        ready:function(){
            var self = this
            try{
                // var score = self.score
                var score = this.$parent.$data.score
                var l = score.Listening //听力
                var r = score.Reading //阅读
                var t = score.Total //总分
                var wr = score.Writing //写作
                var n = score.name //名字
                var s = score.school //学校
                var id = score.ticket //准考证
                var year = "20"+id.slice(6,8)+"年"
                if(id.slice(8,9) === "1"){
                    var mon = "6月"
                }else{
                    var mon = "12月"
                };
                if(id.slice(9,10) === "1"){
                    var cettype = "四"
                }else{
                    var cettype = "六"
                }
            }catch(e){
                console.log(e)
                // self.$route.router.go({path:"404"})
            }
            var scorecanvas = this.$$.score; 
            // scorecanvas.width = scorecanvas.width*2
            var w = scorecanvas.width // canvas宽
            var h = scorecanvas.height // canvas高
            var context = scorecanvas.getContext("2d");
            context.beginPath();
            context.fillStyle="#1b3e53"
            context.moveTo(0,h/20)
            context.lineTo(0,h*1.4/20);
            context.lineTo(w/2,h*1/10)
            context.lineTo(w,h*1.4/20)
            context.lineTo(w,h/20);
            context.fill();            
            context.beginPath();
            context.fillStyle="#34495e";
            context.moveTo(0,0);
            context.lineTo(0,h/20);
            context.lineTo(w/2,h*1.5/20);
            context.lineTo(w,h/20);
            context.lineTo(w,0);
            context.fill()
            context.font="36px '黑体'";
            context.fillStyle = "#fff"
            context.fillText("四六级成绩单",w/2-100,h/20);

            context.beginPath();
            context.fillStyle="#72c0ca"
            context.moveTo(0,h*1.4/20)
            context.lineTo(w/2,h*1/10)
            context.lineTo(w,h*1.4/20)
            context.lineTo(w,h*1/10)
            context.lineTo(w/2,h*2.6/20)
            context.lineTo(0,h*1/10)
            context.fill()
            //header end 

            context.beginPath();
            context.strokeStyle="#b9b9b9"
            context.lineWidth = "2"
            context.moveTo(w*4/15,h/5)
            context.lineTo(w/15,h/5)
            context.lineTo(w/15,h*19/20)
            context.lineTo(w*14/15,h*19/20)
            context.lineTo(w*14/15,h/5)
            context.lineTo(w*11/15,h/5)
            context.stroke()
            context.font=w/17+ "px '黑体'";
            context.fillStyle = "#8a8a8a"
            context.fillText("英语"+cettype+"级",w/2-w/9,h*1.05/5);
            context.beginPath();
            context.fillStyle="#4fbac3";
            context.arc(w*4/15,h/5,16,0,Math.PI*2,true); 
            context.arc(w*11/15,h/5,16,0,Math.PI*2,true); 
            context.fill();
            context.font="32px '黑体'";
            context.fillStyle="#b9b9b9";
            context.fillText("考生姓名：",w/6,h*5.5/20);
            context.fillText("所在学校:",w/6,h*6.5/20);
            context.fillText("考试时间:",w/6,h*7.5/20);
            context.fillText("准考证号:",w/6,h*8.5/20);
            //渲染信息
            context.fillText(n,w/6+200,h*5.5/20);
            context.fillText(s,w/6+200,h*6.5/20);
            context.fillText(year+mon,w/6+200,h*7.5/20);
            context.fillText(id,w/6+200,h*8.5/20);

            context.font= w/25+ "px '黑体'";
            // context.fillText("姓名中的生僻字可能无法正常显示，",w/6,h*18/20);
            context.fillText("最终成绩以成绩单为准。",w/4,h*18.7/20);

            context.beginPath();
            context.fillStyle="#1abc9c"
            context.arc(w*1.1/6,h*10/20,12,0,Math.PI*2,true);
            context.arc(w*1.1/6,h*12/20,12,0,Math.PI*2,true);
            context.arc(w*1.1/6,h*14/20,12,0,Math.PI*2,true);
            context.arc(w*1.1/6,h*16/20,12,0,Math.PI*2,true);
            context.fill(); 
            context.beginPath();
            context.fillStyle="#000"
            context.font="bold 38px '黑体'";
            context.fillText("总分",w*1.4/6,h*10.2/20);
            context.fillText("听力",w*1.4/6,h*12.2/20);
            context.fillText("阅读",w*1.4/6,h*14.2/20);
            context.fillText("写作",w*1.4/6,h*16.2/20);
            context.fillStyle="#ecf0f1";
            context.fillRect(w*1.4/6,h*10.6/20,w/1.8,25); 
            context.fillRect(w*1.4/6,h*12.6/20,w/1.8,25); 
            context.fillRect(w*1.4/6,h*14.6/20,w/1.8,25); 
            context.fillRect(w*1.4/6,h*16.6/20,w/1.8,25); 
            //渲染成绩
            context.beginPath();
            context.fillStyle="#000"
            context.fillText(t,w*1.4/6+w/1.8-70,h*10.2/20);
            context.fillText(l,w*1.4/6+w/1.8-70,h*12.2/20);
            context.fillText(r,w*1.4/6+w/1.8-70,h*14.2/20);
            context.fillText(wr,w*1.4/6+w/1.8-70,h*16.2/20);
            //渲染进度条
            context.beginPath();
            context.fillStyle="#1abc9c"
            context.fillRect(w*1.4/6,h*10.6/20,w/1.8*t/710,25); 
            context.fillRect(w*1.4/6,h*12.6/20,w/1.8*l/248.5,25); 
            context.fillRect(w*1.4/6,h*14.6/20,w/1.8*r/248.5,25); 
            context.fillRect(w*1.4/6,h*16.6/20,w/1.8*wr/213,25); 


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