#Using strace, find out why Apache is returning a 500 error. Once you findthe issue, fix it and then automate it using Puppet

file_line {'fix phpp to php':
  path    => '/var/www/html/wp-settings.php',
  line    => "define('DB_HOST', 'localhost');",
  match   => 'phpp',
  replace => 'php',
}
