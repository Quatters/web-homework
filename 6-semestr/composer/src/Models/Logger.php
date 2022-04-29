<?php

namespace Models;

require_once dirname(__DIR__, 2) . '/vendor/autoload.php';

use Monolog\Logger as MonologLogger;
use Monolog\Handler\StreamHandler;

class Logger {
    private $log;
    private $log_path;

    public function __construct() {
        $this->log = new MonologLogger("Log");
        $this->log_path = dirname(__DIR__, 2) . '/.log';
        $this->log->pushHandler(new StreamHandler($this->log_path), MonologLogger::INFO);
    }

    public function get_data() {
        $content = file_get_contents($this->log_path);
        return explode("\n", $content);
    }
    
    public function info($data) {
        $this->log->info($data);
    }

    public function notice($data) {
        $this->log->notice($data);
    }
}