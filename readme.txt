install
pip install fastapi uvicorn sqlalchemy

#build image
docker build -t fastapi-crud-app-v2 .


#run image
docker run -p 8000:8000 fastapi-crud-app-v2

#running images
docker ps

#all images 
docker ps -a

#Check Network Bindings
docker inspect <container_id>

#Access the Container Shell
docker exec -it <container_id> /bin/sh
curl http://localhost:8000

#stop Container
docker stop <container_id>
docker stop <container_name>

#stop all running container
docker stop $(docker ps -q)




