<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Image Upload Progress Bar</title>
	<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
	<link rel="stylesheet" href="css/style.css">
	<script src = "https://code.jquery.com/jquery-2.1.3.min.js"></script>
	<script src = "http://malsup.github.com/jquery.form.js"></script>
	<script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>
	<script src ="js/script.js"></script>
</head>
<body>
	<div class="container-main">
		<h1>Image Uploader</h1>
		<p>Image Uploading using jquery and ajax.</p>
		
		<form action="upload.php" method="post" enctype="multipart/form-data">
	    	<label for="file">Select image to upload:</label>
	    	<input type="file" name="file" id="file"><br>
	    	<input type="submit" value="Upload Image" name="submit" class="btn btn-success">
		</form>
	</div>
</body>
</html>