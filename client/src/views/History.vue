<template>
    <div class="history">
        <div class="login-title-1" @click="goHome">
			<b><i>Fuck JP Words</i></b>
		</div>
		<div class="login-title-2">
			<i></i>
		</div>
        <div class="filter-container">
            <div class="title">
                <p><b>{{ function_title }}</b></p>
            </div>
            <div class="filter">
                <div class="filter-item">
                    <p class="notice">分组</p>
                    <el-select class="input" v-model="exam_id" placeholder="-">
						<el-option v-for="(item, index) in exam_info" :key="index" :label="item.finish_datetime+' 分数:'+item.score" :value="item.test_id"></el-option>
					</el-select>
                </div>
                <div class="filter-item"></div>
            </div>
            <div class="commit">
                <div class="commit-btn"><el-button type="primary" size="mini" @click="getExamDetail" round>添加</el-button></div>
            </div>
        </div>
        <div class="info-container">
            <div class="info-list" v-for="(item, index) in exam_data" :key="index">
                <div class="label1">类型</div>
                <div class="text1" v-if="item.type == 1">汉译日</div>
                <div class="text1" v-if="item.type == 2">日译汉</div>
                <div class="label2">你的回答</div>
                <div class="text2" style="color: green;" v-if="item.type == 1 && item.answer == item.words_jp">{{item.answer}}</div>
                <div class="text2" style="color: red;" v-if="item.type == 1 && item.answer != item.words_jp">{{item.answer}}</div>
                <div class="text2" style="color: green;" v-if="item.type == 2 && item.answer == item.trans_cn">{{item.answer}}</div>
                <div class="text2" style="color: red;" v-if="item.type == 2 && item.answer != item.trans_cn">{{item.answer}}</div>
                <div class="label3">日语</div>
                <div class="text3" style="color: #108EE9;" v-if="item.type == 1">{{item.words_jp}}</div>
                <div class="text3" v-if="item.type != 1">{{item.words_jp}}</div>
                <div class="label4">汉语</div>
                <div class="text4" style="color: #108EE9;" v-if="item.type == 2">{{item.trans_cn}}</div>
                <div class="text4" v-if="item.type != 2">{{item.trans_cn}}</div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            function_title: '考试历史',
            exam_id: '',
            exam_info: [],
            exam_data: []
        }
    },
    methods: {
        getExamInfo: function() {
            this.$axios
                .get('/api/exam_result')
                .then(res => {
                    this.exam_info = res.data;
                })
                .catch(err => {
                    console.log(err);
                });
        },
        getExamDetail: function() {
            this.$axios
                .get('/api/exam_detail?test_id='+this.exam_id)
                .then(res => {
                    this.exam_data = res.data;
                })
                .catch(err => {
                    console.log(err);
                });
        },
        goHome: function() {
            this.$router.push({
				path: "/",
			});            
        }
    },
    mounted() {
        this.getExamInfo();
    }
}
</script>
<style>
    .history {
        height: 100%;
        background-image: linear-gradient(to bottom , #108EE9, #FFFFFF);
	}
    .history .login-title-1 {
		position: absolute;
		width: fit-content;
		top: 5px;
		left: 5px;
		color: white;
		font-size: 20px;
	}
	.history .login-title-2 {
		position: absolute;
		width: fit-content;
		top: 5px;
		right: 5px;
		color: white;
		font-size: 20px;
	}
    .history .filter-container {
		position: absolute;   
		top: 18%;   
		left: 50%;   
		-webkit-transform: translate(-50%, -50%);   
		-moz-transform: translate(-50%, -50%);   
		-ms-transform: translate(-50%, -50%);   
		-o-transform: translate(-50%, -50%);   
		transform: translate(-50%, -50%);
		width: 90%;
        height: 23%;
		padding: 32px 20px 35px 20px;
		border-radius: 25px;
		margin: 0px auto;
		background: #fff;
		background-clip: padding-box;
	}
    .history .filter-container .title {
        position: absolute;
		width: fit-content;
		top: 7px;
		left: 20px;
		color: black;
		font-size: 15px;
    }
    .history .filter-container .filter {
        width: 100%;
        display: flex;
        flex-wrap: wrap;
    }
    
    .history .filter-container .filter .filter-item{
        width: 100%;
        display: flex;
        flex-wrap: wrap;
        margin: 0 0 5px 0;
    }
    .history .filter-container .filter .filter-item .notice{
        width: 20%;
		color: black;
		font-size: 12px;
        display: flex;
		justify-content: right;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .history .filter-container .filter .filter-item .input{
        width: 80%;
        height: 60%;
    }
    .history .filter-container .commit .commit-btn{
        position: absolute;
		width: fit-content;
		bottom: 5px;
		right: 20px;
    }
    .history .info-container {
		position: absolute; 
		display: flex;
        flex-wrap: wrap;  
		top: 65%;   
		left: 50%;   
		-webkit-transform: translate(-50%, -50%);   
		-moz-transform: translate(-50%, -50%);   
		-ms-transform: translate(-50%, -50%);   
		-o-transform: translate(-50%, -50%);   
		transform: translate(-50%, -50%);
		width: 90%;
        height: 63%;
		padding: 10px 5px 10px 5px;
		border-radius: 25px;
		margin: 0px auto;
		background: #fff;
		background-clip: padding-box;
	}
    .history .info-container .info-list {
        width: 100%;
        height: 20%;
		display: flex;
        flex-wrap: wrap;
        border-bottom:1px dashed grey;
        margin: 0 5px 0 5px;
    }
    .history .info-container .info-list .label1 {
        width: 10%;
        height: 50%;
        color: grey;
		font-size: 12px;
        display: flex;
		justify-content: right;
		align-items:center; /*实现垂直居中*/
    }
    .history .info-container .info-list .text1 {
        width: 30%;
        height: 50%;
        color: black;
		font-size: 12px;
        display: flex;
		justify-content: center;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .history .info-container .info-list .label2 {
        width: 20%;
        height: 50%;
        color: grey;
		font-size: 12px;
        display: flex;
		justify-content: right;
		align-items:center; /*实现垂直居中*/
    }
    .history .info-container .info-list .text2 {
        width: 40%;
        height: 50%;
        color: black;
		font-size: 12px;
        display: flex;
		justify-content: center;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .history .info-container .info-list .label3 {
        width: 10%;
        height: 50%;
        color: grey;
		font-size: 12px;
        display: flex;
		justify-content: right;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .history .info-container .info-list .text3 {
        width: 40%;
        height: 50%;
        color: black;
		font-size: 12px;
        display: flex;
		justify-content: center;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .history .info-container .info-list .label4 {
        width: 10%;
        height: 50%;
        color: grey;
		font-size: 12px;
        display: flex;
		justify-content: right;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .history .info-container .info-list .text4 {
        width: 40%;
        height: 50%;
        color: black;
		font-size: 12px;
        display: flex;
		justify-content: center;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
</style>