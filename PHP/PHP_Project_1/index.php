<?php
$item_list = [];
$page_content = renderTemplate('main.php', ['items' => $items_list]);
$layout_content = renderTemplate('layout.php', ['content' => $page_content, 'title' => 'Дневник наюлюдения за погодой']);
print($layout_content);?>