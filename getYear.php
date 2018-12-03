<?php
// Importing DBConfig.php file.
include 'DBConfig.php';

$Encoded_Host = json_encode($HostName);

// Creating connection.
 $con = mysqli_connect($HostName,$HostUser,$HostPass,$DatabaseName);

if($con -> connect_error){
        die("Connection failed: " . $con->connect_error);
}

 // Getting the received JSON into $json variable.




 // Creating SQL query and insert the record into MySQL database table.
$Sql_Query = ( "SELECT DISTINCT Year  FROM VEHICLE_SPECS_ADDITIONAL ");


$result = $con->query($Sql_Query);

if($result ->num_rows > 0){

while($row[] = $result -> fetch_assoc()){
        $item = $row;
        $json = json_encode($item);
}
 // If the record inserted successfully then show the message.
$MSG = 'Data Inserted Successfully into MySQL Database' ;

// Converting the message into JSON format.


// Echo the message.
echo $json;
 }
 else{
 //Print eror message if no results are found
 echo json_encode(array('message'=> 'No Results found.',));

 }

 mysqli_close($con);
?>
