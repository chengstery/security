<?php

include "common.php";
//修复漏洞，在显示文本前，先进行SESSION验证
if (!isset($_SESSION['islogin']) or $_SESSION['islogin'] != 'true') {
    die("你还没有登录，无法访问本页面</br>");

}

echo '欢迎登录安全测试平台</br>'

?>