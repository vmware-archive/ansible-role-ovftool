# Copyright 2015 VMware, Inc.  All rights reserved.
# SPDX-License-Identifier: Apache-2.0 OR GPL-3.0-only

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_hosts_file(File):
    f = File('/usr/bin/ovftool')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
