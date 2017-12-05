#### flaskAPI.py must be in ./code/ directory


#### Creating container (flask:0.1 can be chainged to anything):
  docker build -t flask:0.1 .
  
#### Running container:
  docker run -p 5000:5000 flask:0.1
