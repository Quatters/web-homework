<?php

class Class1 {
    function get_logical_path() {
        return static::class;
    }

    function get_physical_path() {
        return __FILE__;
    }
}