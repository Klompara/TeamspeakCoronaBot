# TeamspeakCoronaBot
Teamspeak 3 Query Bot which displays Covid-19 stats of Austria 

The python script connects with the "ts3" python module via telnet to the teamspeak server.
The Host, port, id of the virtual server and the credentials for the query login are in def_param.py
After login it sends a request to a coronavirus-rest-api on https://corona.lmao.ninja/countries and searches for the country data
3 channels are then edited using the data to set the channel name
repeats every 300 seconds (5 minutes)