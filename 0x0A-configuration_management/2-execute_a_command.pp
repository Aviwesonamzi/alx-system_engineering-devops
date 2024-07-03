# 2-execute_a_command.pp
# This Puppet manifest kills a process named killmenow using pkill

exec { 'kill_killmenow':
  command => '/usr/bin/pkill -f killmenow',
  onlyif  => '/bin/pgrep -f killmenow',
}

