<?php
include 'getdata.php';
if (!empty($_COOKIE['sid'])) {
    // check session id in cookies
    session_id($_COOKIE['sid']);
}

session_start();
require_once 'classes/Auth.class.php';

?><!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=Edge">
    <title>Weather history | The weather service</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles/style.css">
    <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>

<body>
         <div class="container">

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
                    <li class="active"><a href="history.php">History</a></li>
                    <li><a href="forecast.html">Forecast</a></li>
                    <li><a href="about.php">About</a></li>
                </ul>
                <!-- Right navbar -->
                <ul class="nav navbar-nav navbar-right">
                  <form class="ajax" method="post" action="./ajax.php">
                    <input type="hidden" name="act" value="logout">
                    <div class="form-actions">
                      <button class="btn btn-large btn-success" type="submit">Logout</button>
                    </div>
                  </form>
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container-fluid -->
    </nav>
    <main>
      <div id="hint" class="normal"></div>
      <table class="table table-striped table-bordered table-hover">
        <tr class="header">
          <td class="cl_hd_fr" onmouseover="tooltip( this , 'Время в данном населённом пункте. Учитывается летнее/зимнее время' ,  'hint' )" onmouseout="hideInfo(this , 'hint')" colspan="2"><div class="brdDateLightArc forDate">Date/Time</td>
          <td id="t_archive_t" class="cl_hd" onmouseover="tooltip( this , 'Температура воздуха (градусы Цельсия) на высоте 2 метра над поверхностью земли' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">T</div></td>
          <td id="t_archive_po" class="cl_hd" onmouseover="tooltip( this , 'Атмосферное давление на уровне станции (миллиметры ртутного столба)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">Po</div></td>
          <td id="t_archive_p" class="cl_hd" onmouseover="tooltip( this , 'Атмосферное давление, приведенное к среднему уровню моря (миллиметры ртутного столба)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">P</div></td>
          <td id="t_archive_pa" class="cl_hd" onmouseover="tooltip( this , 'Барическая тенденция: изменение атмосферного давления за последние три часа (миллиметры ртутного столба)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">Pa</div></td>
          <td class="cl_hd" onmouseover="tooltip( this , 'Относительная влажность (%) на высоте 2 метра над поверхностью земли' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">U</div></td>
          <td class="cl_hd" onmouseover="tooltip( this , 'Направление ветра (румбы) на высоте 10-12 метров над земной поверхностью, осредненное за 10-минутный период, непосредственно предшествовавший сроку наблюдения' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">DD</div></td>
          <td id="t_archive_wv" class="cl_hd" onmouseover="tooltip( this , 'Cкорость ветра на высоте 10-12 метров над земной поверхностью, осредненная за 10-минутный период, непосредственно предшествовавший сроку наблюдения (метры в секунду)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">Ff</div></td>
          <td id="t_archive_wv_10" class="cl_hd" onmouseover="tooltip( this , 'Максимальное значение порыва ветра на высоте 10-12 метров над земной поверхностью за 10-минутный период, непосредственно предшествующий сроку наблюдения (метры в секунду)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">ff10</div></td>
          <td id="t_archive_wv_3" class="cl_hd" onmouseover="tooltip( this , 'Максимальное значение порыва ветра на высоте 10-12 метров над земной поверхностью за период между сроками (метры в секунду)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">ff3</div></td>
          <td class="cl_hd" onmouseover="tooltip( this , 'Общая облачность' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">N</div></td>
          <td class="cl_hd" onmouseover="tooltip( this , 'Текущая погода, сообщаемая с метеорологической станции' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">WW</div></td>
          <td class="cl_hd" onmouseover="tooltip( this , 'Прошедшая погода между сроками наблюдения 1' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">W1</div></td>
          <td class="cl_hd" onmouseover="tooltip( this , 'Прошедшая погода между сроками наблюдения 2' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">W2</div></td>
          <td id="t_archive_tn" class="cl_hd" onmouseover="tooltip( this , 'Минимальная температура воздуха (градусы Цельсия) за прошедший период (не более 12 часов)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">Tn</div></td>
          <td id="t_archive_tx" class="cl_hd" onmouseover="tooltip( this , 'Максимальная температура воздуха (градусы Цельсия) за прошедший период (не более 12 часов)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">Tx</div></td>
          <td class="cl_hd" onmouseover="tooltip( this , 'Слоисто-кучевые, слоистые, кучевые и кучево-дождевые облака' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">Cl</div></td>
          <td class="cl_hd" onmouseover="tooltip( this , 'Количество всех наблюдающихся облаков Cl или, при отсутствии облаков Cl, количество всех наблюдающихся облаков Cm' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">Nh</div></td>
          <td id="t_archive_h" class="cl_hd" onmouseover="tooltip( this , 'Высота основания самых низких облаков (м)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">H</div></td>
          <td class="cl_hd" onmouseover="tooltip( this , 'Высококучевые, высокослоистые и слоисто-дождевые облака' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">Cm</div></td>
          <td class="cl_hd" onmouseover="tooltip( this , 'Перистые, перисто-кучевые и перисто-слоистые облака' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">Ch</div></td>
          <td id="t_archive_vv" class="cl_hd" onmouseover="tooltip( this , 'Горизонтальная дальность видимости (км)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">VV</div></td>
          <td id="t_archive_td" class="cl_hd" onmouseover="tooltip( this , 'Температура точки росы на высоте 2 метра над поверхностью земли (градусы Цельсия)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">Td</div></td>
          <td id="t_archive_pr" class="cl_hd" onmouseover="tooltip( this , 'Количество выпавших осадков (миллиметры)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">RRR</div></td>
          <td class="cl_hd" onmouseover="tooltip( this , 'Период времени, за который накоплено указанное количество осадков (часы)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">tR</div></td>
          <td class="cl_hd" onmouseover="tooltip( this , 'Состояние поверхности почвы без снега или измеримого ледяного покрова' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">E</div></td>
          <td id="t_archive_tg" class="cl_hd" onmouseover="tooltip( this , 'Минимальная температура поверхности почвы за ночь. (градусы Цельсия)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">Tg</div></td>
          <td class="cl_hd" onmouseover="tooltip( this , 'Состояние поверхности почвы со снегом или измеримым ледяным покровом' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">E'</div></td>
          <td id="t_archive_sss" class="cl_hd" onmouseover="tooltip( this , 'Высота снежного покрова (см)' ,  'hint' )" onmouseout="hideInfo( this , 'hint' )"><div class="brdDateLightArc">sss</div></td>
        </tr>
        <tbody>
          <tr></tr>
        </tbody>
      </table>

    </main>
    <?php else: ?>
    <link rel="stylesheet" href="./vendor/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css">
      <form class="form-signin ajax" method="post" action="./ajax.php">
           <fieldset>
        <div class="main-error alert alert-error hide"></div>

        <legend>Please sign in</legend>
          <div class="form-group">
                      <label class="col-md-4 control-label" for="login">Login</label>
                      <div class="col-md-4">
                          <input name="username" type="text" class="input-block-level" placeholder="Username" autofocus>
                              </div>
                  </div>
           <div class="form-group">
                      <label class="col-md-4 control-label" for="password">Password</label>
                     <input name="password" type="password" class="input-block-level" placeholder="Password">
                      <div class="col-md-4">
                          </div>
                  </div>

        <div class="form-group">
                      <label class="col-md-4 control-label"></label>
                      <div class="col-md-4">
                        <div class="checkbox">
                          <label>
                            <input name="remember-me" type="checkbox" value="remember-me" checked> Remember me
                            </label>
                        </div>
                      </div>
                  </div>
        <input type="hidden" name="act" value="login">
        <div class="form-group">
                      <label class="col-md-4 control-label" for="submit"></label>
                      <div class="col-md-4">
        <button class="btn btn-success" type="submit">Sign in</button>
    <span>or</span>
          <a id="authorizaton" name="authorizaton" class="btn btn-default" href="/register.php">Create an account</a>
        </div>
     </div>
                  </div>
        </fieldset>
      </form>

      <?php endif; ?>

    </div> <!-- /container -->
    <script src="/js/hints.js"></script>
    <script src="./js/ajax-form.js"></script>
    <script type="text/javascript">

        var countries = JSON.parse('<?php echo json_encode(json_php("country")) ?>').country;
        var cities = JSON.parse('<?php echo json_encode(json_php("city")) ?>').city;

        var countryEl = $("#country");
        for (var i = 0; i < countries.length; ++i){
          countryEl.append($("<option></option>")
                   .attr("value", countries[i].country_id)
                   .text(countries[i].country_name));
        }

        var cityEl = $("#city");
        countryEl.change(function(){
          cityEl.children().each(function() {
            if (!$(this).attr("disabled")) this.remove();
          });
          cityEl.val("");
          cities.forEach(function(city) {
            if (city.country_id == countryEl.val()){
              console.log(city);
              cityEl.append($("<option></option>")
                    .attr("value", city.city_id)
                    .text(city.city_name));
            }
            cityEl.removeAttr("disabled");
          });
        });

    </script>
  </body>
</html>
