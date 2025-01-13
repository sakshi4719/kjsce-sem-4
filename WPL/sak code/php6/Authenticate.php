<?php
session_start();

// Define your valid username and password
$valid_username = "asmi";
$valid_password = "password";

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve form data
    $entered_username = $_POST['username'];
    $entered_password = $_POST['password'];

    // Validate the entered credentials
    if ($entered_username === $valid_username && $entered_password === $valid_password) {
        // Authentication successful
        // Set session variables
        $_SESSION['username'] = $entered_username;

        // Set cookies (optional)
        // Setcookie("username", $entered_username, time() + (86400 * 30), "/"); // 86400 = 1 day

        // Redirect to welcome page
        header("Location: welcome.php");
        exit();
    } else {
        // Authentication failed
        $error = "Invalid username or password!";
    }
}
?>


