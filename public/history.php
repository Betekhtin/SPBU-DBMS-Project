<?
  ini_set ("session.use_trans_sid", true);
  session_start();
  include ('../lib/connect.php');
?>

<!DOCTYPE html>

<html lang="en">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=Edge">
    <title>Weather history | The weather service</title>
    <link rel="stylesheet" href="styles/style.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css">
</head>

<body>
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
                <a class="navbar-brand glyphicon glyphicon-home" href="index.html"></a>
            </div>
            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="navbar">
                <ul class="nav navbar-nav">
                    <li class="active"><a href="history.html">History</a></li>
                    <li><a href="forecast.html">Forecast</a></li>
                    <li><a href="about.html">About</a></li>
                </ul>
                <!-- Right navbar -->
                <ul class="nav navbar-nav navbar-right">
                    <a href="authorization.html" id="sign_in_btn" class="btn btn-default navbar-btn">Sign in</a>
                    <a href="registration.html" id="sign_up_btn" class="btn btn-success navbar-btn">Sign up</a>
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container-fluid -->
    </nav>
    <main class="center-block">

        <form class="form-horizontal" action="history.php">
            <fieldset>
                <legend>Weather history</legend>
                <div class="form-group">
                    <label class="col-md-4 control-label" for="country">Country</label>
                    <div class="col-md-4">
                        <select id="country" name="country" class="form-control">
                          <option value=""></option>
                          <?
                          $tmp=mysql_query("SELECT * FROM country");
                          while ($country_options = mysql_fetch_array($tmp, MYSQL_ASSOC)){
                            printf("<option value=\"%s\">%s</option>", $country_options["country_id"], $country_options["country_name"]);
                          }
                          ?>
                        </select>
                    </div>
                </div>

                <div class="form-group">
                    <label class="col-md-4 control-label" for="city">City</label>
                    <div class="col-md-4">
                        <select id="city" name="city" class="form-control">
                          <option value=""></option>
                          <option value="Moscow">Moscow</option>
                          <option value="Saint-Petersburg">Saint-Petersburg</option>
                          <script>
                          var country = $('#country');
                          country.addEventListener('change', function(){
                            var selected_id = country.value;
                            <?
                            $tmp=mysql_query("SELECT * FROM city where city.country_id= \"\"");
                            while ($country_options = mysql_fetch_array($tmp, MYSQL_ASSOC)){
                              printf("<option value=\"%s\">%s</option>", $country_options["country_id"], $country_options["country_name"]);
                            }
                            ?>
                          })
                          </script>
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
    </main>
    <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</body>

</html>
