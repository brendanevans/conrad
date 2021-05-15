docker stop "conrad"
docker build -t conrad .
docker run --rm -it --name "conrad" -v=$(pwd):/conrad conrad