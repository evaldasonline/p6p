<?php
include 'var.inc';
include 'dbopen.inc';

// $conn = mysqli_connect(host_db, user_db, pass_db, name_db);

///////////////////////////////////////////////////////////


$sql = "SELECT id, i1, f1  FROM T1" ;

$result = mysqli_query($conn, $sql);
if (mysqli_num_rows($result) > 0) {

    echo "<table><tr><td>id</td><td>integer</td><td>float</td></tr>";
    $lenta = array();
    array_push($lenta, array('id', 'i1', 'f1'));

    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "<tr><td>" . $row["id"]. " </td><td> " . $row["i1"]. " </td><td> " . $row["f1"]. "</tr>";
	array_push($lenta,  array($row['id'], $row['i1'], $row['f1']));
    }

    echo "</table>";

} else {
    echo "0 results";
}

// echo "<pre>";
// print_r($lenta);

$gra=array();
$max = sizeof($lenta);
for($x = 1; $x < $max;$x++)
{
    $gra[1][$x]= $lenta[$x][1];
    $gra[2][$x]= $lenta[$x][2];
}

// print_r($gra[1]);

$r_i1 = json_encode($gra[1]);
$r_i1 = json_encode($gra[1]);






////////////////////////////////////
include 'dbclose.inc';
?>
