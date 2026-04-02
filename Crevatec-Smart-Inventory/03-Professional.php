<?php
/**
*************************************************************************
* PROJECT: Crevatec Smart Inventory
* LEVEL: 03-Professional (L2 UI + SQL Database Persistence)
* POWERED BY CREVATEC | DEVELOPED BY OLAKUNLE SUNDAY OLALEKAN
* COLOR THEME: Industrial Navy (#2C3E50)
* STATUS: Adjusted for Enterprise Reliability.
*************************************************************************
**/

// 1. SECURE CONNECTION LOGIC
$db = new mysqli("localhost", "root", "", "crevatec_inventory");

if ($db->connect_error) {
    die("<div style='color:red; padding:20px;'>Crevatec System Error: Connection Failed. Please ensure MySQL is running.</div>");
}

// 2. RE-IMPLEMENTED LOGIC: Server-Side processing
$message = "";
if(isset($_POST['add'])) {
    $n = $_POST['name']; 
    $q = $_POST['qty']; 
    $p = $_POST['price'];
    $val = $q * $p; 
    
    // SQL Security Layer: Changed 'name' to 'item_name' to match your database
    $stmt = $db->prepare("INSERT INTO stock (item_name, qty, price, total_val) VALUES (?, ?, ?, ?)");
    $stmt->bind_param("sidd", $n, $q, $p, $val);
    
    if($stmt->execute()) {
        // Redirect to prevent duplicate form submission on refresh
        header("Location: " . $_SERVER['PHP_SELF'] . "?status=success&item=" . urlencode($n));
        exit();
    } else {
        $message = "<p style='color: red;'>Error: " . $stmt->error . "</p>";
    }
    $stmt->close();
}

// Success message handling after redirect
if(isset($_GET['status']) && $_GET['status'] == 'success') {
    $item = htmlspecialchars($_GET['item']);
    $message = "<p style='color: #27AE60; font-weight: bold;'>✔ Sync Successful: $item added to Enterprise Database.</p>";
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Crevatec Pro | Enterprise Inventory</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #f4f7f6; color: #2C3E50; padding: 40px; }
        .container { max-width: 900px; margin: auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
        .header-bar { background: #2C3E50; color: white; padding: 20px; border-radius: 8px 8px 0 0; margin: -30px -30px 20px -30px; }
        input { padding: 12px; margin: 5px 0; border: 1px solid #ccc; border-radius: 4px; width: 100%; box-sizing: border-box; }
        button { background: #e67e22; color: white; border: none; padding: 15px; width: 100%; cursor: pointer; font-weight: bold; border-radius: 4px; transition: 0.3s; }
        button:hover { background: #d35400; }
        table { width: 100%; border-collapse: collapse; margin-top: 30px; }
        th, td { padding: 12px; text-align: left; border-bottom: 1px solid #eee; }
        th { background: #f8f9fa; }
    </style>
</head>
<body>

<div class="container">
    <div class="header-bar">
        <h2 style="margin:0;">Crevatec Enterprise Inventory</h2>
        <small>Professional Tier | Secure SQL Persistence</small>
    </div>

    <?php echo $message; ?>

    <form method="POST">
        <input name="name" required placeholder="Product Name">
        <input name="qty" type="number" required placeholder="Quantity">
        <input name="price" type="number" step="0.01" required placeholder="Unit Price">
        <button name="add">Sync to Crevatec Database</button>
    </form>

    <h3>Enterprise Records:</h3>
    <table>
        <thead>
            <tr>
                <th>Product</th>
                <th>Quantity</th>
                <th>Unit Price</th>
                <th>Total Value</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
            <?php 
            $res = $db->query("SELECT * FROM stock ORDER BY id DESC");
            if ($res->num_rows > 0) {
                while($row = $res->fetch_assoc()) {
                    // Changed ['name'] to ['item_name'] to match your manual DB setup
                    $name = htmlspecialchars($row['item_name'] ?? 'Unnamed');
                    echo "<tr>
                            <td>{$name}</td>
                            <td>{$row['qty']}</td>
                            <td>\$" . number_format($row['price'], 2) . "</td>
                            <td><strong>\$" . number_format($row['total_val'], 2) . "</strong></td>
                            <td style='color: #27AE60;'>Active</td>
                          </tr>";
                }
            } else {
                echo "<tr><td colspan='5' style='text-align:center;'>No records found in database.</td></tr>";
            }
            ?>
        </tbody>
    </table>
</div>

</body>
</html>