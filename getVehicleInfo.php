<?php
// Importing DBConfig.php file.
include 'DBConfig.php';



// Creating connection.
 $con = mysqli_connect($HostName,$HostUser,$HostPass,$DatabaseName);

 // Getting the received JSON into $json variable.
$json = file_get_contents('php://input');
 if($con -> connect_error){
        echo json_encode("Connection");
        die("Connection failed: " . $con->connect_error);
}

// decoding the received JSON and store into $obj variable.
$obj = json_decode($json,true);

//Retrieves the data from $obj (a json array) and stores the data in the variables below

$get_year = $_GET['model_year'];
$year = stripslashes($get_year);
$year= str_replace('"', '', $year);


$get_make = $_GET['model_make_id'];
$make = stripslashes($get_make);
$make = str_replace('"', '', $make);

$get_model = $_GET['model_name'];
$model = stripslashes($get_model);
$model = str_replace('"', '', $model);


$get_trim = $_GET['model_trim'];
$trim = stripslashes($get_trim);
$trim = str_replace('"', '', $trim);



 // Creating SQL query and insert the record into MySQL database table.
$Sql_Query = ( "SELECT DISTINCT * FROM VEHICLE_SPECS_ADDITIONAL WHERE  Make LIKE '$make' and Year LIKE '$year' and Model LIKE '$model' ");
$result = $con->query($Sql_Query);

if($result ->num_rows > 0){

while($row[] = $result -> fetch_assoc()){
        $item = $row;
        $json = json_encode($item);
}

echo $json;

 }
 else{
 //Print an error message if nothing is found
 echo  json_encode("No Results Found");

 }

 mysqli_close($con);
?>

