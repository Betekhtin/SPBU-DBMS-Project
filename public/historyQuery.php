<?php
include 'getdata.php';
if (!empty($_COOKIE['sid'])) {
    // check session id in cookies
    session_id($_COOKIE['sid']);
}

session_start();
require_once 'classes/Auth.class.php';

?>
    <!DOCTYPE html>
    <html lang="ru">

    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=Edge">
        <title>История погоды | The weather service</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="styles/style.css">
    </head>

    <body>

        <?php if (Auth\User::isAuthorized()): ?>

        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css">

        <nav class="navbar navbar-default navbar-static-top">
            <div class="container-fluid">
                <!-- Brand and toggle get grouped for better mobile display -->
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                      <span class="sr-only">Toggle navigation</span>
                      <span class="icon-bar"></span>
                      <span class="icon-bar"></span>
                      <span class="icon-bar"></span>
                    </button>
                    <a class="navbar-brand glyphicon glyphicon-home" href="index.php"></a>
                </div>
                <!-- Collect the nav links, forms, and other content for toggling -->
                <div class="collapse navbar-collapse" id="navbar">
                    <ul class="nav navbar-nav">
                        <li class="active"><a href="history.php">История</a></li>
                        <li><a href="forecast.php">Прогноз</a></li>
                        <li><a href="about.php">О проекте</a></li>
                    </ul>
                    <!-- Right navbar -->
                    <ul class="nav navbar-nav navbar-right">
                        <form class="ajax" method="post" action="./ajax.php">
                            <input type="hidden" name="act" value="logout">
                            <div class="form-actions">
                                <button class="btn btn-large btn-success" type="submit">Выйти</button>
                            </div>
                        </form>
                    </ul>
                </div>
                <!-- /.navbar-collapse -->
            </div>
            <!-- /.container-fluid -->
        </nav>

