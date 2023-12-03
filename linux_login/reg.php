<?php

include "common.php";
//设置使用中国北京时间作为时区
date_default_timezone_set("PRC");

$conn = create_connection();

$username = $_POST['username'];
$password = $_POST['password'];
$tmpPath = $_FILES['photo']['tmp_name'];    //获取文件的临时路径
$fileName = $_FILES['photo']['name'];       //获取文件的原始文件名

// echo $tmpPath . '<br/>';
// 判断后缀名
// $split = explode(".",$fileName)
// $extName = end($split);
// if ($extName == 'php') {
//   die("invalid-file");
// }

// 判断文本类型
$fileType = $_FILES["photo"]["type"];
if ($fileType != 'image/jpeg' && $fileType != 'image/png' && $fileType != 'image/gif'){
  die("invalid-file");
}

$sql = "select username from users where username='$username'";
$result = mysqli_query($conn,$sql);
$count = mysqli_num_rows($result);
if($count >= 1){
    die('user-exists');
}

//上传文件，从临时路径移动到指定路径
// move_uploaded_file($tmpPath,'./upload/' . $fileName) or die('文件上传失败');

//使用时间戳对上传文件进行重命名
$suffix = explode(".",$fileName);
$newName = date('Ymd_His.') . end($suffix);
move_uploaded_file($tmpPath,'./upload/' . $newName) or die('文件上传失败');

// $now = date('Y-m-d H:i:s');
// $md5password = md5($password);
// $sql = "insert into users(username,password,avatar,createtime) values ('$username','$md5password','$newName',now())" ;
// mysqli_query($conn,$sql) or die('reg-fail');
// mysqli_close($conn);

echo '请确认你的个人信息：<br/><hr>';
echo "用户名：$username<br/>";
echo "密码为：$password<br/>";
echo "头像：<img src='./upload/$newName' width=300/><br/>";
echo "<a href='login.html'>点此登录</a>";

?>