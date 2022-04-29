<?php

namespace Controllers;

require_once dirname(__DIR__, 2) . '/vendor/autoload.php';

use Controllers\BaseController;
use Models\Logger;

class ErrorController extends BaseController {
    private $code; 

    public function __construct($code = null) {
        $this->code = $code;
        parent::__construct();
    }

    public function get($params) {
        $log = new Logger();
        $message = [];

        if (is_null($this->code)) {
            $message['description'] = 'Unknown error.';
            $log->notice('Somebody got unknown error');
        } 
        else {
            $message['code'] = $this->code;
            if ($this->code === 404) {
                $message['description'] = 'Page not found.';
                $log->notice('Somebody got 404 error');
            }
            else if ($this->code >= 500) {
                $message['description'] = 'Internal server error.';
                $log->notice('Somebody got 500 error');
            } 
        }

        echo $this->render($message);
    }
}