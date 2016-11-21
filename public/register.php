<?php

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
        <title>Регистрация | The weather service</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="styles/style.css">
        <link rel="stylesheet" href="./vendor/bootstrap/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css">
    </head>

    <body>
        <?php if (Auth\User::isAuthorized()): ?>

        <h1>Вы уже авторизованы</h1>

        <form class="ajax" method="post" action="./ajax.php">
            <input type="hidden" name="act" value="logout">
            <div class="form-actions">
                <button class="btn btn-large btn-primary" type="submit">Выйти</button>
            </div>
        </form>

        <?php else: ?>

        <form class="form-signin ajax" method="post" action="./ajax.php">
            <fieldset>
                <div class="main-error alert alert-error hide"></div>

                <legend>Регистрация</legend>
                <div class="form-group">
                    <label class="col-md-4 control-label" for="login">Логин</label>
                    <div class="col-md-4">
                        <input name="username" type="text" class="input-block-level" placeholder="Ваш логин" autofocus>
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-md-4 control-label" for="password">Пароль</label>
                    <div class="col-md-4">
                        <input name="password1" type="password" class="input-block-level" placeholder="Ваш пароль">
                    </div>
                </div>

                <div class="form-group">
                    <label class="col-md-4 control-label" for="password">Подтверждение пароля</label>
                    <div class="col-md-4">
                        <input name="password2" type="password" class="input-block-level" placeholder="Пожалуйста, введите пароль повторно">
                    </div>
                </div>
                <input type="hidden" name="act" value="register">

                <div class="form-group">
                    <label class="col-md-4 control-label" for="submit"></label>
                    <div class="col-md-4">
                        <button class="btn btn-success" type="submit">Зарегистрироваться</button>
                        <span>или</span>
                        <a id="authorizaton" name="authorizaton" class="btn btn-default" href="/index.php">Войти</a>
                    </div>
                </div>
                </div>
            </fieldset>
        </form>
        <?php endif; ?>

        <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
        <script src="./js/ajax-form.js"></script>

    </body>

    </html>
