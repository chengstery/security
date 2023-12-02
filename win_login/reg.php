<?php

$conn = mysqli_connect('127.0.0.1','root','你的数据库密码','learn') or die("数据库连接不成功.");

$username = $_POST['username'];
$password = $_POST['password'];

$sql = "select username from user where username='$username'";
$result = mysqli_query($conn,$sql);
$count = mysqli_num_rows($result);
if($count >= 1){
    die('user-exists');
}

$sql = "insert into user(username,password) values ('$username','$password')" ;
mysqli_query($conn,$sql) or die('reg-fail');
mysqli_close($conn);

echo 'reg-pass';

?>