<?php
include 'var.inc';
include 'dbopen.inc';

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

///////////////////////////////////////////////////////////


$HTTP_GET_VARS;

$i1=htmlspecialchars($_GET["i1"]);
$f1=htmlspecialchars($_GET["f1"]);

echo 'i1=' . $i1 . ' f1=' . $f1;

if (empty($i1) or  empty($f1)) {
    echo "<br> empty<br>";
  } else {
    $sql = "INSERT INTO T1 (i1, f1) VALUES (" . $i1 . ", " .  $f1 . ")";
    if ($conn->query($sql) === TRUE) {
        echo "New record created successfully"  ;
      } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}


include 'dbclose.inc';
?>
