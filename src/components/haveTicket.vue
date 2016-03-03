<template>
    <div class="container" v-el="bg">
        &nbsp;
        <h1 class="logo">
            CET
            <span>四六级成绩查询</span>
        </h1>
        <a v-link="'/find'" class="change" >
            <p>无准考证查询</p>
            <em><i></i></em>
        </a>
        <form class='getscore'>
            <input type="text" class="ticket" placeholder="请输入准考证号" v-model="ticket">
            <input type="text" class="name" placeholder="请输入姓名" v-model="name">
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
        .footer {
            height: 20%;
            position: relative;
        }
        .copyright{
            position: absolute;
            bottom: 0;
            width: 100%;
            /*width: 320px!important;*/
            /*margin-top: 100px;*/
        }
    </style>
    <style>
        .error{
            width: 235px;
            height: 185px;
            background: #fff;
            position:absolute;
            top:50%;left:50%;
            -webkit-transform-origin:50% 50%;
            -webkit-transform:translate3d(-50%,-50%,0);
            opacity: 1;
            border-radius: 5px;
        }
        #error { 
            width: 50px;
            margin-left: 92.5px;
            height: 50px;
            margin-top: 20px;
        }
        .error p {
            color: #a3a3a3;
            text-align: center;
            font-size: 16px;
        }
        .err-btn {
            width: 105px;
            height: 40px;
            background: #1abc9c;
            margin: 0 auto;
            text-align: center;
            line-height: 40px;
            border-radius: 5px;
            color: #fff;
        }
        .footer {
            margin: 30px;
        }
        .notice,.copyright{
            text-align: center;
            width: 320px;
            color: #fff;
            margin: 0 auto;
            margin-top: 10px;
            line-height: 30px;
        }
/*        .copyright{
            margin-top: 30px;
        }*/
        .submit{
            background: #1abc9c;
            color: #fff;
            font-size: 16px;
        }
        .getscore{
            width: 295px;
            margin: 0 auto;
            /*background: black;*/
        }
        .getscore input ,.submit{
            border: 0;
            width: 100%;
            height: 35px;
            margin-top: 20px;
            border-radius: 5px;
            outline: 0;
            padding-left: 5px;
            box-sizing:border-box;
        }
        .getscore input:focus{
            /*outline: 2px solid #1abc9c;*/
            box-shadow: 0 0 0 2px #1abc9c;
            /*outline-radius: 5px;*/
            /*height: 40px;*/
        }
        .change{
            display: block;
            width: 140px;
            height: 40px;
            float: right;
            clear: both;
            margin-right: 30px;
        }
        .change p{
            display: inline-block;
            margin: 0;
            line-height: 40px;
            float: left;
            font-size: 15px;
            color: #fff;
            font-weight: 700;
        }
        .change em {
            position: relative;
            display: inline-block;
            width: 40px;
            height: 40px;
            border-radius: 20px;
            background: #1abc9c;
            float: right;
        }
        .change i {
            display: inline-block;
            width: 13px;
            height: 13px;
            border:3px solid #fff;
            border-width: 3px 3px 0 0 ;
            transform:rotate(45deg);
            position: absolute;
            top: 13px;
            left: 9px;
        }
        .logo{
            color: #fff;
            text-align: center;
            font-size: 72px;
            margin: 20px!important;

        }
        .logo span{
            display: block;
            font-size: 16px;
        }
        .container{
            height: 100%;
            background-color: #1b3e53;
        }
        .submit{
            clear: both;
            line-height: 35px;
            text-align: center;
        }
    </style>
    <script>
        export default{
        props: ['score'],
        data(){
            return{
                error:false,
                ticket:"",
                name:"",
                submitBtn:"提 交",
                
            }
        },
        ready:function(){
            var self = this
            this.$http.post("http://wechat.zeffee.com/check46/",{ //发送请求
                action:"verify"
            })
            .then(function (resp){ //请求成功返回
                        // alert(resp.data)
                if(resp.data === "fail"){
                    // alert("//非法请求")
                    self.$route.router.go({path:"404"});
                }
                },function(){ //请求失败跳转404
                    // alert("//网络不通，请求失败")
                    self.$route.router.go({path:"404"})
                })
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
            //error logo
            this.$$.bg.style.backgroundImage = 'url("' + cxt.canvas.toDataURL() + '")';
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
                        id_num:self.ticket,
                        name:self.name,
                        score:"id_card"
                    })
                    .then(function (resp){ //请求成功返回
                        if(resp.data === "fail"){
                            // alert("//非法请求")
                            self.$route.router.go({path:"404"})
                        }
                        else if(resp.data.Status === "1"){
                            self.score = resp.data
                            // this.$dispatch('child-msg',"add",self.score);
                            self.$parent.$data.score = self.score
                            self.$route.router.go({path:"score"});
                            self.submitBtn = "提 交";
                            }else{
                                self.error = true;
                                // window.location.href="http://www.chsi.com.cn/cet/"; 
                                self.submitBtn = "提 交";
                            }
                        },function(){ //请求失败跳转404
                            // alert("//网络不通")
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