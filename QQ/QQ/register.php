<style type="text/css">
a:link{
//設定還沒有瀏覽過的連結
text-decoration:none;
background-color:#ffffff;
}
a:visited {
//設定已經瀏覽過的連結
color:#ffffff;
background-color:red;
}
a:hover {
//設定滑鼠移經的連結
text-decoration:underline;
background-color:#fafafa;
color:gray;
}
a:active {
//設定正在點選的連結
text-decoration:none;
background-color:gray;
color:#fafafa;

}
</style>
<html>
    <title>跳轉頁面</title>
</html>
<?php 
$conn=require_once("config.php");
if($_SERVER["REQUEST_METHOD"]=="POST"){
    $username=$_POST["username"];
    $password=$_POST["password"];
    //檢查帳號是否重複
    $check="SELECT * FROM users WHERE username='".$username."'";
    if(mysqli_num_rows(mysqli_query($conn,$check))==0){
        $sql="INSERT INTO users (id,username, password)
            VALUES(NULL,'".$username."','".$password."')";
        
        if(mysqli_query($conn, $sql)){
            echo "註冊成功!3秒後將自動跳轉頁面<br>";
            echo "<a href='index.php#tologin'>未成功跳轉頁面請點擊此</a>";
            header("refresh:3;url=index.php#tologin");
            exit;
        }else{
            echo "Error creating table: " . mysqli_error($conn);
        }
    }
    else{
        echo "該帳號已有人使用!<br>3秒後將自動跳轉頁面<br>";
        echo "<a href='index.php#toregister'>未成功跳轉頁面請點擊此</a>";
        header("refresh:3;url=index.php#toregister");
        //header("refresh:3;url=register.html",true);
        exit;
    }
}


mysqli_close($conn);

function function_alert($message) { 
      
    // Display the alert box  
    echo "<script>alert('$message');
     window.location.href='index.php';
    </script>"; 
    
    return false;
} 
?>