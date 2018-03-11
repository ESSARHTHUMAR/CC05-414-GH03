<html>

<head>

</head>


<body>

<img src="image/bb1.jpg">

<?php

$conn = mysqli_connect("localhost","root","","location");
	
$result = mysqli_query($conn,"SELECT * FROM locationmapp");
$sim =72.5877;
$a = 7;
$b=  8;
$c = 6;
while ($row = mysqli_fetch_assoc($result))	
{
	if($sim == $row['Longitude'])
	{
		
	
	
	?><img src="image/<?php echo $row['aa']; ?>"> <?php
		
    
	
	
	
	}
	}
	
 

?>
</body>
</html>