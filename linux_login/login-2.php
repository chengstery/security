<?php

/**
 * 本代码通过转义引号对SQL注入进行防护
 */

include "common.php";

//获得用户发送的请求
//使用addslashes函数强制将用户输入的引号添加转义符
$username = addslashes($_POST['username']);
$password = $_POST['password'];
$vcode = $_POST['vcode'];

//验证码的验证

 if($vcode !== '0000'){
    die("vcode-error");
 }

 $conn = create_connection();

 $md5password = md5($password);
 //拼接SQL语句并执行它
 //先查用户名对比密码
 $sql = "select * from users where username='$username'";
 $result = mysqli_query($conn,$sql) or die("SQL语句执行错误");   //result获取到的查询结果，称为结果集

//认证和授权失败
 if(mysqli_num_rows($result) == 1){
    $row = mysqli_fetch_assoc($result);
    //var_dump($row);  //打印
    if ($md5password == $row['password']) {
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
 mysqli_close($conn);

?>