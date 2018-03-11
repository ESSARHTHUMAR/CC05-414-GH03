
<?php

function what()
{
 echo $abc;
}

?>



<html>

<head>

<link rel="stylesheet" type="text/css" href="CSS/sty.css">
<link rel="icon" href="image/1-dE4F_nf8P60V2baaaOxgLQ.jpg" type="image/gif" sizes="16x16"> 
<title>Traffic Management</title>

</head>
<body>

<div class="asd">



<button onclick="getLocation()" style="margin-left:35%;
                                       margin-top:20px;">Track nearby NODE</button>
									   

									   
	


	<table>
		<tbody id="data">  </tbody>
	</table>


	<script type="text/javascript">
var copy = [];
var lala = [];
var alal = [];
 var l = 0;
  var e= 0;
var x = document.getElementById("data");

function getLocation() {
    if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(locationSuccess);
}
else{
    showError("Your browser doesn't support geolocation!");
}



}


function locationSuccess(position) {
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;


var ajax = new XMLHttpRequest();
   var method ="GET";
   var url ="data.php";
   var asynchronous = true;

ajax.open(method,url, asynchronous);

ajax.send();

ajax.onreadystatechange = function()
{
	
if(this.readyState == 4)
{
  var data = JSON.parse(this.responseText);
  console.log(data);
  
  var html = "";
  for(var a=0 ; a < data.length; a++)
  {
	  
	  var Longitude = data[a].LONGITUDE;
	  var Latitude = data[a].LATITUDE;
	 
	  lala[a] =Longitude; 
	  alal[a] = Latitude;
	  
	  var cc = Longitude - lon;
	  var ll = Latitude -lat;
	  
	  var sjo = Math.sqrt((cc*cc)+(ll*ll));
	  
	  
	  copy[a] = sjo;
  
  }
  
 
   for(var c = 0 ; c < 4;c++)
   {
	  if(copy[l] >= copy[c+1])
	  {
        
		l=c+1;
		
	  }
      else{
		  
		  l = l;

	  }
    }
	
	x.innerHTML = "                   1)Longitude: " + lala[l]  +
    "<br>                             2)Latitude: " + alal[l] ; 
	
	


}

}

}


</script>


<p style="color: BLACK;
          "><strong> Enter the value of longitude and latitude</strong></p>
<form action="action.php" target="_blank" method="POST" style="margin-left:10px;
margin-top:20px;">
  
  <input type="number" step=0.0001 name="locationid"/ >
   <input type="number" step=0.0001 name="locationid1"/ >
  
  
  <input type="submit" value="Submit">
</form>









</div>



</body>





</html>