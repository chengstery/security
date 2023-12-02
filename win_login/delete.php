<?php

$articleid = $_POST['articleid'];

$conn = mysqli_connect('127.0.0.1','root','你的数据库密码','learn') or die("数据库连接不成功.");
//mysqli_query($conn,"delete from article where articleid=$articleid") or die("delete-fail");
mysqli_query($conn,"update article set isDelete=0 where articleid=$articleid") or die("delete-fail");

echo 'delete-ok';

//通常在进行删除时，会使用软删除：回收站、设定列表识


?>