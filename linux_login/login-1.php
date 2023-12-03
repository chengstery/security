<?php

/**
 * 最初有SQL注入漏洞和验证码漏洞的代码
 */

include "common.php";

//获得用户发送的请求
$username = $_POST['username'];
$password = $_POST['password'];
$vcode = $_POST['vcode'];

//验证码的验证


 if($vcode !== '0000'){
    die("vcode-error");
 }

 $conn = create_connection();

 $md5password = md5($password);
 //拼接SQL语句并执行它
 //该SQL语句在实现登录操作时,存在严重的逻辑问题
 $sql = "select * from users where username='$username' and password='$md5password'";
 $result = mysqli_query($conn,$sql) or die("SQL语句执行错误");   //result获取到的查询结果，称为结果集

//认证和授权失败
 if(mysqli_num_rows($result) == 1){
    echo "login-pass";

    //登录成功后，记录SESSION变量
    $_SESSION['username'] = $username;
    $_SESSION['islogin'] = 'true';

    //echo "<script>location.href='welcome.php'</script>";
 }else{
    echo "login-fail";
    echo "<script>location.href='login.html'</script>";
 }


 //关闭数据库
 mysqli_close($conn);

?>