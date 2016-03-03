<template>
    <div class="container" v-el="bg">
        &nbsp;
        <h1 class="logo">
            CET
            <span>四六级成绩查询</span>
        </h1>
        <a v-link="'/'" class="change">
            <p>快速查询</p>
            <em><i></i></em>
        </a>
        <form class='getscore'>
            <input type="text" class="name" placeholder="请输入姓名" v-model="name">
            <input type="text" class="name" placeholder="请输入省份" v-model="province">
            <input type="text" class="name" placeholder="请输入学校" v-model="school">
            <div class="cet-type">
                <label name="type" for="cet4">
                    <input style="opacity:0;position:absolute;" type="radio" checked id="cet4" name="type" value="1" v-model="cettype">
                    <canvas 
                    style="display:inline-block;" 
                    v-el="on" width="25" height="25"
                    v-show="cettype==1">on</canvas>
                    <canvas
                    style="display:inline-block;" 
                    v-el="off" width="25" height="25"
                    v-show="cettype==2">off</canvas>

                    <span>四级</span>
                </label>
                <label name="type" for="cet6">
                    <input type="radio" style="opacity:0;position:absolute;" id="cet6" name="type" value="2" v-model="cettype">
                    <canvas 
                    style="display:inline-block;" 
                    v-el="on1" width="25" height="25"
                    v-show="cettype==2">on</canvas>
                    <canvas
                    style="display:inline-block;" 
                    v-el="off1" width="25" height="25"
                    v-show="cettype==1">off</canvas>
                    <span>六级</span>
                    <!-- <i class="{{ cettype==1?'cet6':'cet4' }}">qqq</i> -->
                </label>
            </div>
            <div @click="submit" class="submit">{{ submitBtn }}</div>
        </form>
        <div class="footer">
            <p class="notice">
                   注意：1.最终成绩请以成绩单为准。<br>
                         2. 名字中包含生僻字可能无法查询。 <br>
                    3. 2015年12月成绩在2月26号9点之后公布。</p>
                <p class="copyright">版权所有:网园资讯工作室</p>
            </div>
            <canvas style="display:none;" v-el="experiment" width="{{canvas_width}}" height="{{canvas_height}}" id="canvas">你的瀏覽器版本太低，請及時更新</canvas>
            <!-- <canvas style="display:none;" v-el="on" width="25" height="25">CET4</canvas> -->
            <!-- <canvas style="display:none;" v-el="off" width="25" height="25">CET4</canvas> -->
            <div class="error" v-show="error">
                <canvas id="error" v-el="errorlogo" width="50" height="50"> 
                    错误！
                </canvas>
                <p>查询失败，没有找到你的成绩。</p>
                <div @click="closeErr" class="err-btn">
                    确&nbsp;&nbsp;定
                </div>
            </div>
        </div>    
    </template>
    <style scoped>
        label span {
            height: 35px;
            display: inline-block;
            position: relative;
            top: -6px;
            left: 5px;
        }
        .footer{
            clear: both;
            position: relative;
            top: 20px
        }
        .submit{
            float: left;
            clear: both;
        }
        .change{
            width: 108px;
            float: left;
            margin-left: 30px;
        }
        .change p{
            float: right;
        }
        .change em {
            float: left;
        }
        .change i {
            transform:rotate(-135deg);
            top: 13px;
            left: 15px;
        }
        .cet-type input {
            /*float: left;*/
            width: 35px;
            border: 0;
            margin-top: 0;
        }
        .cet-type label{
            display: inline-block;
            line-height: 35px;
            height: 35px;
            color: #fff;
            float: left;
            margin-top: 20px;
            margin-left: 20px;
        }
        .cet-type input:focus {
            box-shadow: none!important;
        }
        .cet-type label[for='cet6'] {
            float: right;
            margin-left: 0;
            margin-right: 25px;
        }
    </style>
    <script>
        export default{
            data(){
                return{
                    error:false,
                    submitBtn:"提 交",
                    name:"",
                    province:"广东",
                    school:"韶关学院",
                    cettype:1,
                    score:""
                }
            },
        init:function(){
            var self = this
            self.score = this.$parent.$data.score
        },
            ready:function(){
            var self = this
            this.$http.post("http://wechat.zeffee.com/check46/",{ //发送请求
                action:"verify"
            })
            .then(function (resp){ //请求成功返回
                        // alert(resp.data)
                if(resp.data === "fail"){
                    // alert("非法请求")
                    self.$route.router.go({path:"404"});
                }
                },function(){ //请求失败跳转404
                    // alert("网络不通")
                    self.$route.router.go({path:"404"})
                })
            //hack radio
            //on
            var on_canvas = this.$$.on;
            var oncxt = on_canvas.getContext("2d");
            oncxt.beginPath();
            oncxt.arc(12.5,12.5,10,0,360,false);
            oncxt.lineWidth=5;
            oncxt.strokeStyle="#1abc9c";
            oncxt.stroke();
            oncxt.beginPath();
            oncxt.fillStyle="#1abc9c"
            oncxt.arc(12.5,12.5,4,0,360,false);
            oncxt.fill()
            //off 
            var off_canvas = this.$$.off;
            var offcxt = off_canvas.getContext("2d");
            offcxt.beginPath();
            offcxt.arc(12.5,12.5,10,0,360,false);
            offcxt.lineWidth=5;
            offcxt.strokeStyle="#d7dbde";
            offcxt.stroke();
            //on
            var on1_canvas = this.$$.on1;
            var on1cxt = on1_canvas.getContext("2d");
            on1cxt.beginPath();
            on1cxt.arc(12.5,12.5,10,0,360,false);
            on1cxt.lineWidth=5;
            on1cxt.strokeStyle="#1abc9c";
            on1cxt.stroke();
            on1cxt.beginPath();
            on1cxt.fillStyle="#1abc9c"
            on1cxt.arc(12.5,12.5,4,0,360,false);
            on1cxt.fill()
            //off 
            var off1_canvas = this.$$.off1;
            var off1cxt = off1_canvas.getContext("2d");
            off1cxt.beginPath();
            off1cxt.arc(12.5,12.5,10,0,360,false);
            off1cxt.lineWidth=5;
            off1cxt.strokeStyle="#d7dbde";
            off1cxt.stroke();
            //
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
            this.$$.bg.style.backgroundImage = 'url("' + cxt.canvas.toDataURL() + '")';
            //error logo
            var errorcanvas = this.$$.errorlogo;
            var context = errorcanvas.getContext("2d");
            context.beginPath();
            context.lineWidth = 4; 
            context.strokeStyle = "#fd785d"
            context.arc(25,25,20,Math.PI*0.7,Math.PI*0.6,false);
            context.stroke();
            context.beginPath();
            context.moveTo(15,15);
            context.lineTo(35,35);
            context.stroke();
            context.beginPath();
            context.moveTo(35,15);
            context.lineTo(15,35);
            context.stroke();
        },
        methods:{
            closeErr:function(){
                this.error = false;
            },
            submit:function(){
                var self = this
                self.$parent.$data.score = ""
                if(self.submitBtn === "提 交"){
                    self.submitBtn = "提 交 中...";
                    this.$http.post("http://wechat.zeffee.com/check46/",{ //发送请求
                        province:self.province.replace(/省/, ""),
                        username:self.name,
                        school:self.school,
                        cet_type:self.cettype,
                        score:"no_card"
                    })
                    .then(function (resp){ //请求成功返回
                        if(resp.data === "fail"){
                            // alert("非法请求")
                            self.$route.router.go({path:"404"})
                        }
                        else if(resp.data.Status === "1"){
                            // var self = this
                            self.score = resp.data
                            self.$parent.$data.score = self.score
                            self.$route.router.go({path:"score"});
                            self.submitBtn = "提 交";
                        }else{
                            self.error = true;
                            // window.location.href="http://www.chsi.com.cn/cet/"; 
                            self.submitBtn = "提 交";
                        }
                        },function(){ //请求失败跳转404
                            // alert("网络不通")
                            self.$route.router.go({path:"404"})
                            self.submitBtn = "提 交";
                        })
                }
            }
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