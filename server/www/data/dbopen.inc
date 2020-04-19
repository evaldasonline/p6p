<?php


$conn = mysqli_connect($host_db, $user_db, $pass_db, $name_db);
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
?>