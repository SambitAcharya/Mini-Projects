<?php 
	class CurrencyConverter implements CurrencyConverterInterface
	{
		
		// Variables

		protected $currencyURL = 'http://www.freecurrencyconverterapi.com/api/v2';

		protected $convertEndPoint = 'convert?q=%s&compact=y';
		
		protected $currenciesEndPoint = 'currencies';

		//Functions
		
		public function convert(array $conversions){
			
			$currencies = [];
			$results = [];

			$currencies = array_map(function($c){
				return "{$c[0]}_{$c[1]}";
			}, $conversions);

			$query = implode(',', array_unique($currencies));

			// Build Up URL
			$convertEndPoint = sprintf($this->convertEndPoint, $query);
			$url = "{$this->currencyURL}/{$convertEndPoint}";
		
			// Get response
			$response = json_decode($this->curlRequest($url), true);

			// Build up results
			foreach($conversions as $c){
				$key = "$c[0]_$c[1]";
				$results[] = isset($response[$key]) ? $response[$key]['val'] * $c[2]: null;
			}

			return $results;
		}

		public function getCurrencies(){
			$url = "{$this->currencyURL}/{$this->currenciesEndPoint}";
		
			return json_decode($this->curlRequest($url), true)['results'];
		}

		protected function curlRequest($url){
			$curl = curl_init();
			curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
			curl_setopt($curl, CURLOPT_URL,$url);
		
			return curl_exec($curl);
		}
	}
?>