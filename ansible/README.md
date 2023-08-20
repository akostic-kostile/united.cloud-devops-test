## Notes:
- This playbook uses `community.general.pam_limits` module. While the [official documentation for the module](https://docs.ansible.com/ansible/latest/collections/community/general/pam_limits_module.html) says that this collection is NOT installed as part of `ansible-core` package I received it after installing that very package.
This command will install it, if it's not already installed:
    ```
    $ ansible-galaxy collection list | grep "community.general" || ansible-galaxy collection install community.general
    ```

- Playbook is only runnable against Ubuntu 22.04 LTS x64

- There are 3 different configuration locations that can affect number of open files:
    - Limits by user, you can check this with `$ ulimit -Sn` (for soft limits) and `$ ulimit -Hs` (for hard limits). `pam_limits` module changes these limits.
    - `$ sudo sysctl fs.file-max` This is a global setting for all processes together. By default this is set to 9223372036854775807 on Ubuntu 22.04, but if it was changed in your case you can increase the number by uncommenting sysctl item at the end of the `playbook.yml`
    - There is a limit imposed on the service (process) level that might be the problem as well. This is beyond the scope of this playbook but two useful links for you to look at:
    https://www.2daygeek.com/linux-modifying-existing-systemd-unit-file/
    https://www.freedesktop.org/software/systemd/man/systemd.exec.html#Process%20Properties


## How to use it:
1. Edit inventory file by replacing `$USER` and `$HOST` with SSH user and hostname (or ip) respectively.
2. Playbook assumes that the user you're increasing the number of open files for is called `app`, if it's anything else edit the `playbook.yml` file accordingly.
3. Execute the following command:
    ```
    $ ansible-playbook -i inventory playbook.yml
    ```