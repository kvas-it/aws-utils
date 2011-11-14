#!/usr/bin/env python

import boto
import os
import sys

HOME = os.getenv('HOME')
ssh_dir = os.path.join(HOME, '.ssh')

ec2 = boto.connect_ec2()
print """Connected to EC2

I will now create a key pair for you.
Enter desired name of the key-pair, please"""

kp_name = sys.stdin.readline().strip()

print """Will create a keypair named "%s" and save it in "%s".
Press ENTER to continue.""" % (kp_name, ssh_dir)
sys.stdin.readline()

key_pair = ec2.create_key_pair(kp_name)  
key_pair.save(ssh_dir)

