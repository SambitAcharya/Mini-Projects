<?php

header('Content-type: image/png');

require_once 'vendor/autoload.php';

if (isset($_GET['text'])) {
	
	$size = isset($_GET['size']) ? $_GET['size']:200;
	$padding = isset($_GET['padding']) ? $_GET['padding']:10;
	$text = $_GET['text'];

	$qr = new Endroid\QrCode\QrCode();

	$qr->setText($text);
	$qr->setSize(200);
	$qr->setPadding(10);

	$qr->render();
}

?>