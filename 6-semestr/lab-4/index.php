<?php

function print_messages($messages) {
    foreach ($messages as $message) {
        echo "<p class=\"message\">$message</p>";
    }
}

function handle_user($user) {
    if (!file_exists("users/$user.json")) {
        file_put_contents("users/$user.json", json_encode([]));
    }

    $content = json_decode(file_get_contents("users/$user.json"), true);
    
    $message = $_POST['message'];
    if (isset($message) && $message !== '') {
        $content[] = $message;
        file_put_contents("users/$user.json", json_encode($content));
    }

    echo "<p>Пользователь \"$user\":</p>";
    print_messages($content);
}

$login = $_POST['login'];
$password = $_POST['password'];

if (!isset($login) || $login === '' || $login === 'default') {
    handle_user('default');
}
elseif (isset($login)) {
    $users = json_decode(file_get_contents('auth.json'), true);
    $actual_password = $users[$login];

    if (!isset($actual_password)) {
        echo "Создан пользователь \"$login\"";
        $users[$login] = $password;
        file_put_contents('auth.json', json_encode($users));
        handle_user($login);
    }
    elseif ($password === $actual_password) {
        handle_user($login);
    }
    else {
        echo "Неверный пароль";
    }
}

?>

<form action="/" method="post">
    <div>
        <label>
            Логин
            <input type="text" name="login" placeholder="default" id="login" onclick="resetInput">
        </label>
    </div>
    <div>
        <label>
            Пароль
            <input type="text" name="password" placeholder="default" id="password" onclick="resetInput">
        </label>
    </div>
    <div>
        <label>
            Сообщение
            <input type="text" name="message" id="message" onclick="resetInput">
        </label>
    </div>
    <button>Отправить</button>
</form>

<style>
    .message {
        border-bottom: 1px solid gray;
    }
</style>