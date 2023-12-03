<?php

/**
 * 本代码解决用户登录失败的次数限制问题，更加完整解决登录模块的爆破和其他漏洞
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
 $sql = "select userid,username,password,role,failcount,TIMESTAMPDIFF(minute,lasttime,now()) from users where username=?";

 //绑定查询参数
 $stmt = $conn->prepare($sql);
 $stmt->bind_param("s",$username);

 //绑定结果参数
 $stmt->bind_result($userid,$username2,$password2,$role,$failcount,$timediff);

 $stmt->execute();
 $stmt->store_result();

//认证和授权失败
 if($stmt->num_rows == 1){       //表明用户存在
    $stmt->fetch();

    //判断密码是否正确之前，先判断登录次数是否受限
    if($failcount >=5 && $timediff <=60){
      die('user-locked');
    }


    if ($md5password == $password2) {

      if($failcount > 0){
         $sql = "update users set failcount=0 where userid=?";
         $stmt = $conn->prepare($sql);
         $stmt->bind_param("i",$userid);
         $stmt->execute();
      }

      echo "login-pass";

    //登录成功后，记录SESSION变量
    $_SESSION['username'] = $username;
    $_SESSION['islogin'] = 'true';
    $_SESSION['role'] = $role;

    echo "<script>location.href='list.php'</script>";
    }else{

      $sql = "update users set failcount=failcount+1 ,lasttime=now() where userid=?";
      $stmt = $conn->prepare($sql);
      $stmt->bind_param("i",$userid);
      $stmt->execute();

      echo "login-fail";
      echo "<script>location.href='login.html'</script>";
    }   
 }else{
    echo "user-invalid";
    echo "<script>location.href='login.html'</script>";
 }


 //关闭数据库
$conn->close();

?>