# This Puppet manifest installs Nginx and configures a custom HTTP response header.

# Ensure Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => File['/etc/nginx/conf.d/custom_header.conf'],
}

# Create the custom header configuration file
file { '/etc/nginx/conf.d/custom_header.conf':
  ensure  => file,
  content => template('custom_header/custom_header.conf.erb'),
  require => Package['nginx'],
}

# Ensure the Nginx configuration directory exists
file { '/etc/nginx/conf.d':
  ensure => directory,
  owner  => 'root',
  group  => 'root',
  mode   => '0755',
}
