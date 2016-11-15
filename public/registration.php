<?
ini_set ("session.use_trans_sid", true);
session_start();
include ('../lib/connect.php'); //подключаемся к БД
include ('../lib/function_global.php');

//проверим, быть может пользователь уже авторизирован. Если это так, перенаправим его на главную страницу сайта
//if (isset($_SESSION['id']) || (isset($_COOKIE['login']) && isset($_COOKIE['password'])))
//{
//	header('Location: http://localhost');
//}
//else
//{
	if (isset($_POST['submit'])) //если была нажата кнопка регистрации, проверим данные на корректность и, если данные введены и введены правильно, добавим запись с новым пользователем в БД
	{
		$correct = true;//registrationCorrect(); //записываем в переменную результат работы функции registrationCorrect(), которая возвращает true, если введённые данные верны и false в противном случае
		if ($correct) //если данные верны, запишем их в базу данных
		{
			$login = htmlspecialchars($_POST['login']);
			$password = $_POST['password'];
			$mail = htmlspecialchars($_POST['email']);
			$salt = mt_rand(100, 999);
			$tm = time();
			$password = md5(md5($password).$salt);
      $city_id='1';
			if (mysql_query("INSERT INTO user (city_id,login,password,salt,mail_reg,mail,reg_date,last_act) VALUES ('".$city_id."','".$login."','".$password."','".$salt."','".$mail."','".$mail."','".$tm."','".$tm."')")) //пишем данные в БД и авторизовываем пользователя
			{
				setcookie ("login", $login, time() + 50000, '/');
				setcookie ("password", md5($login.$password), time() + 50000, '/');
				$rez = mysql_query("SELECT * FROM users WHERE login=".$login);
				@$row = mysql_fetch_assoc($rez);
				$_SESSION['id'] = $row['id'];
				$regged = true;
				include ("index.html"); //подключаем шаблон
			}
      else include("history.php");
		}
		else
		{
			include_once ("registration.html"); //подключаем шаблон в случае некорректности данных
		}
	}
//	else
//	{
		//include_once ("registration.html"); //подключаем шаблон в случае если кнопка регистрации нажата не была, то есть, пользователь только перешёл на страницу регистрации
//	}
//}
?>
