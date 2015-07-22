# ansible-role-ovftool

Ansible playbook to automate downloading and installing ovftool.

## Requirements

This role currently supports only Debian/Ubuntu distros.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    tmp_dir: "/tmp"

The templorary directory to use for storing downloaded and other temmporary file.


    ovf_zip: "VMware-ovftool-4.1.0-2459827-lin.x86_64.zip"

The ovftool binary to download.

    ovf_zip_md5: "63698e602af6e24640146a6592348c99"

The MD5 hash of the binary to download.

    ovf_zip_url: "http://localhost/downloads/{{ ovf_zip }}"

The url to use for downloading the binary.

    ovf_dir: "/usr/local/bin"

The directory into which to install the downloaded ovftool binaries.

## Example playbook

```
---
- hosts: supervio
  sudo: True
  connection: local
  roles:
    - ovftool
```

## License

TBD

## Author Information

This role was created in 2015 by [Tom Hite / VMware](http://www.vmware.com/).
