#!/usr/bin/bash
ansible all --key-file ~/.ssh/ansible -i inventory -m ping