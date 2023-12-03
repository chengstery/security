<?php

// 连接数据库并访问数据
$conn = new mysqli('127.0.0.1','root','你的数据库密码','learn');
$conn->set_charset('utf8');
$sql = "select articleid,author,viewcount,createtime from article where articleid<5";
$result = $conn->query($sql);

// 输出JSON数据到页面
$json = json_encode($result->fetch_all(MYSQLI_ASSOC));
echo $json;

$conn->close();



?>