<html>
<head>
<link rel="stylesheet" type="text/css" href="CSS/sty.css">
</head>
<body>
<div class= "fgh">
<?php 

$abc = $_POST['locationid'];
$dfg = $_POST['locationid1'];


$conn = mysqli_connect("localhost","root","","location");
	
$result = mysqli_query($conn,"SELECT * FROM locationapp");

$a= 7;
$b = 8;
$c = 6;

while ($row = mysqli_fetch_assoc($result))	
{
	if($abc == $row['Longitude'])
	{
	if($a > $b && $a > $c)	
	{
	?><img src="image/<?php echo $row['aa']; ?>" style="width:450px;
	                                                    height:400px;
														
	"> <?php
	break;
	}
	if($b > $c && $b > $a)
	{
	?><img src="image/<?php echo $row['bb']; ?>" style="width:450px;height:400px;"> <?php
	break;}
	if($c > $a && $c > $b)
	{
    ?><img src="image/<?php echo $row['cc']; ?>" style="width:450px;height:400px;"> <?php
	break;}	
	}
	}
		


?>

<h3>*Black spot is your location </h3>
<h3>*Red marked area is polluted</h3>
<h3>*Prefer green marked area</h3>






</div>
</body>
</html>