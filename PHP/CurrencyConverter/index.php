<?php 
	require 'CurrencyConverterInterface.php';
	require 'CurrencyConverter.php';

	$converter = new CurrencyConverter;

	// Enter the unit to be converted as the first item of the list
	// Enter the unit to convert to as the second item of the list
	// Enter the value as the third item of the list
	
	$results = $converter->convert([
		['USD', 'INR', 75.00], 
		['INR', 'USD', 4500.00]
	]);

	$count = 0;
	foreach($results as $res){
		$count++;
		echo "Conversion $count = $res <br>";
	}
?>
