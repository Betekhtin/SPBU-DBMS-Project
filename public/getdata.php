<?php
function json_php($str)
{


$mysqli = new mysqli("localhost", "root", "root", "mydb");

/* check connection */
if ($mysqli->connect_errno) {
    printf("Connect failed: %s\n", $mysqli->connect_error);
    exit();
}
$query = "select * from ".$str;

$data = array(); // в этот массив запишем то, что выберем из базы

if ($ta = $mysqli->query($query)) {

    while($row = mysqli_fetch_assoc($ta)) {
                                             //$data[] = $row;
                                             $data[$str][] = $row;
                                           }

   /* free result set */
                                       
   $ta->free();
 
}

$mysqli->close();

//return json_encode($data); // и отдаём как json
return $data;
}
?>