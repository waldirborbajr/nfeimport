FROM python:3.8-slim

MAINTAINER Waldir Borba Junior <wborbajr@gmail.com>

# ENV LANG=en_US.UTF-8 
# ENV LANGUAGE=en_US.UTF-8
# ENV LC_ALL en_US.UTF-8
# ENV TZ America/Sao_Paulo

# ENV export DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update \
    && apt-get -y install watch nano \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV TZ=America/Sao_Paulo
RUN rm -f /etc/localtime \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata    

ENV PYTONUNBUFFERED 1

WORKDIR /nfeimport

ADD . /nfeimport

RUN pip install --no-cache-dir -r requirements.txt

# CMD ["/usr/bin/watch" "-n" "300" "/nfeimport/NFeKollector.sh"]