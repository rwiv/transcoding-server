cd ..

docker rmi chat-server
docker build -t transcoding-server:latest -f .\docker\Dockerfile-cuda .
pause
