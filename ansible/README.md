## Notes:

- Playbook is only runnable against Ubuntu 22.04 LTS x64

- There are 3 different configuration locations that can affect number of open files:
    - Limits per user set in `/etc/security/limits.conf` file. For your user you can check this with `$ ulimit -Sn` (for soft limits) and `$ ulimit -Hs` (for hard limits). `community.general.pam_limits` module changes these limits.  **`limits.conf` does nothing for systemd enabled OS (which are all of them right now?).**
    - `$ sudo sysctl fs.file-max` This is a global setting for all processes system-wide. By default this is set to 9223372036854775807 on Ubuntu 22.04, but if it was changed in your case you can increase the number by uncommenting sysctl item at the end of the `playbook.yml`
    - There is a limit imposed on the process (service) level by systemd. You can check the current limits with `$ cat /proc/$PID/limits`. The best way to increase it is to add override file to `/etc/systemd/system/$SVC-NAME.service/override.conf`. Two useful links:
    https://www.2daygeek.com/linux-modifying-existing-systemd-unit-file/
    https://www.freedesktop.org/software/systemd/man/systemd.exec.html#Process%20Properties

        **Relevant property is `LimitNOFILE=` under `[Service]`.**


## How to use it:
1. Playbook assumes that we are increasing number of open files for Nginx service (and makes sure Nginx is installed in the first place).
2. Edit inventory file by replacing `$USER` and `$HOST` with SSH user and hostname (or ip) respectively.
3. Execute the following command:
    ```
    $ ansible-playbook -i inventory playbook.yml
    ```