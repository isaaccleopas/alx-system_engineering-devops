# Puppet Manifest: Change ULIMIT value in /etc/default/nginx and restart nginx

# Set the value of ULIMIT
file { '/etc/default/nginx':
  ensure  => file,
  content => "ULIMIT=\"4096\"\n",
}

# Notify the service to restart if the file changes
service { 'nginx':
  ensure    => running,
  require   => File['/etc/default/nginx'],
  subscribe => File['/etc/default/nginx'],
  restart   => '/usr/sbin/service nginx restart',
}
