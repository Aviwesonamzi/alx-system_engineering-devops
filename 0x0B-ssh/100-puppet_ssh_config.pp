# Puppet manifest to configure SSH client to use specific private key and refuse password authentication

# Ensure the 'IdentityFile' configuration is set
file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => '  IdentityFile ~/.ssh/school',
  match => '^  IdentityFile',
}

# Ensure password authentication is refused
file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',
  line  => '  PasswordAuthentication no',
  match => '^  PasswordAuthentication',
}
