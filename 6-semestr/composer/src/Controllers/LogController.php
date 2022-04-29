<?php 

namespace Controllers;

require_once dirname(__DIR__, 2) . '/vendor/autoload.php';

use Controllers\BaseController;
use Models\Logger;

class LogController extends BaseController {
    public function get($params) {
        $log = new Logger();
        echo $this->render(['data' => $log->get_data()]);
    }
}