<?php
require 'con.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $isbn = $_POST['isbn'];
    $title = $_POST['title'];
    $author = $_POST['author'];
    $price = $_POST['price'];

    $sql = "INSERT INTO book (isbn, title, author, price) VALUES ('$isbn', '$title', '$author', '$price')";

    if ($conn->query($sql) === TRUE) {
        header("Location: view.php"); // Redirect to index.php or another page after successful insertion
        exit();
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    $conn->close();
}
?>
1`