<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Submitted Information</title>
</head>
<body>
    <h2>Submitted Information (REQUEST Method)</h2>
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST" || $_SERVER["REQUEST_METHOD"] == "GET") {
        $name = $_REQUEST['name'];
        $email = $_REQUEST['email'];
        $age = $_REQUEST['age'];

        echo "<p>Name: $name</p>";
        echo "<p>Email: $email</p>";
        echo "<p>Age: $age</p>";
    } else {
        echo "<p>No form data submitted.</p>";
    }
    ?>
</body>
</html>

