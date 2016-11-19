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
    <main class="center-block">

        <form class="form-horizontal" action="historyQuery.php">
            <fieldset>
                <legend>Weather history</legend>
                <div class="form-group">
                    <label class="col-md-4 control-label" for="country">Country</label>
                    <div class="col-md-4">

                        <select id="country" name="country" class="form-control">
                          <option disabled selected value> ----------- </option>

                        </select>

                    </div>
                </div>

                <div class="form-group">
                    <label class="col-md-4 control-label" for="city">City</label>
                    <div class="col-md-4">
                        <select id="city" name="city" class="form-control" disabled>
                          <option disabled selected value> ----------- </option>
                        </select>
                    </div>
                </div>

                <div class="form-group">
                    <label class="col-md-4 control-label" for="date_from">From</label>
                    <div class="col-md-4">
                        <input type="date" id="date_from" name="date_from" class="form-control" required></input>
                    </div>
                </div>

                <div class="form-group">
                    <label class="col-md-4 control-label" for="date_to">To</label>
                    <div class="col-md-4">
                        <input type="date" id="date_from" name="date_from" class="form-control" required></input>
                    </div>
                </div>

                <div class="form-group">
                    <label class="col-md-4 control-label" for="submit"></label>
                    <div class="col-md-4">
                        <button id="submit" name="submit" class="btn btn-success">Show history</button>
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
