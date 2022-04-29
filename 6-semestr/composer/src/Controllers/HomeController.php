<?php 

namespace Controllers;

require_once dirname(__DIR__, 2) . '/vendor/autoload.php';

use Controllers\BaseController;
use Models\Logger;

class HomeController extends BaseController {
    public function get($params) {
        if ($params && $params['name']) {
            $name = $params['name'];
            
            $log = new Logger();
            $log->info("$name has been catched");

            $this->view = 'catched.html.twig';
        }
        echo $this->render();
    }
}