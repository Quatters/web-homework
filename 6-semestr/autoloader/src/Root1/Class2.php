<?php

namespace Root1;

class Class2 {
    function get_logical_path() {
        return static::class;
    }

    function get_physical_path() {
        return __FILE__;
    }
}