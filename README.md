## united.cloud-devops-test

For the purpose of these interview questions let's assume OS is Ubuntu Server 22.04 LTS x64. You will need GIT repo for these so I suggest you create gitlab.com or github.com private repo and commit all your work there, you can share this repo with sibin.arsenijevic@united.cloud, vladimir.rusovac@united.cloud and boris.petrovic@united.cloud just be sure to add us as developers on gitlab as it allows us to view source code. 

Each of these tasks should be done on a separate branch and later merged into master.

1. If we assume running some of the services causes "Too many open files" errors in logs write Ansible (preferred) or Puppet or Chef "playbook" which sets this limit to the higher value.

2. Create simple Python script which will fetch current IP geoip info from http://www.geoplugin.net/json.gp?ip=<current_ip> API and store it into SQLite database along with all geoip info that is available through API. Each record needs to be timestamped. Script has to loop and fetch results every minute. You have to use requests library in your script. You may not install requests as python global package. Script should be PEP8 compliant (or rather pass pylint check with flying colors)

3. Package the said script into Docker container and ensure that script runs when container is started and that sqlite database is created on host machine (not inside the container). Bonus points for doing this with smallest possible docker image.

4. Given that you have complex time-critical high-traffic bare-metal java-powered infrastructure and also lighter virtualized services (cmdb, jenkins, nexus, gitlab, etc) describe your vision for monitoring, provisioning, de-provisioning, back-up-ing, hypervisor-ing, log collecting? This question is aimed more at technologies / products that you would use so giving a list of technologies and brief reason for them (1 or 2 sentences per tech is enough). (there is no "right" answer)

5. At 4 a.m. Friday night you get a call from NOC member that one of the servers on one of the locations is reported as down and that he has tried to ssh over public network to it but it just times out. Since this is one of the "more important" servers you have to check it yourself. You know that there are other servers at the same location and that they are all interconnected through a switch in a "private" network which you can access. SSH is not bound to any interface. What would be your troubleshooting steps? Explain what are you checking and why. Try to come up with the most elaborate "fail scenario". (there is no "right" answer)

6. (Bonus Question) Looking at the graphs of your monitoring solution one of your high-traffic servers has few of the cores on 100% and others running fairly low at 20%. Looking at top/htop output this load is not coming from "userland". What would your troubleshooting steps be? (there is no "right" answer)

## Solutions:
