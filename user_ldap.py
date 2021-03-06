#!/usr/bin/env python
##################################################################
#Created by: Alvin Aguila Sosangyo
#
#Script checks if multiple users exist on multiple ldap servers
#How to use?
# 1. Input list of servers at list_servers.txt
# 2. Input list of users at list_users.txt
# 3. Run the script
##################################################################
import subprocess

fo = open("list_server.txt", "r")
str = fo.read().split();

fo2 = open("list_user.txt", "r")
str2 = fo2.read().split();

for i in str:
	for i2 in str2:
		subprocess.call([
			"ssh", "-q", i,
			"uname -n",
			"; ",
			"ldaplist -l passwd", i2, "| grep dn"
		])
fo.close()
fo2.close()
