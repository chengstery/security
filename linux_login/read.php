<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div{
            width: 800px;
            margin: auto;
            height: 40px;
        }
    </style>
</head>
<body>
    <?php

    include "common.php";

    // header("Content-Security-Policy: script-src 'self'");
    // header("Content-Security-Policy: script-src 'self' http://192.168.88.137:3000");
    // header("Content-Security-Policy: script-src 'self' http://192.168.88.150 'unsafe-inline'");
    header("Content-Security-Policy: script-src 'self'; report-uri http://192.168.88.130/security/cspreport.php");

    if(!isset($_SESSION['islogin']) || $_SESSION['islogin'] != 'true'){
        die("请先登录。<a href='login.html'>点此登录</a>");
    }

    $conn = create_connection();
    
    //$id = addslashes($_GET['id']);
    $id = $_GET['id'];
    $conn = mysqli_connect('127.0.0.1','root','13360296757','learn') or die("数据库连接不成功.");
    mysqli_query($conn,"set names utf8");

    //$sql = "select articleid,author,headline,content,viewcount,createtime from article where articleid=$id";
    $sql = "select * from article where articleid=$id";
    $result = mysqli_query($conn,$sql);
    ini_set("display_errors", "On");//打开错误提示
    ini_set("error_reporting",E_ALL);//显示所有错误

    $article = mysqli_fetch_assoc($result);   //读取结果集中第一行数据，并用关联数组展示

    ?>

    <div><?=$article['headline']?></div>
    <div><hr/></div>
    <div><?=$article['content']?></div>
</body>
</html>

