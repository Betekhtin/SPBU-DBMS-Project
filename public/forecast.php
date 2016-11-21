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
        <title>Прогноз | The weather service</title>
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
                        <li><a href="history.php">История</a></li>
                        <li class="active"><a href="forecast.php">Прогноз</a></li>
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
        <main class="center-block">

            <form class="form-horizontal" action="historyQuery.php" method="post">
                <fieldset>
                    <legend>Прогноз</legend>
                    <div class="form-group">
                        <label class="col-md-4 control-label" for="country">Страна</label>
                        <div class="col-md-4">
                          <select id="country" name="country" class="form-control">
                            <option disabled selected value> ----------- </option>
                          </select>
                        </div>
                    </div>

                    <div class="form-group">
                        <label class="col-md-4 control-label" for="city">Город</label>
                        <div class="col-md-4">
                            <select id="city" name="city" class="form-control" disabled>
                              <option disabled selected value> ----------- </option>
                            </select>
                        </div>
                    </div>

                    <div class="form-group">
                        <label class="col-md-4 control-label" for="date_from">От</label>
                        <div class="col-md-4">
                            <input type="date" id="date_from" name="date_from" class="form-control" required></input>
                        </div>
                    </div>

                    <div class="form-group">
                        <label class="col-md-4 control-label" for="date_to">До</label>
                        <div class="col-md-4">
                            <input type="date" id="date_to" name="date_to" class="form-control" required></input>
                        </div>
                    </div>

                    <div class="form-group">
                        <label class="col-md-4 control-label" for="submit"></label>
                        <div class="col-md-4">
                            <button id="submit" name="submit" class="btn btn-success">Получить прогноз</button>
                        </div>
                    </div>

                </fieldset>
            </form>
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

            <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
            <script src="js/ajax-form.js"></script>
            <script src="js/query-form-control.js"></script>
            <script>
                var countries = JSON.parse('<?php echo json_encode(json_php("country")) ?>').country;
                var cities = JSON.parse('<?php echo json_encode(json_php("city")) ?>').city;
                var minDate = "2016-11-09";
                formControl(countries, cities, minDate, null);
            </script>

    </body>

    </html>
