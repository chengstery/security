<?php

//利用Session保存图片验证码
session_start();

// $type = $_GET['type'];
// if ($type == 'vcode'){
//     getCode();
// }elseif($type == 'text'){
//     echo $_SESSION['vcode'];
// }

getCode();

//生成图片验证码
function getCode($vlen = 4,$width = 110,$height = 40){
    //定义响应类型为PNG图片
    header("content-type:image/png");

    //生成随机验证码字符串，并将其保存在Session中
    $chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890';
    //$chars = '0000';
    $vcode = substr(str_shuffle($chars),0,$vlen);

    $_SESSION['vcode'] = $vcode;

    //调用setcookie函数生成自定义Cookie
    //setcookie("vcode",$vcode,time()+3600*24*30*12);

    //定义图片并设置背景色RGB为：100，200，100
    $image = imagecreate($width,$height);
    $imgColor = imagecolorallocate($image,100,200,200);

    //以RGB=0，0，0的颜色绘制黑色文字
    $color = imagecolorallocate($image,0,0,0);
    imagestring($image,5,30,12,$vcode,$color);

    //生成一批随机位置的干扰点
    for($i=0;$i<50;$i++){
        imagesetpixel($image,rand(0,$width),rand(0,$height),$color);
    }

    //输出图片验证码
    imagepng($image);
    imagedestroy($image);

}


?>