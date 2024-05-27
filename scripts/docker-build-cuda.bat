cd ..

docker rmi transcoding-server
docker build -t transcoding-server:latest -f .\docker\Dockerfile-cuda .
pause
