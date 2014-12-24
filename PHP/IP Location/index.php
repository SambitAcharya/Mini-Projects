<?php 
	require 'Geo.php';

	$geo = new Geo;

	$geo->request('117.203.215.201');

	$country = $geo->country;

	echo "This IP address is from $country";

?>