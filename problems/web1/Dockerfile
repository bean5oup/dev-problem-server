FROM python:3.8

# ENV
ENV user bean3oup
ENV port 8080

# SET packages
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential musl-dev gcc

# SET challenges
RUN adduser --disabled-password $user
COPY . /app
WORKDIR /app
RUN pip install flask
RUN chmod 777 /app
RUN gcc /app/flag.c -o /flag \
    && chmod 111 /flag && rm /app/flag.c

# RUN
USER $user
EXPOSE $port

ENTRYPOINT ["python"]
CMD ["app.py"]
