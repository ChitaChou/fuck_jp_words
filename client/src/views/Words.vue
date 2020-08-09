<template>
    <div class="user-management-admin">
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
                    <p class="notice">单词</p>
                    <el-input type="text" class="input" v-model="words_jp" auto-complete="off"></el-input>
                </div>
                <div class="filter-item">
                    <p class="notice">翻译</p>
                    <el-input type="text" class="input" v-model="trans_cn" auto-complete="off"></el-input>
                </div>
                <div class="filter-item">
                    <p class="notice">分组</p>
                    <el-select class="input" v-model="group_id" placeholder="-">
						<el-option v-for="(item, index) in group_info" :key="index" :label="item.group_name" :value="item.group_id"></el-option>
					</el-select>
                </div>
                <div class="filter-item"></div>
            </div>
            <div class="commit">
                <div class="commit-btn"><el-button type="primary" size="mini" @click="addWord" round>添加</el-button></div>
            </div>
        </div>
        <div class="info-container">
            <div class="info-list" v-for="(item, index) in word_info" :key="index">
                <div class="label1">单词</div>
                <div class="text1">{{item.words_jp}}</div>
                <div class="label2">翻译</div>
                <div class="text2">{{item.trans_cn}}</div>
                <div class="label3">分组</div>
                <div class="text3">{{item.group_id}}</div>
                <div class="label4">修改时间</div>
                <div class="text4">{{item.upd_datetime}}</div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            function_title: '单词管理',
            words_jp: '',
            trans_cn: '',
            group_id: '',
            word_info: [],
            group_info: []
        }
    },
    methods: {
        getWordInfo: function() {
            this.$axios
                .get('/api/word')
                .then(res => {
                    this.word_info = res.data;
                })
                .catch(err => {
                    console.log(err);
                });
        },
        getGroupInfo: function() {
            this.$axios
                .get('/api/group')
                .then(res => {
                    this.group_info = res.data;
                })
                .catch(err => {
                    console.log(err);
                });
        },
        addWord: function() {
            if (this.words_jp == '' || this.trans_cn == '' || this.group_id == '') {
                alert('信息未填写完整');
            }
            else {
                var words_data = {
                    "words_jp": this.words_jp,
                    "trans_cn": this.trans_cn,
                    "group_id": this.group_id
                };
                this.$axios
                .post('/api/word', words_data)
                .then(res => {
                    if(res.data == 'add_success'){
                        alert('添加成功');
                        this.words_jp = '';
                        this.trans_cn = '';
                        this.group_id = '';
                        this.getWordInfo();
                    }
                    if(res.data == 'parameter_missing'){
                        alert('请检查参数');
                    }
                })
                .catch(err => {
                    console.log(err);
                });
            }
        },
        goHome: function() {
            this.$router.push({
				path: "/",
			});            
        }
    },
    mounted() {
        this.getWordInfo();
        this.getGroupInfo();
    }
}
</script>
<style>
    .user-management-admin {
        height: 100%;
        background-image: linear-gradient(to bottom , #108EE9, #FFFFFF);
	}
    .user-management-admin .login-title-1 {
		position: absolute;
		width: fit-content;
		top: 5px;
		left: 5px;
		color: white;
		font-size: 20px;
	}
	.user-management-admin .login-title-2 {
		position: absolute;
		width: fit-content;
		top: 5px;
		right: 5px;
		color: white;
		font-size: 20px;
	}
    .user-management-admin .filter-container {
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
    .user-management-admin .filter-container .title {
        position: absolute;
		width: fit-content;
		top: 7px;
		left: 20px;
		color: black;
		font-size: 15px;
    }
    .user-management-admin .filter-container .filter {
        width: 100%;
        display: flex;
        flex-wrap: wrap;
    }
    
    .user-management-admin .filter-container .filter .filter-item{
        width: 50%;
        display: flex;
        flex-wrap: wrap;
        margin: 0 0 5px 0;
    }
    .user-management-admin .filter-container .filter .filter-item .notice{
        width: 20%;
		color: black;
		font-size: 12px;
        display: flex;
		justify-content: right;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .user-management-admin .filter-container .filter .filter-item .input{
        width: 80%;
        height: 60%;
    }
    .user-management-admin .filter-container .commit .commit-btn{
        position: absolute;
		width: fit-content;
		bottom: 5px;
		right: 20px;
    }
    .user-management-admin .info-container {
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
    .user-management-admin .info-container .info-list {
        width: 100%;
        height: 20%;
		display: flex;
        flex-wrap: wrap;
        border-bottom:1px dashed grey;
        margin: 0 5px 0 5px;
    }
    .user-management-admin .info-container .info-list .label1 {
        width: 10%;
        height: 50%;
        color: grey;
		font-size: 12px;
        display: flex;
		justify-content: right;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .user-management-admin .info-container .info-list .text1 {
        width: 30%;
        height: 50%;
        color: black;
		font-size: 12px;
        display: flex;
		justify-content: center;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .user-management-admin .info-container .info-list .label2 {
        width: 20%;
        height: 50%;
        color: grey;
		font-size: 12px;
        display: flex;
		justify-content: right;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .user-management-admin .info-container .info-list .text2 {
        width: 40%;
        height: 50%;
        color: black;
		font-size: 12px;
        display: flex;
		justify-content: right;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .user-management-admin .info-container .info-list .label3 {
        width: 10%;
        height: 50%;
        color: grey;
		font-size: 12px;
        display: flex;
		justify-content: right;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .user-management-admin .info-container .info-list .text3 {
        width: 30%;
        height: 50%;
        color: black;
		font-size: 12px;
        display: flex;
		justify-content: right;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .user-management-admin .info-container .info-list .label4 {
        width: 20%;
        height: 50%;
        color: grey;
		font-size: 12px;
        display: flex;
		justify-content: right;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .user-management-admin .info-container .info-list .text4 {
        width: 40%;
        height: 50%;
        color: black;
		font-size: 12px;
        display: flex;
		justify-content: right;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
</style>