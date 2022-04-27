<?php

spl_autoload_register(function ($class_name) {
    $prefix = 'src/';
    $filePath = str_replace('\\', '/', $class_name) . '.php';

    require_once dirname(__DIR__ ) . '/' . $prefix . $filePath;
});

use Class1;
use Root1\Class1 as Level1Class1;
use Root1\Class2 as Level1Class2;
use Root1\Subroot1\Class1 as Level2Class1;
use Root1\Subroot1\Class2 as Level2Class2;
use Root2\Subroot1\SubSubroot1\Class1 as Level3Class1;

$objects = [new Class1(), new Level1Class1(), new Level1Class2(), 
    new Level2Class1(), new Level2Class2(), new Level3Class1()];

echo '<table border="1" cellpadding="7">';

echo '<tr>';
echo '<th>Logical path</th>';
echo '<th>Physical path</th>';
echo '</tr>';

foreach ($objects as $obj) {
    echo '<tr>';
    echo "<td>{$obj->get_logical_path()}</td>";
    echo "<td>{$obj->get_physical_path()}</td>";
    echo '</tr>';
}

echo '</table>';