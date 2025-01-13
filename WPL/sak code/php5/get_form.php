<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Submitted Information</title>
</head>
<body>
    <h2>Submitted Information (GET Method)</h2>
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "GET") {
        $name = $_GET['name'];
        $email = $_GET['email'];
        $age = $_GET['age'];

        echo "<p>Name: $name</p>";
        echo "<p>Email: $email</p>";
        echo "<p>Age: $age</p>";
    } else {
        echo "<p>No form data submitted.</p>";
    }
    ?>
</body>
</html>

