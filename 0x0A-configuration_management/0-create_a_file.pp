# 0-create_a_file.pp
# This Puppet manifest creates a file at /tmp/school with specific permissions, owner, group, and content

file { '/tmp/school':
  ensure  => 'file',
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}

