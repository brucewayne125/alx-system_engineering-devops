#!/usr/bin/env bash
#  using Puppet to make changes to our configuration file.

file_line { 'set identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentifyFile ~/.ssh/school',
}

file_line { 'Disable passeord authen':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}
