<?php

if (!empty($_COOKIE['sid'])) {
    // check session id in cookies
    session_id($_COOKIE['sid']);
}
session_start();
require_once './classes/Auth.class.php';

?><!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>PHP Ajax Registration</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles/style.css">
     <link rel="stylesheet" href="./vendor/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css">

  </head>

  <body>

    <div class="container">

      <?php if (Auth\User::isAuthorized()): ?>

      <h1>Your are already registered!</h1>

      <form class="ajax" method="post" action="./ajax.php">
          <input type="hidden" name="act" value="logout">
          <div class="form-actions">
              <button class="btn btn-large btn-primary" type="submit">Logout</button>
          </div>
      </form>

      <?php else: ?>




      <form class="form-signin ajax" method="post" action="./ajax.php">
           <fieldset>
        <div class="main-error alert alert-error hide"></div>

        <legend>Create an account</legend>
          <div class="form-group">
                <label class="col-md-4 control-label" for="login">Login</label>
                  <div class="col-md-4">
                          <input name="username" type="text" class="input-block-level" placeholder="Username" autofocus>
                      </div>
          </div>
          <div class="form-group">
                <label class="col-md-4 control-label" for="password">Password</label>
                     <input name="password1" type="password" class="input-block-level" placeholder="Password">
                      <div class="col-md-4">
                          </div>
                  </div>

          <div class="form-group">
                <label class="col-md-4 control-label" for="password">Confirm password</label>
                     <input name="password2" type="password" class="input-block-level" placeholder="Password">
                      <div class="col-md-4">
                            </div>
                        </div>
          <input type="hidden" name="act" value="register">

        <div class="form-group">
                      <label class="col-md-4 control-label" for="submit"></label>
                      <div class="col-md-4">
                          <button class="btn btn-success" type="submit">Sign ip</button>
                            <span>or</span>
                      <a id="authorizaton" name="authorizaton" class="btn btn-default" href="/index.php">Log in</a>
        </div>
      </div>
                  </div>
        </fieldset>
      </form>
      <?php endif; ?>

    </div> <!-- /container -->

   <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script src="./js/ajax-form.js"></script>

  </body>
</html>
