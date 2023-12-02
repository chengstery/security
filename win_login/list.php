<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script type="text/javascript" src="jquery-3.7.0.min.js"></script>
    <title><?php echo date("Y-m-d H:i:s"); ?></title>
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

    // session_start();   //要用session都要确保调用此函数

    // if($_SESSION['islogin'] != 'true'){
    //     die("请先登录。");
    // }

    $conn = mysqli_connect('127.0.0.1','root','你的数据库密码','learn') or die("数据库连接不成功.");
    mysqli_query($conn,"set names utf8");

    $sql = "select articleid,author,headline,viewcount,createtime from article where isDelete=1";
    $result = mysqli_query($conn,$sql);

    // 将数据库查询到的结果集中的数据取出，保存到一个数组中
    //$rows = mysqli_fetch_all($result);
    //mysqli_fetch_all  默认使用索引数组，也可以设定参数强制使用关联数组
    $rows = mysqli_fetch_all($result,MYSQLI_ASSOC);

    //便利结果集数据并输出到页面中
    // foreach($rows as $row){
    //     echo $row[0] . '-' . $row[1] . '-' . $row[2] . '-' . $row[3] . '-' . $row[4] . "<br/>";
    // }

    //便利结果集数据并表格中展示
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

</body>
</html>
