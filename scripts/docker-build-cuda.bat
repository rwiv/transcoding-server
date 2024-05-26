cd ..

docker rmi chat-server
docker build -t transcoding-server:latest -f ./Dockerfile-cuda .
pause
