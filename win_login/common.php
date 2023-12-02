<?php

session_start();

function create_connection(){
    //连接数据库
    $conn = mysqli_connect('127.0.0.1','root','你的数据库密码','learn') or die("数据库连接不成功.");

    //设置编码格式的两种方式
    mysqli_query($conn,"set names utf8");
    mysqli_set_charset($conn,'utf8');
    
    return $conn;
}

function create_connection_oop(){
    //连接数据库
    $conn = mysqli_connect('127.0.0.1','root','你的数据库密码','learn') or die("数据库连接不成功.");

    //设置编码格式的两种方式
    $conn->query("set names utf8");
    $conn->set_charset('utf8');
    
    return $conn;
}

//执行SQL语句
function test_mysqli_oop(){
    $conn = create_connection_oop();
    $sql = "select * from users where userid < 6";
    $result = $conn->query($sql);
    //获取结果集行数
    echo $result->num_rows;
    //获取结果集数组
    $rows = $result->fetch_all();
    var_dump($rows);
}

//MySQLi预处理功能（面向对象）
function mysqli_prepare_stmt(){
    $conn = create_connection_oop();

    //?在预处理语句中用于代替参数
    //$sql = "select * from users where username=? and password=?";
    //$stmt->bind_param("ss",$username,$password);
    $sql = "select * from users where userid < ?";  

    //实例化Prepared Statement与处理对象
    $stmt = $conn->prepare($sql);
    //实例化后需要将参数值进行绑定并在执行时替换
    //bind_param第一个参数是数据类型  i:整数，s:字符串，d:小数,b:二进制
    $stmt->bind_param("i",$userid);
    $userid = 6;

    //正式执行SQL语句
    $stmt->execute();   //execute()返回布尔类型

    //如果针对查询语句需进行结果绑定
}

test_mysqli_oop();


?>