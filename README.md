## Python server dockerized

In this repo, we will learn how to create simple python functionality exposed via REST API and containerized using docker.  

We are using FAST API and docker basics, and focus is to create a running example of docker containerized python codebase serving rest api calls.  

#### Steps 

###### Local run
* Create python virtual environment `python3 -m venv .venv`  
* Activate the virtual environment `source .venv/bin/activate`. This will update PATH env var to use python and pip from virtual environment, so dependencies are downloaded to virtual environment.  
* `pip install -r requirements.txt`  

###### Docker 
* Create docker image `docker build -t py-docker-server-img .`  
* Optionally push image to docker hub ``  
* Run docker image as docker container `docker run -p 8000:8000 --name py-docker-server-container py-docker-server-img`  
You will see a server response as shown below from logs :   
```
> docker run -p 8000:8000 --name py-docker-server-container py-docker-server-img
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     192.168.65.1:36080 - "GET / HTTP/1.1" 200 OK
INFO:     192.168.65.1:36081 - "GET /greet HTTP/1.1" 200 OK
```