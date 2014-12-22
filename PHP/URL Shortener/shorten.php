<?php 
session_start();
require_once 'classes/Shortener.php';

$s = new Shortener;

if(isset($_POST['url'])){
	
	$url = $_POST['url'];

	if($code = $s->makeCode($url))
		$_SESSION['feedback'] = " Generated! Your Short URL is: <a href=\"http://localhost/MiniPHPProjects/URL%20Shortener/{$code}\">http://localhost/MiniPHPProjects/URL%20Shortener/{$code}</a> ";
	else 
		$_SESSION['feedback'] = "There was a problem. Invalid URL.";
	
}

header('Location: index.php');
?>