FROM ubuntu:20.04
MAINTAINER bean3oup
RUN apt update
RUN apt install xinetd -y
RUN useradd -mU bean3oup
COPY ./pwn_nc /etc/xinetd.d/pwn
COPY ./nc /home/bean3oup/nc
RUN chmod 4750 /home/bean3oup /home/bean3oup/nc
RUN chown -R bean3oup:bean3oup /home/bean3oup
CMD ["/usr/sbin/xinetd","-dontfork"]
