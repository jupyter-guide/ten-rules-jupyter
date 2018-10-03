FROM ubuntu:16.04
MAINTAINER Niema Moshiri <niemamoshiri@gmail.com>
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -yq --no-install-recommends python3 python3-pip
RUN pip3 install jupyter
RUN pip3 install -r requirements.txt
