<?php

/**
 * 本代码通过MySQLi的预处理功能来对SQL注入进行防护，并进行验证码防护
 */


include "common.php";

//获得用户发送的请求
$username = $_POST['username'];
$password = $_POST['password'];
$vcode = $_POST['vcode'];

//根据图片验证码验证
if (strtoupper($_SESSION['vcode']) != strtoupper($vcode)) {
   die("vcode-error");
}else {
   //验证码成功后清空本次Session中的验证码
   unset($_SESSION['vcode']);
   //$_SESSION['vcode'] = '';  //可以用空字符验证码绕过
}

// if (strtoupper($_COOKIE['vcode']) != strtoupper($vcode)) {
//    die("vcode-error");
// }

//每提交一次都清空，会增加服务器负担
unset($_SESSION['vcode']);

 $conn = create_connection_oop();

 //md5加密
 $md5password = md5($password);

 //拼接SQL语句并执行它
 //先查用户名对比密码
 $sql = "select userid,username,password,role from users where username=?";

 //绑定查询参数
 $stmt = $conn->prepare($sql);
 $stmt->bind_param("s",$username);

 //绑定结果参数
 $stmt->bind_result($userid,$username2,$password2,$role);

 $stmt->execute();
 $stmt->store_result();


//认证和授权失败
 if($stmt->num_rows == 1){
    $stmt->fetch();
    if ($md5password == $password2) {
      echo "login-pass";

    //登录成功后，记录SESSION变量
    $_SESSION['username'] = $username;
    $_SESSION['islogin'] = 'true';

    echo "<script>location.href='welcome.php'</script>";
    }else{
      echo "login-fail";
      echo "<script>location.href='login.html'</script>";
    }   
 }else{
    echo "login-fail";
    echo "<script>location.href='login.html'</script>";
 }


 //关闭数据库
$conn->close();

?>