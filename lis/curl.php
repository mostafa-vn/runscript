<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
<div class="container-sm">
<?php
date_default_timezone_set('Asia/tehran');
echo '<div class="container">' . "The time is " . date("h:i:sa"). '</div>';
echo "<br><br>";
echo 'Current PHP version: ' . phpversion();
echo "<br><br>";
echo 'file_get_contents : ', ini_get('allow_url_fopen') ? 'Enabled' : 'Disabled';
echo "<br><br>";
echo 'Curl: ', function_exists('curl_version') ? 'Enabled' : 'Disabled';
echo "<br><br>";
echo "Memory Limit:" . ini_get('memory_limit');
echo "<br><br>";
$v = ini_get("max_input_vars");
echo  "Max Input Vars is <b>$v</b>";
echo "<br><br>";
$r= shell_exec("php -m");
echo "<td>".$r."</td>";
?>
</div>