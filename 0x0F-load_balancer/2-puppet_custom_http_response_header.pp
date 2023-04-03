# Installs a Nginx server with custom HTTP header

exec { 'install_nginx':
  provider => shell,
  command  => 'sudo apt-get update && sudo apt-get install -y nginx',
  before   => Exec['enable server_tokens'],
}

exec { 'enable server_tokens':
  provider => shell,
  command  => 'sudo sed -i "/^#.*server_tokens off;/s/^#//" /etc/nginx/nginx.conf',
  before   => Exec['add_header'],
}

exec { 'add_header':
  provider    => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
  before      => Exec['restart Nginx'],
}

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
