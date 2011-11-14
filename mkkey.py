#!/usr/bin/env python

import boto
import os

HOME = getenv('HOME')

ec2 = boto.connect_ec2()

key_pair = ec2.create_key_pair('auto-2')  
key_pair.save(os.path.join(HOME, '.ssh'))

