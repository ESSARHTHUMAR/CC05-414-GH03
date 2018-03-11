<?php

$conn = mysqli_connect("localhost","root","","location");
	
$result = mysqli_query($conn,"SELECT * FROM locationida");

$data = array();
while ($row = mysqli_fetch_assoc($result))	
{
	$data[] = $row;
}
	
 echo json_encode($data);


?>