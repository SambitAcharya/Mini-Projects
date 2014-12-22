<?php 
	class Shortener{

		protected $db;

		public function __construct(){
			// For demo purposes
			$this->db = new mysqli('localhost','root','','website');
		}

		protected function generateCode($num){
			return base_convert($num, 10, 36);
		}

		public function makeCode($url){
			
			$url = trim($url);

			if(!filter_var($url, FILTER_VALIDATE_URL))
				return '';

			$url = $this->db->escape_string($url);

			// Check if URL already exists
			$exists = $this->db->query("SELECT code FROM links WHERE url = '{$url}'");
			
			if($exists->num_rows)
				return $exists->fetch_object()->code;
		    else {
				
				// Insert record without a code
				$this->db->query("INSERT INTO links ( url,created ) VALUES ( '{$url}',NOW() ) ");
			
				// Generate code based on inserted ID
				$code = $this->generateCode($this->db->insert_id);
			
				// Update the record with the generated code
				$this->db->query("UPDATE links SET code = '{$code}' WHERE url = '{$url}'");

				return $code;
			}
		}

		public function getURL($code){

			$code = $this->db->escape_string($code);
			$code = $this->db->query("SELECT url FROM links WHERE code = '$code'");
		
			if($code->num_rows){
				return $code->fetch_object()->url;
			}

			return '';
		}
	}
?>