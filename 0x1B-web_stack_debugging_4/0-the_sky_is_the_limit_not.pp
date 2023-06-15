# Increases the amount of traffic an Nginx server can handle.

# Update the ULIMIT value in /etc/default/nginx
exec { 'update-nginx-ulimit':
  command => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  path    => '/bin:/usr/bin',
}

# Restart Nginx after updating the ULIMIT
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Exec['update-nginx-ulimit'],
}
