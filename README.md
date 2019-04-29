# ansible-role-ovftool

Ansible playbook to automate downloading and installing ovftool.

## Requirements

Ovftool can be downloaded from [here](https://www.vmware.com/support/developer/ovf/). To use this role you must 
download the ovftool zip, host it in a local repository, and set `ovf_zip_url` to the location you store it.

This role currently supports only Debian/Ubuntu distros.

## Role Variables

Note: A non-defaulted variable, download_site, must be set by a vars file
or by other mechanism prior to calling this role. The download_site must
provide a valid URL base (e.g., http://mysite.com/downloads)
from which the download files (e.g., ISO files or similar) may be obtained.
in particular, see the ovf_zip_url variable below.

```yaml
# The temporary directory to use for storing downloaded and other temporary file.
tmp_dir: "/tmp"

# The ovftool binary to download.
ovf_zip: "VMware-ovftool-4.1.0-2459827-lin.x86_64.zip"

# The MD5 hash of the binary to download.
ovf_zip_md5: "63698e602af6e24640146a6592348c99"

# The url to use for downloading the binary.
# Note: you must define the download_site in a vars file.
ovf_zip_url: "{{ download_site }}/{{ ovf_zip }}"

# The directory into which to install the downloaded ovftool binaries.
ovf_dir: "/usr/local/bin"
```

## Example playbook

```yaml
---
- hosts: ovftool
  roles:
    - ovftool

- hosts: localhost
  roles:
    - ovftool
```

# License and Copyright
 
Copyright 2015-2017 VMware, Inc.

SPDX-License-Identifier: Apache-2.0 OR GPL-3.0-only

[This code is Dual Licensed Apache-2.0 or GPLv3](LICENSE)

## Author Information

This role was created in 2015 by [Tom Hite / VMware](http://www.vmware.com/).
