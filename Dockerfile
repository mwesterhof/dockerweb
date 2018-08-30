FROM alpine:latest
MAINTAINER Marco Westerhof "m.westerhof@lukkien.com"
RUN apk update
RUN apk add py-pip python-dev
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]
