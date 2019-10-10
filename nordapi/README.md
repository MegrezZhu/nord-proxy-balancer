# NordVPN API example

This is just a very simple Python based example of the calls you can make to the NordVPN client api and the data you can obtain. I'm not a programmer and know nothing about Python, this code just shows what is possible rather than making any attempt to be useful. It simply calls the api and dumps the JSON back to the command line(the config.zip file is dumped in the current directory).

The calls in this program are -

```sh
-u, --userdata     -  -u my@email mypassword  - gives account details                                           
-l, --serverload   -  -l au1.nordvpn.com      - shows server load as percentage                                  
-s, --serverstats  -  -s - lists server load for all servers                        
-d, --serverdetail -  -d - lists detailed information about all servers                                          
-c, --config       -  -c - downloads OpenVPN config files for all servers to config.zip                           
-a, --address      -  -a - displays users IP address                                    
-n, --nameserver   -  -n - displays NordVPN nameservers    
```
The calls are all very simple, the request for account details requires a token to be validated by hashing a user password, and hashing again with a key.

The information for this is available from the debug logs in the Windows client - it's public knowledge. Hopefully people can do interesting things with this api information, for instance producing an open source Linux client with live server details like the Windows version.