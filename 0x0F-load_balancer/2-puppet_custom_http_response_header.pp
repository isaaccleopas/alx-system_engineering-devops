# Installs a Nginx server with custom HTTP header

exec { 'install_nginx':
	command => '/usr/bin/apt-get update && /usr/bin/apt-get install -y nginx',
	path    => '/usr/bin',
	creates => '/usr/sbin/nginx',
}

file_line { 'enable server_tokens':
	path    => '/etc/nginx/nginx.conf',
	line    => 'server_tokens off;',
	match   => '^#.*server_tokens off;',
	replace => 'server_tokens off;',
	}

$hostname = $::hostname

file { '/etc/nginx/sites-enabled/default':
	ensure  => file,
	content => "server {\n\tadd_header X-Served-By ${hostname};",
	mode    => '0644',
	}

service { 'nginx':
	ensure => running,
	enable => true,
	}

