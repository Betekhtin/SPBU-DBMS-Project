<?
function registrationCorrect() {
	if ($_POST['login'] == "") return false; //не пусто ли поле логина
	if ($_POST['password'] == "") return false; //не пусто ли поле пароля
	if ($_POST['mail'] == "") return false; //не пусто ли поле e-mail
	if (!preg_match('/^([a-zA-Z0-9])(\w|-|_)+([a-z0-9])$/is', $_POST['login'])) return false; // соответствует ли логин регулярному выражению
	if (strlen($_POST['password']) < 8) return false; //не меньше ли 5 символов длина пароля
	$rez = mysql_query("SELECT * FROM users WHERE login=$login");
	if (@mysql_num_rows($rez) != 0) return false; // проверка на существование в БД такого же логина
	return true;
}//если выполнение функции дошло до этого места, возвращаем true }

function mysql_insert($table, $inserts) {
    $values = array_map('mysql_real_escape_string', array_values($inserts));
    $keys = array_keys($inserts);

    return mysql_query('INSERT INTO `'.$table.'` (`'.implode('`,`', $keys).'`) VALUES (\''.implode('\',\'', $values).'\')');
}

?>
