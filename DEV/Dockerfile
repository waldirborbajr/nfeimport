FROM python:3.8-slim

MAINTAINER Waldir Borba Junior <wborbajr@gmail.com>

ENV TZ=America/Sao_Paulo
ENV export DEBIAN_FRONTEND=noninteractive
ENV PYTONUNBUFFERED 1

RUN apt-get -y update \
    && apt-get -y install watch nano locales \    
    && sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && dpkg-reconfigure --frontend=noninteractive locales \
    && update-locale LANG=en_US.UTF-8 \
    && rm -f /etc/localtime \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /nfeimport

ADD . /nfeimport

RUN pip install --no-cache-dir -r requirements.txt

# CMD ["/nfeimport/NFeKollector.sh"]