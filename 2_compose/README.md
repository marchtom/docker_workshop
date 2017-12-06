### Docker-compose

#### python flask + redis db


Files must be in the same directory. 
To start containers:
  > docker-compose up
  
###### 0.0.0.0:5000/ :
Counts how many times main page was visited  

###### 0.0.0.0:5000/w/txt :
Returns json {'txt': txt}

###### 0.0.0.0:5000/post/key/val :
Adds key:val to redis database

###### 0.0.0.0:5000/key :
Returns key:val from db as json
