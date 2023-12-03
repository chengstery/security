<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script type="text/javascript" src="./php/jquery-3.7.0.min.js"></script>
    <title>发表文章</title>
    <style>
        #outer{
            width: 800px;
            height: 600px;
            border: solid 0px red;
            margin: auto;
        }
        #outer div{
            margin: 20px;
            border: solid 0px gray;
        }
        #outer div input{
            width: 600px;
        }
        #outer div textarea{
            width: 600px;
            height: 300px;
        }
    </style>

    <script>
        function doAdd(){
            var headline = $("#headline").val();
            var content = $("#content").val();
            var param = "headline=" + headline + "&content=" + content;
            $.post("doadd.php",param,function(data){
                if (data =="add-success") {
                    alert('发表文章成功.');
                    location.href = 'list.php';
                }else{
                    alert('发表文章失败.');
                }

            });
        }

    </script>
</head>
<?php session_start()?>
<body>

    <div id="outer">
        <div>你的当前用户名：<?=$_SESSION['username']?>，角色为：<?php echo $_SESSION['role']?></div>
        <div>请输入文章标题：<input type="text" id="headline"/></div>
        <div>请输入文章内容：<textarea id="content"></textarea></div>
        <div style="text-align:center;"><button onclick="doAdd()">提交文章</button></div>
    </div>
    
</body>
</html>