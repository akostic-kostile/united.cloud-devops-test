## Question:

2. Create simple Python script which will fetch current IP geoip info from http://www.geoplugin.net/json.gp?ip=<current_ip> API and store it into SQLite database along with all geoip info that is available through API. Each record needs to be timestamped. Script has to loop and fetch results every minute. You have to use requests library in your script. You may not install requests as python global package. Script should be PEP8 compliant (or rather pass pylint check with flying colors)

3. Package the said script into Docker container and ensure that script runs when container is started and that sqlite database is created on host machine (not inside the container). Bonus points for doing this with smallest possible docker image.

## Solution:
