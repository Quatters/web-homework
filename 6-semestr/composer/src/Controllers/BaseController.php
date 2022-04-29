<?php

namespace Controllers;

use Twig\Loader\FilesystemLoader;
use Twig\Environment;

abstract class BaseController {
    protected $view;
    protected $twig;

    public function __construct() {
        $unqualified_classname = (new \ReflectionClass($this))->getShortName();
        $this->view = strtolower(str_replace('Controller', '.html.twig', $unqualified_classname));

        $loader = new FilesystemLoader(dirname(__DIR__, 2) . '/views');
        $this->twig = new Environment($loader);
    }

    public function get($params) {
        echo $this->render();
    }

    protected function render($view_params = []) {
        return $this->twig->render($this->view, $view_params);
    }
}