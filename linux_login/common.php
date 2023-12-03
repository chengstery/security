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
    //echo $result->num_rows;
    //获取结果集数组
    $rows = $result->fetch_all(MYSQLI_ASSOC);
    //var_dump($rows);
    foreach($rows as $row){
        echo "username:" . $row['username'] . ",password:" . $row['password'] . "<br/>";
    }
}

//MySQLi预处理功能（面向对象）
function mysqli_prepare_stmt(){
    $conn = create_connection_oop();

    //?在预处理语句中用于代替参数
    $sql = "update users set username = ? where userid = ?";  

    //实例化Prepared Statement与处理对象
    $stmt = $conn->prepare($sql);
    //实例化后需要将参数值进行绑定并在执行时替换
    //bind_param第一个参数是数据类型  i:整数，s:字符串，d:小数,b:二进制
    $stmt->bind_param("si",$username,$userid);
    $username = 'hahasb';
    $userid = 6;

    //正式执行SQL语句
    //$stmt->execute();   //execute()返回布尔类型
    //$conn->commit();    //默认情况下，更新操作会自动提交，也可手工处理

    //如果针对查询语句需进行结果绑定
    $sql = "select * from users where userid < ?";  
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("i",$userid);
    $userid = 6;

    //绑定结果参数
    $stmt->bind_result($userid,$username,$password,$role,$avatar,$createtime);
    $stmt->execute();

    //调用结果并处理
    $stmt->store_result();

    //输出行数
    echo $stmt->affected_rows . "<br/>";
    echo $stmt->num_rows . "<br/>";

    //遍历结果
    while ($stmt->fetch()) {
        echo $userid,$username,$password,'<br/>';
    }

}

//test_mysqli_oop();
//mysqli_prepare_stmt();

?>