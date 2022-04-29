<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$uri = explode('?', $_SERVER['REQUEST_URI']);
$path = $uri[0];

$raw_params = explode('&', $uri[1]);
$params = [];
foreach ($raw_params as $raw_param) {
    $kw = explode('=', $raw_param);
    $params[$kw[0]] = $kw[1];
}

switch ($path) {
    case '/':
        header("Location: http://{$_SERVER['HTTP_HOST']}/home");
        break;

    case '/home':
        $home_controller = new Controllers\HomeController();
        $home_controller->get($params);
        break;

    case '/log':
        $log_controller = new Controllers\LogController();
        $log_controller->get($params);
        break;

    default:
        $error_controller = new Controllers\ErrorController(404);
        $error_controller->get($params);
        break;
}