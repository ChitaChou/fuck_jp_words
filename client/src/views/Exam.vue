<template>
    <div class="exam">
        <div class="login-title-1" @click="goHome">
			<b><i>正在考试中</i></b>
		</div>
		<div class="login-title-2" @click="commitExam">
			<i>交卷</i>
		</div>
        <div class="info-container">
            <div class="info-list" v-for="(item, index) in exam_data" :key="index">
                <div class="label1">题号</div>
                <div class="text1">{{index+1}}</div>
                <div class="label2">类型</div>
                <div class="text2" v-if="exam_type == 1">汉译日</div>
                <div class="text2" v-if="exam_type == 2">日译汉</div>
                <div class="label3">题目</div>
                <div class="text3" v-if="exam_type == 1">{{item.trans_cn}}</div>
                <div class="text3" v-if="exam_type == 2">{{item.words_jp}}</div>
                <div class="label4">作答</div>
                <div class="text4">
                    <el-input type="text" class="input" v-model="answer[index]" auto-complete="off"></el-input>
                </div>
            </div>
        </div>
        <el-dialog title="选择考试类型" :visible.sync="dialogVisible" width="80%" :before-close="goHome">
            <span>选择词汇分组和考试类型</span>
            <el-select class="input" v-model="group_id" placeholder="-">
                <el-option v-for="(item, index) in group_info" :key="index" :label="item.group_name" :value="item.group_id"></el-option>
            </el-select>
            <span slot="footer" class="dialog-footer">
            <el-button @click="getExamInfo(1)">汉译日</el-button>
            <el-button @click="getExamInfo(2)">日译汉</el-button>
        </span>
        </el-dialog>
    </div>
</template>
<script>
export default {
    data() {
        return {
            function_title: '单词管理',
            dialogVisible: false,
            group_id: '',
            exam_type: '',
            group_info: [],
            exam_id: '',
            exam_data: [],
            answer: []
        }
    },
    methods: {
        getGroupInfo: function() {
            this.$axios
                .get('/api/group')
                .then(res => {
                    this.group_info = res.data;
                    this.dialogVisible = true;
                })
                .catch(err => {
                    console.log(err);
                });
        },
        getExamInfo: function(type) {
            if ((type == 1 || type == 2) && this.group_id != '') {
                this.exam_type = type;
                this.$axios
                    .get('/api/exam?words_group='+this.group_id+'&type='+this.exam_type)
                    .then(res => {
                        if (res.data == 'parameter_error'){
                            this.$message.error('请检查参数');
                        }
                        else if (res.data == 'exam_type_error'){
                            this.$message.error('考试类型选择错误');
                        }
                        else if (res.data == 'group_has_no_words'){
                            this.$message.error('当前分组下没有词汇');
                        }
                        else if (res.data == 'words_group_error'){
                            this.$message.error('词汇分组不存在');
                        }
                        else {
                            this.exam_id = res.data.exam_id;
                            this.exam_data = res.data.exam_words;
                            this.dialogVisible = false;
                            this.$message({
                                type: 'success',
                                message: '考试开始!'
                            });
                        }
                    })
                    .catch(err => {
                        console.log(err);
                    });
            }
            else{
                this.$message.error('请检查参数');
            }
        },
        commitExam: function() {
            this.$confirm('要交卷吗？', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning',
            }).then(() => {
                var answer_data = [];
                for (var i = 0; i< this.answer.length; i++){
                    // 封装答案数据
                    var temp = {
                        "test_id": this.exam_id,
                        "words_id": this.exam_data[i].words_id,
                        "answer": this.answer[i]
                    }
                    answer_data[i] = temp;
                }
                // 提交答案数据
                this.$axios
                    .post('/api/exam', answer_data)
                    .then(res => {
                        if(res.data == 'ans_success'){
                            // 提交成功，获取分数
                            var points_data = {
                                "test_id": this.exam_id,
                                "type": this.exam_type
                            }
                            this.$axios
                            .post('/api/exam_result', points_data)
                            .then(res => {
                                if ('score' in res.data){
                                    this.$message({
                                        type: 'success',
                                        message: '交卷成功!本次分数为'+res.data.score
                                    });
                                    this.goHome();
                                }
                                else{
                                    alert('考试提交失败，请重试');
                                }
                            })
                            .catch(err => {
                                console.log(err);
                            });
                        }
                        else {
                            alert('请检查参数');
                        }
                    })
                    .catch(err => {
                        console.log(err);
                    });
            }).catch(() => {
                
            });
        },
        goHome: function() {
            this.$router.push({
				path: "/",
			});            
        }
    },
    mounted() {
        this.getGroupInfo();
    }
}
</script>
<style>
    .exam {
        height: 100%;
        background-image: linear-gradient(to bottom , #108EE9, #FFFFFF);
	}
    .exam .login-title-1 {
		position: absolute;
		width: fit-content;
		top: 5px;
		left: 5px;
		color: white;
		font-size: 20px;
	}
	.exam .login-title-2 {
		position: absolute;
		width: fit-content;
		top: 5px;
		right: 5px;
		color: white;
		font-size: 20px;
	}
    .exam .info-container {
		position: absolute; 
		display: flex;
        flex-wrap: wrap;  
		top: 52%;   
		left: 50%;   
		-webkit-transform: translate(-50%, -50%);   
		-moz-transform: translate(-50%, -50%);   
		-ms-transform: translate(-50%, -50%);   
		-o-transform: translate(-50%, -50%);   
		transform: translate(-50%, -50%);
		width: 90%;
        height: 90%;
		padding: 10px 5px 10px 5px;
		border-radius: 25px;
		margin: 0px auto;
		background: #fff;
		background-clip: padding-box;
	}
    .exam .info-container .info-list {
        width: 100%;
        height: 15%;
		display: flex;
        flex-wrap: wrap;
        border-bottom:1px dashed grey;
        margin: 0 5px 0 5px;
    }
    .exam .info-container .info-list .label1 {
        width: 10%;
        height: 50%;
        color: grey;
		font-size: 12px;
        display: flex;
		justify-content: right;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .exam .info-container .info-list .text1 {
        width: 30%;
        height: 50%;
        color: black;
		font-size: 12px;
        display: flex;
		justify-content: right;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .exam .info-container .info-list .label2 {
        width: 20%;
        height: 50%;
        color: grey;
		font-size: 12px;
        display: flex;
		justify-content: right;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .exam .info-container .info-list .text2 {
        width: 40%;
        height: 50%;
        color: black;
		font-size: 12px;
        display: flex;
		justify-content: right;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .exam .info-container .info-list .label3 {
        width: 10%;
        height: 50%;
        color: grey;
		font-size: 12px;
        display: flex;
		justify-content: right;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .exam .info-container .info-list .text3 {
        width: 30%;
        height: 50%;
        color: black;
		font-size: 12px;
        display: flex;
		justify-content: center;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .exam .info-container .info-list .label4 {
        width: 20%;
        height: 50%;
        color: grey;
		font-size: 12px;
        display: flex;
		justify-content: right;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .exam .info-container .info-list .text4 {
        width: 40%;
        height: 50%;
        color: black;
		font-size: 12px;
        display: flex;
		justify-content: right;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
</style>