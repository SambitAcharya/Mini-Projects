<?php 

interface CurrencyConverterInterface{
	public function convert(array $conversions);
	public function getCurrencies();
}

?>