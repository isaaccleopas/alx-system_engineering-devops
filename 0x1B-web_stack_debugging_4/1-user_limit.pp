# Puppet Manifest: Increase file limits for the holberton user

# Install the pam module
package { 'libpam-modules':
  ensure => installed,
}

# Change limits for the holberton user
file { '/etc/security/limits.d/holberton.conf':
  ensure  => file,
  content => "holberton hard nofile 65536\nholberton soft nofile 65536\n",
  require => Package['libpam-modules'],
}
