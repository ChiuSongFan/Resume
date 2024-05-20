<!DOCTYPE html>
<html lang="utf-8">
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
    integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
    crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
    integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
    crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
    integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
    crossorigin="anonymous"></script>

<head>
    <title>TimesShow 泰秀影城 - 線上購票 Powered by 旭旭購票</title>

    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <!-- FontAwesome CSS -->
    <link rel="stylesheet" href="css/font-awesome.min.css">

    <!-- ElegantFonts CSS -->
    <link rel="stylesheet" href="css/elegant-fonts.css">

    <!-- themify-icons CSS -->
    <link rel="stylesheet" href="css/themify-icons.css">

    <!-- Swiper CSS -->
    <link rel="stylesheet" href="css/swiper.min.css">

    <!-- Styles -->
    <link rel="stylesheet" href="./style.css">
</head>

<body>
        <div class="nav-bar">
            <div class="container">
                <div class="row">
                    <div class="col-9 col-lg-3">
                        <div class="site-branding">
                            <h1 class="site-title"><a href="index.html" rel="home">泰秀影城</a></h1>
                        </div><!-- .site-branding -->
                    </div><!-- .col -->

                    <div class="col-3 col-lg-9 flex justify-content-end align-content-center">
                        <nav class="site-navigation flex justify-content-end align-items-center">
                            <ul class="flex flex-column flex-lg-row justify-content-lg-end align-content-center">
                                <li><a href="#">電影資訊</a></li>
                                <li><a href="theater.html">影城介紹</a></li>
                                <li><a href="login_index.php">會員登入</a></li>
                            </ul>

                            <div class="hamburger-menu d-lg-none">
                                <span></span>
                                <span></span>
                                <span></span>
                                <span></span>
                            </div><!-- .hamburger-menu -->

                            <div class="header-bar-cart">
                                <a href="#" class="flex justify-content-center align-items-center"><span
                                        aria-hidden="true" class="icon_bag_alt"></span></a>
                            </div><!-- .header-bar-search -->
                        </nav><!-- .site-navigation -->
                    </div><!-- .col -->
                </div><!-- .row -->
            </div><!-- .container -->
        </div>
</body?>

    <?php
    session_start();
    
    if(isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true){
        header("location: index.php");
        exit; 
    }
    ?>
    <head>
        <title>登入畫面</title>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
        <meta name="description" content="Login and Registration Form with HTML5 and CSS3" />
        <meta name="keywords" content="html5, css3, form, switch, animation, :target, pseudo-class" />
        <meta name="author" content="Codrops" />
        <link rel="shortcut icon" href="../favicon.ico"> 
        <link rel="stylesheet" type="text/css" href="css/demo.css" />
        <link rel="stylesheet" type="text/css" href="css/style3.css" />
		<link rel="stylesheet" type="text/css" href="css/animate-custom.css" />
    </head>
    <body>
        <div class="container">
            <header>
            </header>
            <section>				
                <div id="container_demo" >
                    <a class="hiddenanchor" id="toregister"></a>
                    <a class="hiddenanchor" id="tologin"></a>
                    <div id="wrapper">
                        
                        <div id="login" class="animate form">
                            
                            <form  method="post" action="login.php" autocomplete="on"> 
                                <h1>登入</h1> 
                                <p> 
                                    <label for="username" class="uname" data-icon="u" >使用者名稱 </label>
                                    <input id="username" name="username" required="required" type="text" placeholder="使用者名稱"/>
                                </p>
                                <p> 
                                    <label for="password" class="youpasswd" data-icon="p"> 您的密碼</label>
                                    <input id="password" name="password" required="required" type="password" placeholder="範例: X8df!90EO" /> 
                                </p>
                                <p class="keeplogin"> 
									<input type="checkbox" name="loginkeeping" id="loginkeeping" value="loginkeeping" /> 
									<label for="loginkeeping">記住我</label>
								</p>
                                <p class="login button"> 
                                    <input type="submit" name="submit" value="登入" /> 
								</p>
                                <p class="change_link">
									還不是會員 ?
									<a href="#toregister" class="to_register">註冊會員</a>
								</p>
                            </form>
                        </div>

                        <div id="register" class="animate form">
                        <form name="registerForm" method="post" action="register.php" onsubmit="return validateForm()">
                                <h1> 註冊會員 </h1> 
                                <p> 
                                    <label for="username" class="uname" data-icon="u">使用者名稱</label>
                                    <input type="text" name="username">
                                </p>
                                <p> 
                                    <label for="password" class="youpasswd" data-icon="p">密碼</label>
                                    <input type="password" name="password" id="password">
                                </p>
                                <p> 
                                    <label for="passwordsignup_confirm" class="youpasswd" data-icon="p">確認密碼</label>
                                    <input type="password" name="password_check" id="password_check">
                                </p>
                                <p class="signin button"> 
                                    <input type="submit" value="註冊" name="submit">
								</p>
                                <p class="change_link">  
									已經有會員 ?
									<a href="#tologin" class="to_register"> 登入 </a>
								</p>
                            </form>
                        </div>
						
                    </div>
                </div>  
            </section>
        </div>
    </body>
</html>