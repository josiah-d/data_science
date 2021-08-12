## Warmup 

Using the latitude and longitude coordinates for BART stations use
Spark to create a function that calculates the closest BART station to a
particular IP address or hostname.

Use this CSV file for the latitude longitude coordinates of BART
stations. 

<https://raw.githubusercontent.com/enjalot/bart/master/data/bart_stations.csv>

Use the Haversine formula to calculate the distance between two
latitude longitude coordinates. For more details see here.

<http://andrew.hedges.name/experiments/haversine/>

Use this service to get the coordinates of an IP address or hostname.

<http://freegeoip.net>

For example, here is how to get the coordinates of <http://github.com>

<http://freegeoip.net/csv/github.com>
