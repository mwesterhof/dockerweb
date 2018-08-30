build:
	docker build -t dockerweb:latest .

run:
	docker run -p 5000:5000 -v /var/run/docker.sock:/var/run/docker.sock dockerweb:latest
