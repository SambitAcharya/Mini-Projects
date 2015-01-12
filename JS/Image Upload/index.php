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
		
		<form action="upload.php" method="post" id="myForm"
		enctype="multipart/form-data">
		<label for="file">Filename:</label>
		<input type="file" name="file" id="file"><br>
		<input type="submit" name="submit" class="btn btn-success" value="Upload Image">
		</form>

		<div class="progress progress-striped active">
		  <div class="progress-bar"  role="progressbar" aria-valuenow="0" aria-valuemin="0" 
		  aria-valuemax="100" style="width: 0%">
		    <span class="sr-only">0% Complete</span>
		  </div>
		</div>
		<div class="image"></div>
		</div>
</body>
</html>