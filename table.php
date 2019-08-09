<html>
<head>
    <title>HELP ME TOM CRUISE</title>
</head>
<body>
<table align="center" border="1">
<?php
    $cnx = new mysqli('localhost', 'root', '123', 'wsj');

    if ($cnx->connect_error)
        die('Connection failed: ' . $cnx->connect_error);

    $query = 'SELECT * FROM stocks';
    $cursor = $cnx->query($query);
	echo '<th> Exchange </th>';
	echo '<th> Symbol </th>';
	echo '<th> Company </th>';
	echo '<th> Volume </th>';
	echo '<th> Price </th>';
	echo '<th> Change </th>';
	echo '<br>';
    while ($row = $cursor->fetch_assoc()) {
	    

	echo '<tr>';
        echo '<td>' . $row['exchange'] . '</td><td>' . $row['symbol'] . '</td><td>'  . $row['company'] . '</td><td>' . $row['volume'] . '</td><td>' . $row['price'] . '</td><td>' . $row['chang'] . '</td>';
       echo '</tr>';
    }

    $cnx->close();
?>
</table>
</body>
</html>
