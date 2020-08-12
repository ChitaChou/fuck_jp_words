<template>
    <div class="menu">
        <div class="login-title-1">
			<b><i>Fuck JP Words</i></b>
		</div>
		<div class="login-title-2">
			<i></i>
		</div>
        <div class="person-container">
			<div class="avatar">
				<img src="../assets/image/icon-user.png" height="100%" width="100%" alt="">
			</div>
			<div class="person-info">
				<div class="person-name1"></div>
				<div class="person-name"><b>用户1</b></div>
				<div class="person-comment">暂无</div>
			</div>
			<div class="status" id="status1">
				<div class="num" style="color: orange;">None</div>
				<div class="text">完成考试</div>
			</div>
			<div class="status" id="status2">
				<div class="num">None</div>
				<div class="text">平均分</div>
			</div>
			<div class="status" id="status3">
				<div class="num"></div>
				<div class="text"></div>
			</div>
			<div class="status" id="status4">
				<div class="num"></div>
				<div class="text"></div>
			</div>
        </div>
        <div class="ctrl-btn-container">
			<div class="btn" @click="goExam">
				<div class="icon"><img src="../assets/image/test.png" height="80%" width="80%" alt=""></div>
				<div class="text">去考试</div>
			</div>
			<div class="btn" @click="goHistory">
				<div class="icon"><img src="../assets/image/history.png" height="80%" width="80%" alt=""></div>
				<div class="text">考试历史</div>
			</div>
			<div class="btn" @click="goWordsManagement">
				<div class="icon"><img src="../assets/image/words.png" height="80%" width="80%" alt=""></div>
				<div class="text">单词管理</div>
			</div>
			<div class="btn" @click="goGroupManagement">
				<div class="icon"><img src="../assets/image/group.png" height="80%" width="80%" alt=""></div>
				<div class="text">单词分组管理</div>
			</div>
			<div class="btn">
				<div class="icon"></div>
				<div class="text"></div>
			</div>
			<div class="btn">
				<div class="icon"></div>
				<div class="text"></div>
			</div>
			<div class="btn">
				<div class="icon"></div>
				<div class="text"></div>
			</div>
			<div class="btn">
				<div class="icon"></div>
				<div class="text"></div>
			</div>
			<div class="btn">
				<div class="icon"></div>
				<div class="text"></div>
			</div>
			<div class="btn">
				<div class="icon"></div>
				<div class="text"></div>
			</div>
        </div>
    </div>
</template>
<script>
export default {
	methods:{
		exit(){
			this.$message({
				type: 'success',
				message: '已退出'
			});
			this.$router.push({
				path: "/",
			});
		},
		goWordsManagement(){
			this.$router.push({
				path: "/words",
			});
		},
		goGroupManagement() {
			this.$router.push({
				path: "/groups",
			});
		},
		goExam() {
			this.$router.push({
				path: "/exam",
			});
		},
		goHistory () {
			this.$router.push({
				path: "/history",
			});
		}
	},
    mounted(){
    }
}
</script>
<style>
    .menu {
        height: 100%;
        background-image: linear-gradient(to bottom , #108EE9, #FFFFFF);
	}

    .menu .login-title-1 {
		position: absolute;
		width: fit-content;
		top: 5px;
		left: 5px;
		color: white;
		font-size: 20px;
	}

	.menu .login-title-2 {
		position: absolute;
		width: fit-content;
		top: 5px;
		right: 5px;
		color: white;
		font-size: 20px;
	}

    .menu .person-container {
		position: absolute; 
		display: flex;
        flex-wrap: wrap;  
		top: 18%;   
		left: 50%;   
		-webkit-transform: translate(-50%, -50%);   
		-moz-transform: translate(-50%, -50%);   
		-ms-transform: translate(-50%, -50%);   
		-o-transform: translate(-50%, -50%);   
		transform: translate(-50%, -50%);
		width: 90%;
        height: 23%;
		padding: 10px 5px 10px 5px;
		border-radius: 25px;
		margin: 0px auto;
		background: #fff;
		background-clip: padding-box;
	}

	.menu .person-container .avatar {
		width: 30%;
		height: 60%;
		vertical-align: middle;
		text-align: center;
	}

	.menu .person-container .person-info {
		width: 70%;
		height: 60%;
		display: flex;
        flex-wrap: wrap;
	}

	.menu .person-container .person-info .person-name1{
		width: 100%;
		height: 10%;
		font-size: 17px;
		text-align: left;
	}

	.menu .person-container .person-info .person-name{
		width: 100%;
		height: 40%;
		font-size: 17px;
		text-align: left;
	}

	.menu .person-container .person-info .person-comment{
		width: 100%;
		height: 50%;
		font-size: 12px;
		color: gray;
		text-align: left;
		vertical-align:middle;
	}

	.menu .person-container .status{
		width: 25%;
		height: 40%;
	}

	.menu .person-container .status .num{
		width: 100%;
		height: 70%;
		color: red;
		font-size: 20px;
		display: flex;
		justify-content: center;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
	}

	.menu .person-container .status .text{
		width: 100%;
		height: 30%;
		text-align: center;
		vertical-align:middle;
	}

    .menu .ctrl-btn-container {
		position: absolute; 
		display: flex;
        flex-wrap: wrap;  
		top: 58%;   
		left: 50%;   
		-webkit-transform: translate(-50%, -50%);   
		-moz-transform: translate(-50%, -50%);   
		-ms-transform: translate(-50%, -50%);   
		-o-transform: translate(-50%, -50%);   
		transform: translate(-50%, -50%);
		width: 90%;
        height: 53%;
		padding: 10px 5px 10px 5px;
		border-radius: 25px;
		margin: 0px auto;
		background: #fff;
		background-clip: padding-box;
	}

	.menu .ctrl-btn-container .btn {
		width: 50%;
		height: 20%;
		display: flex;
        flex-wrap: wrap;
		flex-direction: row;
		align-items: center; /*垂直居中*/
    	justify-content: center; /*水平居中*/
		font-size: 0;
	}

	.menu .ctrl-btn-container .btn .icon {
		width: 30%;
		text-align: center;
	}

	.menu .ctrl-btn-container .btn .text {
		width: 70%;
		font-size: 16px;
		display: flex;
		justify-content: center;/*实现水平居中*/
		align-items:center; /*实现垂直居中*/
	}
</style>