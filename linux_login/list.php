<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script type="text/javascript" src="./php/jquery-3.7.0.min.js"></script>
    <title>文章列表></title>
    <style>
        table{
            width: 800px;
            margin: auto;
            border: solid 1px green;
            border-spacing: 0px;
        }

        td{
            border:solid 1px gray;
            height: 30px;
        }
    </style>
    <script>
        function doDelete(articleid){
            if(!window.confirm("你确定要删除该文章吗?")){
                return false;
            }
            
            $.post('delete.php','articleid=' + articleid,function(data){
                if (data == 'delete-ok') {
                    window.alert('删除成功');
                    //location.href='list.php';
                    location.reload();   //刷新当前页面
                }else{
                    window.alert('删除失败' + data);
                }
            });
        }
    </script>
</head>
<body>
    
    <table>
        <tr>
            <td>序号</td>
            <td>编号</td>
            <td>作者</td>
            <td>标题</td>
            <td>次数</td>
            <td>时间</td>
            <td>操作</td>
        </tr>
    <?php

    include "common.php";

    if(!isset($_SESSION['islogin']) || $_SESSION['islogin'] != 'true'){
        die("请先登录。<a href='login.html'>点此登录</a>");
    }

    $conn = create_connection();
    $sql = "select articleid,author,headline,viewcount,createtime from article where isDelete=1";
    $result = mysqli_query($conn,$sql);

    // 将数据库查询到的结果集中的数据取出，保存到一个数组中
    $rows = mysqli_fetch_all($result,MYSQLI_ASSOC);

    //遍历结果集数据并表格中展示
    $i = 1;
    foreach($rows as $row){
        echo '<tr>';
        echo '<td>' . $i . '</td>';
        echo '<td>' . $row['articleid'] . '</td>';
        echo '<td>' . $row['author'] . '</td>';
        echo '<td><a href="read.php?id=' . $row['articleid'] . '">' . $row['headline'] . '</a></td>';
        echo '<td>' . $row['viewcount'] . '</td>';
        echo '<td>' . $row['createtime'] . '</td>';
        echo '<td><button onclick="doDelete(' . $row['articleid'] . ')">删除</button><button>编辑</button></td>';
        echo '</tr>';
        $i += 1;
    }
    mysqli_close($conn);

    ?>
    </table>

    <br><hr><br>

    <div style="width:100%; margin:auto;text-align:center"><a href="add.php">发表文章</a></div>

</body>
</html>