<?php if ($_POST) {
       $country = $_POST['country'];
       $city = $_POST['city'];
       $date_from = $_POST['date_from'];
       $date_to = $_POST['date_to'];
       $query= 'select * from temperature where (date >= \''.$date_from.'\' and date <= \''.$date_to.' 23:00:00\') and (city_id='.$city.')';
       $temperature=ms_q($query,'temperature');
       //------------
       $query= 'select * from weather where (date >= \''.$date_from.'\' and date <= \''.$date_to.' 23:00:00\') and (city_id='.$city.')';
       $weather=ms_q($query,'weather');
        //------------
       $query= 'select * from wind where (date >= \''.$date_from.'\' and date <= \''.$date_to.' 23:00:00\') and (city_id='.$city.')';
       $wind=ms_q($query,'wind');
        //------------
       $query= 'select * from pressure where (date >= \''.$date_from.'\' and date <= \''.$date_to.' 23:00:00\') and (city_id='.$city.')';
       $pressure=ms_q($query,'pressure');
        //------------
       $query= 'select * from other_weather_data where (date >= \''.$date_from.'\' and date <= \''.$date_to.' 23:00:00\') and (city_id='.$city.')';
       $other_weather_data=ms_q($query,'other_weather_data');
       //------------
       $query= 'select * from clouds where (date >= \''.$date_from.'\' and date <= \''.$date_to.' 23:00:00\') and (city_id='.$city.')';
       $clouds=ms_q($query,'clouds');
       //-------все почти готово к работе
//       foreach ($temperature as $key => $value) {
//
//      echo "{$key} => {$value} ";
//       print_r($temperature);
//}
//       echo $temperature['temperature'][15]['date'];
//
      // echo count($temperature['temperature']);
?>
        <main>
            <div id="hint" class="normal"></div>
            <table class="table table-striped table-bordered table-hover">
                <tr class="header">
                    <td onmouseover="tooltip( this , 'Время в данном населённом пункте. Учитывается летнее/зимнее время' ,  'hint' )" onmouseout="hideInfo(this , 'hint')" colspan="2">
                        <div class="brdDateLightArc forDate">Date/Time</td>
                    <td onmouseover="tooltip( this , 'Температура воздуха (градусы Цельсия) на высоте 2 метра над поверхностью земли' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">T</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Атмосферное давление на уровне станции (миллиметры ртутного столба)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">Po</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Атмосферное давление, приведенное к среднему уровню моря (миллиметры ртутного столба)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">P</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Барическая тенденция: изменение атмосферного давления за последние три часа (миллиметры ртутного столба)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">Pa</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Относительная влажность (%) на высоте 2 метра над поверхностью земли' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">U</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Направление ветра (румбы) на высоте 10-12 метров над земной поверхностью, осредненное за 10-минутный период, непосредственно предшествовавший сроку наблюдения' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">DD</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Cкорость ветра на высоте 10-12 метров над земной поверхностью, осредненная за 10-минутный период, непосредственно предшествовавший сроку наблюдения (метры в секунду)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">Ff</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Максимальное значение порыва ветра на высоте 10-12 метров над земной поверхностью за 10-минутный период, непосредственно предшествующий сроку наблюдения (метры в секунду)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">ff10</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Максимальное значение порыва ветра на высоте 10-12 метров над земной поверхностью за период между сроками (метры в секунду)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">ff3</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Общая облачность' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">N</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Текущая погода, сообщаемая с метеорологической станции' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">WW</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Прошедшая погода между сроками наблюдения 1' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">W1</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Прошедшая погода между сроками наблюдения 2' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">W2</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Минимальная температура воздуха (градусы Цельсия) за прошедший период (не более 12 часов)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">Tn</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Максимальная температура воздуха (градусы Цельсия) за прошедший период (не более 12 часов)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">Tx</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Слоисто-кучевые, слоистые, кучевые и кучево-дождевые облака' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">Cl</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Количество всех наблюдающихся облаков Cl или, при отсутствии облаков Cl, количество всех наблюдающихся облаков Cm' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">Nh</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Высота основания самых низких облаков (м)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">H</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Высококучевые, высокослоистые и слоисто-дождевые облака' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">Cm</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Перистые, перисто-кучевые и перисто-слоистые облака' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">Ch</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Горизонтальная дальность видимости (км)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">VV</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Температура точки росы на высоте 2 метра над поверхностью земли (градусы Цельсия)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">Td</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Количество выпавших осадков (миллиметры)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">RRR</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Период времени, за который накоплено указанное количество осадков (часы)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">tR</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Состояние поверхности почвы без снега или измеримого ледяного покрова' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">E</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Минимальная температура поверхности почвы за ночь. (градусы Цельсия)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">Tg</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Состояние поверхности почвы со снегом или измеримым ледяным покровом' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">E'</div>
                    </td>
                    <td onmouseover="tooltip( this , 'Высота снежного покрова (см)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )">
                        <div class="brdDateLightArc">sss</div>
                    </td>
                </tr>
                <tbody>
<?php
       for ($i=0; $i<count($temperature['temperature']); $i++)
       {
           echo '<tr>';
           //$tmp=[];
           $str=$temperature['temperature'][$i]['date'];
           $tmp=explode(" ", $str);
           echo '<td>'.$tmp[0].'</td>';
           echo '<td>'.$tmp[1].'</td>';
           echo '<td>'.$temperature['temperature'][$i]['T'].'</td>';
           echo '<td>'.$pressure['pressure'][$i]['P0'].'</td>';
           echo '<td>'.$pressure['pressure'][$i]['P'].'</td>';
           echo '<td>'.$pressure['pressure'][$i]['Pa'].'</td>';
           echo '<td>'.$other_weather_data['other_weather_data'][$i]['U'].'</td>';
           echo '<td>'.$wind['wind'][$i]['DD'].'</td>';
           echo '<td>'.$wind['wind'][$i]['Ff'].'</td>';
           echo '<td>'.$wind['wind'][$i]['ff10'].'</td>';
           echo '<td>'.$wind['wind'][$i]['ff3'].'</td>';
           echo '<td>'.$clouds['clouds'][$i]['N'].'</td>';
           echo '<td>'.$weather['weather'][$i]['WW'].'</td>';
           echo '<td>'.$weather['weather'][$i]['W1'].'</td>';
           echo '<td>'.$weather['weather'][$i]['W2'].'</td>';
           echo '<td>'.$temperature['temperature'][$i]['Tn'].'</td>';
           echo '<td>'.$temperature['temperature'][$i]['Tx'].'</td>';
           echo '<td>'.$clouds['clouds'][$i]['Cl'].'</td>';
           echo '<td>'.$clouds['clouds'][$i]['Nh'].'</td>';
           echo '<td>'.$clouds['clouds'][$i]['H'].'</td>';
           echo '<td>'.$clouds['clouds'][$i]['Cm'].'</td>';
           echo '<td>'.$clouds['clouds'][$i]['Ch'].'</td>';
           echo '<td>'.$other_weather_data['other_weather_data'][$i]['VV'].'</td>';
           echo '<td>'.$temperature['temperature'][$i]['Td'].'</td>';
           echo '<td>'.$other_weather_data['other_weather_data'][$i]['RRR'].'</td>';
           echo '<td>'.$other_weather_data['other_weather_data'][$i]['Tr'].'</td>';
           echo '<td>'.$other_weather_data['other_weather_data'][$i]['E'].'</td>';
           echo '<td>'.$temperature['temperature'][$i]['Tg'].'</td>';
           echo '<td>'.$other_weather_data['other_weather_data'][$i]['E_'].'</td>';
           echo '<td>'.$other_weather_data['other_weather_data'][$i]['sss'].'</td>';
           echo '</tr>' ;
       }
?>
                        <tr></tr>
                </tbody>
            </table>

        </main>
<?php } ?>

<?php else: ?>
        <link rel="stylesheet" href="./vendor/bootstrap/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css">
        <form class="form-signin ajax" method="post" action="./ajax.php">
            <fieldset>
                <div class="main-error alert alert-error hide"></div>

                <legend>Пожалуйста, войдите в систему</legend>
                <div class="form-group">
                    <label class="col-md-4 control-label" for="login">Логин</label>
                    <div class="col-md-4">
                        <input name="username" type="text" class="input-block-level" placeholder="Ваш логин" autofocus>
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-md-4 control-label" for="password">Пароль</label>
                    <div class="col-md-4">
                        <input name="password" type="password" class="input-block-level" placeholder="Ваш пароль">
                    </div>
                </div>

                <div class="form-group">
                    <label class="col-md-4 control-label"></label>
                    <div class="col-md-4">
                        <div class="checkbox">
                            <label>
                                <input name="remember-me" type="checkbox" value="remember-me" checked>Запомнить меня
                            </label>
                        </div>
                    </div>
                </div>
                <input type="hidden" name="act" value="login">
                <div class="form-group">
                    <label class="col-md-4 control-label" for="submit"></label>
                    <div class="col-md-4">
                        <button class="btn btn-success" type="submit">Войти</button>
                        <span>или</span>
                        <a id="authorizaton" name="authorizaton" class="btn btn-default" href="/register.php">Зарегистрироваться</a>
                    </div>
                </div>
                </div>
            </fieldset>
        </form>

<?php endif; ?>

        <script src="js/hints.js"></script>
        <script src="js/ajax-form.js"></script>
        <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

    </body>

    </html>
