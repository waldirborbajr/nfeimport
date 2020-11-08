# 1st Stage
#
FROM python:3.8-slim AS base

LABEL maintainer="Waldir Borba Junior <wborbajr@gmail.com>" \
      version="V0.0.1.0" \
      description="Docker Application | nfeimport:latest"

ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV TZ=America/Sao_Paulo
ENV PATH="/venv/bin:$PATH"

WORKDIR /nfeimport

# 2nd Stage
#
FROM base AS build

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
RUN /venv/bin/python -m pip install pip --upgrade
RUN /venv/bin/python -m pip install wheel --upgrade
RUN pip install --no-cache-dir -r requirements.txt

# 3rd Stage
#
FROM base AS final

COPY . .
COPY --from=build /venv /venv
# COPY --from=builder /usr/bin/watch /usr/bin/watch
COPY --from=build /var/spool/cron /var/spool/cron
COPY --from=build /usr/bin/crontab /usr/bin/crontab
COPY --from=build /etc/localtime /etc/localtime
COPY --from=build /etc/locale.gen /etc/locale.gen
# 
COPY cronfile /root/cronfile
RUN crontab /root/cronfile
#
RUN mkdir processed
### Comment below for production
COPY --from=build /usr/bin/htop /usr/bin/htop

ENTRYPOINT ["python"]
