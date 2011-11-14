#!/usr/bin/env python

import boto

ec2 = boto.connect_ec2()

reservation = ec2.run_instances('ami-21f53948', instance_type='m1.large',
    key_name='auto-2')

for r in ec2.get_all_instances():
    if r.id == reservation.id:
        break

print r.instances[0].public_dns_name  

