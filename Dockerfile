FROM ubuntu:20.04
MAINTAINER Wimes <dev.wimes@gmail.com>

# Avoiding user interaction with tzdata
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y apache2 # install Apache web server (Only 'yes')
RUN apt-get install -y software-properties-common # php 5.6(이전버전) 설치를 위해
RUN add-apt-repository ppa:ondrej/php # For Installing PHP 5.6
RUN apt-get update
RUN apt-get install -y php5.6

EXPOSE 8080

CMD ["apachectl", "-D", "FOREGROUND"]
