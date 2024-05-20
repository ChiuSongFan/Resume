
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
    <div>

        <div class="nav-bar">
            <div class="container">
                <div class="row">
                    <div class="col-9 col-lg-3">
                        <div class="site-branding">
                            <h1 class="site-title"><a href="index.php" rel="home">泰秀影城</a></h1>
                        </div><!-- .site-branding -->
                    </div><!-- .col -->

                    <div class="col-3 col-lg-9 flex justify-content-end align-content-center">
                        <nav class="site-navigation flex justify-content-end align-items-center">
                            <ul class="flex flex-column flex-lg-row justify-content-lg-end align-content-center">
                                <li><a href="#">電影資訊</a></li>
                                <li><a href="theater.html">影城介紹</a></li>
                                <li><a href="order.php">訂票</a></li>
                                <li><a href="">歷史訂單</a></li>
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
        </div><!-- .nav-bar -->
    </div>
    <section class="featured-courses  vertical-column courses-wrap">
        <div class="container">
        <div class="d-flex align-items-center justify-content-center h-100">
        <select name="cinemas">
            <option value="">選擇影城</option>
            <option value="1">欣欣秀泰</option>
            <option value="2">台北今日秀泰</option>
            <option value="3">台北東南亞秀泰</option>
            <option value="4">板橋秀泰</option>
        </select>
        <select name="movie">
            <option value="">請選擇電影</option>
            <option value="1">蜘蛛人:無家日</option>
            <option value="2" selected>作家我就爛</option>
            <option value="3">尋找神話之鳥</option>
   
        </select>
        <select name="time">
            <option value="">請選擇時段</option>
            <option value="t1">10:30</option>
            <option value="t2" selected>13:30</option>
            <option value="t3">20:30</option>
   
        </select>

        <button class="btn btn-dark  p-2" type="button" name="button"  onclick="search()">查詢</button>
        <script type="text/javascript">
        function search(){

        //javascript獲取select控制元件的value和text值
        var c = document.getElementById("cinemas").value;//拿到select物件
        var m = document.getElementById("movie").value;//拿到select物件
        var t = document.getElementById("time").value;//拿到select物件
        <?php
        $conn=require_once "config.php";
        $sql = "SELECT * FROM totalorder WHERE username ='".$username."'";
        ?>
        </script>
</div>


        </div><!-- .container -->
    </section><!-- .courses-wrap -->
    <section class="h-100">
  <header class="container h-100">
    <div class="d-flex align-items-center justify-content-center h-100">
    <table>
<thead>
  <tr>
    <th><button class="btn btn-basic  p-2" type="button" name="button" disabled = true>1</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">2</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">3</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">4</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">5</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">6</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">7</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">8</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">9</button></th>
  </tr>
</thead>
<tbody>
  <tr>
  <th><button class="btn btn-basic  p-2" type="button" name="button">1</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">2</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">3</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">4</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">5</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">6</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">7</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">8</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">9</button></th>
  </tr>
  <tr>
  <th><button class="btn btn-basic  p-2" type="button" name="button">1</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">2</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">3</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">4</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">5</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">6</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">7</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">8</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">9</button></th>
  </tr>
  <tr>
  <th><button class="btn btn-basic  p-2" type="button" name="button">1</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">2</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">3</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">4</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">5</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">6</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">7</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">8</button></th>
    <th><button class="btn btn-basic  p-2" type="button" name="button">9</button></th>
  </tr>
</tbody>
</table>
    </div>
  </header>
</section>
</body>
