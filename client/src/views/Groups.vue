<template>
    <div class="group">
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
                    <p class="notice">分组名称</p>
                    <el-input type="text" class="input" v-model="group_name" auto-complete="off"></el-input>
                </div>
                <div class="filter-item"></div>
                <div class="filter-item"></div>
                <div class="filter-item"></div>
            </div>
            <div class="commit">
                <div class="commit-btn"><el-button type="primary" size="mini" @click="addGroup" round>添加</el-button></div>
            </div>
        </div>
        <div class="info-container">
            <div class="info-list" v-for="(item, index) in group_info" :key="index">
                <div class="label1">序号</div>
                <div class="text1">{{item.group_id}}</div>
                <div class="label2">分组名称</div>
                <div class="text2">{{item.group_name}}</div>
                <div class="label3">添加时间</div>
                <div class="text3">{{item.add_datetime}}</div>
                <div class="label4"></div>
                <div class="text4"></div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            function_title: '单词分组管理',
            group_name: '',
            group_info: []
        }
    },
    methods: {
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
        addGroup: function() {
            if (this.group_name == '') {
                alert('信息未填写完整');
            }
            else {
                var group_data = {
                    "group_name": this.group_name
                };
                this.$axios
                .post('/api/group', group_data)
                .then(res => {
                    if(res.data == 'add_success'){
                        alert('添加成功');
                        this.group_name = '';
                        this.getGroupInfo();
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
        this.getGroupInfo();
    }
}
</script>
<style>
    .group {
        height: 100%;
        background-image: linear-gradient(to bottom , #108EE9, #FFFFFF);
	}
    .group .login-title-1 {
		position: absolute;
		width: fit-content;
		top: 5px;
		left: 5px;
		color: white;
		font-size: 20px;
	}
	.group .login-title-2 {
		position: absolute;
		width: fit-content;
		top: 5px;
		right: 5px;
		color: white;
		font-size: 20px;
	}
    .group .filter-container {
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
    .group .filter-container .title {
        position: absolute;
		width: fit-content;
		top: 7px;
		left: 20px;
		color: black;
		font-size: 15px;
    }
    .group .filter-container .filter {
        width: 100%;
        display: flex;
        flex-wrap: wrap;
    }
    
    .group .filter-container .filter .filter-item{
        width: 50%;
        display: flex;
        flex-wrap: wrap;
        margin: 0 0 5px 0;
    }
    .group .filter-container .filter .filter-item .notice{
        width: 20%;
		color: black;
		font-size: 12px;
        display: flex;
		justify-content: right;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .group .filter-container .filter .filter-item .input{
        width: 80%;
        height: 60%;
    }
    .group .filter-container .commit .commit-btn{
        position: absolute;
		width: fit-content;
		bottom: 5px;
		right: 20px;
    }
    .group .info-container {
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
    .group .info-container .info-list {
        width: 100%;
        height: 20%;
		display: flex;
        flex-wrap: wrap;
        border-bottom:1px dashed grey;
        margin: 0 5px 0 5px;
    }
    .group .info-container .info-list .label1 {
        width: 10%;
        height: 50%;
        color: grey;
		font-size: 12px;
        display: flex;
		justify-content: right;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .group .info-container .info-list .text1 {
        width: 30%;
        height: 50%;
        color: black;
		font-size: 12px;
        display: flex;
		justify-content: center;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .group .info-container .info-list .label2 {
        width: 20%;
        height: 50%;
        color: grey;
		font-size: 12px;
        display: flex;
		justify-content: right;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .group .info-container .info-list .text2 {
        width: 40%;
        height: 50%;
        color: black;
		font-size: 12px;
        display: flex;
		justify-content: right;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .group .info-container .info-list .label3 {
        width: 30%;
        height: 50%;
        color: grey;
		font-size: 12px;
        display: flex;
		justify-content: right;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .group .info-container .info-list .text3 {
        width: 40%;
        height: 50%;
        color: black;
		font-size: 12px;
        display: flex;
		justify-content: right;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .group .info-container .info-list .label4 {
        width: 15%;
        height: 50%;
        color: grey;
		font-size: 12px;
        display: flex;
		justify-content: right;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
    .group .info-container .info-list .text4 {
        width: 15%;
        height: 50%;
        color: black;
		font-size: 12px;
        display: flex;
		justify-content: right;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
    }
</style>