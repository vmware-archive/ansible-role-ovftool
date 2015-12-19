# ansible-role-ovftool

Ansible playbook to automate downloading and installing ovftool.

## Requirements

This role currently supports only Debian/Ubuntu distros.

## Role Variables

```yaml
# The temporary directory to use for storing downloaded and other temmporary file.
tmp_dir: "/tmp"

# The ovftool binary to download.
ovf_zip: "VMware-ovftool-4.1.0-2459827-lin.x86_64.zip"

# The MD5 hash of the binary to download.
ovf_zip_md5: "63698e602af6e24640146a6592348c99"

# The url to use for downloading the binary.
ovf_zip_url: "http://build-squid.eng.vmware.com/build/mts/release/bora-2459827/publish/{{ ovf_zip }}"

# The directory into which to install the downloaded ovftool binaries.
ovf_dir: "/usr/local/bin"

# The default IP protocol to use when running ovftool.
ipprotocol: "IPv4"
```

## Example playbook

```yaml
---
- hosts: ovftool
  sudo: True
  connection: local
  roles:
    - ovftool
```

# License and Copyright
 
Copyright 2015 VMware, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Author Information

This role was created in 2015 by [Tom Hite / VMware](http://www.vmware.com/).
