<?php
//require 'vendor/autoload.php';
//use ChartJs\ChartJS;

include 'main.php';
$data = [
    'labels' => ['i1','f1'],
    'datasets' => [[
        'data' => $r_i1,
        'backgroundColor' => '#f2b21a',
        'borderColor' => '#e5801d',
        'label' => 'Legend'
        ]]
];
$options = ['responsive' => false];
$attributes = ['id' => 'example', 'width' => 500, 'height' => 500];
$Line = new ChartJS('line', $data, $options, $attributes);

?><!DOCTYPE html>
<html>
  <head>
    <title>Chart.js-PHP</title>
  </head>
  <body>
    <?php
      echo $Line;
    ?>
    <script src="../js/Chart.min.js"></script>
    <script src="../js/driver.js"></script>
    <script>
      (function() {
        loadChartJsPhp();
      })();
    </script>
  </body>
</html>