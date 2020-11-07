# 1st Stage
#
FROM python:3.8 AS builder 

# labeling
LABEL maintainer="Waldir Borba Junior <wborbajr@gmail.com>" \
      version="V0.0.1.0" \
      description="Docker Application | nfeimport:latest"

# Always set a working directory
WORKDIR /nfeimport

# Sets utf-8 encoding for Python
ENV LANG=C.UTF-8
# Turns off writing .pyc files; superfluous on an ephemeral container.
ENV PYTHONDONTWRITEBYTECODE=1
# Seems to speed things up
ENV PYTHONUNBUFFERED=1

ENV TZ=America/Sao_Paulo

# Ensures that the python and pip executables used
# in the image will be those from our virtualenv.
ENV PATH="/venv/bin:$PATH"

RUN apt-get -y update \
    && apt-get install -y --no-install-recommends \
    watch nano locales gettext build-essential htop cron \
    && sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && dpkg-reconfigure --frontend=noninteractive locales \
    && update-locale LANG=en_US.UTF-8 \
    && rm -f /etc/localtime \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Setup the virtualenv
RUN python -m venv /venv

# Install Python deps
COPY requirements.txt .
RUN /venv/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# 2nd Stage
#
FROM python:3.8-slim AS base

# update PATH environment variable
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PATH="/venv/bin:$PATH"

WORKDIR /nfeimport

# copy only the dependencies installation from the 1st stage image
# copy in Python environment
COPY . .
COPY --from=builder /venv /venv
# COPY --from=builder /usr/bin/watch /usr/bin/watch
COPY --from=builder /var/spool/cron /var/spool/cron
COPY --from=builder /usr/bin/crontab /usr/bin/crontab
COPY --from=builder /etc/localtime /etc/localtime
COPY --from=builder /etc/locale.gen /etc/locale.gen
# 
COPY cronfile /root/cronfile
RUN crontab /root/cronfile
#
RUN mkdir processed
### Comment below for production
COPY --from=builder /usr/bin/htop /usr/bin/htop
