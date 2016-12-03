Mandatory read this link:

https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-nginx-in-ubuntu-16-04


Setup Firewall:
sudo ufw status
sudo ufw enable or sudo ufw enable for diabling thefirewall other wise hoptimized will not work.
sudo ufw allow 'Nginx Full'


ubuntu@ip-10-10-29-108:/tmp/https/nginx$ sudo ufw status
Status: active

To                         Action      From
--                         ------      ----
Nginx Full                 ALLOW       Anywhere
22                         ALLOW       Anywhere
Nginx Full (v6)            ALLOW       Anywhere (v6)
22 (v6)                    ALLOW       Anywhere (v6)


# if you want to remove 
sudo ufw delete allow 'Nginx HTTP'


Make sure this file exists and has the nesseary nginx server configuration
/etc/nginx/sites-available/default

make sure the sym link exists like this(this is enabling the site)
lrwxrwxrwx 1 ubuntu ubuntu 34 Dec  2 23:55 default -> /etc/nginx/sites-available/default

Start or stop or restsart nginx
sudo /etc/init.d/nginx restart


Nginx logs are at /var/log/nginx and any debuggig can be done here 


