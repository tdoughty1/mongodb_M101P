<!DOCTYPE html>
<html>
<head>
<title>Hello World!</title>
</head>
<body>
<p>
Welcome {{username}}
<p>
<ul>
%for thing in things:
<li>{{thing}}</li>
%end
<p>
<form action="/favorite_fruit" method="POST">
What is your favorite fruit?
<input type="text" name="fruit" size="40" value=""><br>
<input type="submit" value="Submit">
</form>
</ul>
</body>
</html>

