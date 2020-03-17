# TeamspeakCoronaBot
Teamspeak 3 Query Bot which displays Covid-19 stats of Austria 

The python script connects with the "ts3" python module via telnet to the teamspeak server.  
The Host, port, id of the virtual server and the credentials for the query login are in def_param.py (needs to be created)  
After login it sends a request to a coronavirus-rest-api on https://corona.lmao.ninja/countries and searches for the country data  
The REST-Api gets the data from https://www.worldometers.info/coronavirus/  
3 channels are then edited using the data to set the channel name  
repeats every 300 seconds (5 minutes)  
