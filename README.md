`docker run --name proxy-balancer -p 1081:1081 -p 1081:1081/udp -p 80:80 -v /home/chu/nginx/nginx.conf:/etc/nginx/nginx.conf:ro -v /home/chu/nginx/upstream.conf:/etc/nginx/upstream.conf:ro -d nginx`
