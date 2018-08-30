build:
	docker build -t dockerweb:latest .

tag:
	docker tag dockerweb mwesterhof/dockerweb

push:
	docker push mwesterhof/dockerweb

run:
	docker run -p 5000:5000 -v /var/run/docker.sock:/var/run/docker.sock dockerweb:latest
