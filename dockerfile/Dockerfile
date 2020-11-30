# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1st Stage
# Environment Image
#
FROM python:3.8-alpine AS base

LABEL maintainer="Waldir Borba Junior <wborbajr@gmail.com>" \
      version="V0.0.1.0" \
      description="Docker Application | nfeimport:latest"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8
ENV TZ America/Sao_Paulo
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /nfeimport

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 2nd Stage
# Compilation Image
#
FROM base AS build

RUN apk add --update --no-cache \
  tzdata \
  htop \
  apk-cron \
  bash \
  && cp /usr/share/zoneinfo/${TZ} /etc/localtime \
  && echo "${TZ}" > /etc/timezone
#   # Cleaning up
#   && apk del tzdata  \
#   && rm -rf /usr/share/zoneinfo/Africa \
#   && rm -rf /usr/share/zoneinfo/Antarctica  \
#   && rm -rf /usr/share/zoneinfo/Arctic  \
#   && rm -rf /usr/share/zoneinfo/Asia  \
#   && rm -rf /usr/share/zoneinfo/Atlantic  \
#   && rm -rf /usr/share/zoneinfo/Australia  \
#   && rm -rf /usr/share/zoneinfo/Europe   \
#   && rm -rf /usr/share/zoneinfo/Indian  \
#   && rm -rf /usr/share/zoneinfo/Mexico  \
#   && rm -rf /usr/share/zoneinfo/Pacific  \
#   && rm -rf /usr/share/zoneinfo/Chile  \
#   && rm -rf /usr/share/zoneinfo/Canada \
#   && rm -rf /var/cache/apk/* \
#   && rm -rf /tmp/*

# Setup the virtualenv
RUN python -m venv /opt/venv

# Install Python deps
COPY requirements.txt .
RUN /opt/venv/bin/python -m pip install pip --upgrade
RUN /opt/venv/bin/python -m pip install wheel --upgrade
RUN pip install --no-cache-dir -r requirements.txt

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd Stage
# Runtime Image
#
FROM base AS final

RUN apk add --update --no-cache \
  apk-cron busybox-suid tzdata \
  && rm -rf /var/cache/apk/*

WORKDIR /nfeimport

# Copy project files
COPY . .
# Copy files from build stage
COPY --from=build /opt/venv /opt/venv
COPY --from=build /bin/bash /bin/bash
# COPY --from=build /var/spool/cron /var/spool/cron
# COPY --from=build /usr/bin/crontab /usr/bin/crontab
COPY --from=build /etc/localtime /etc/localtime
COPY --from=build /etc/timezone /etc/timezone
COPY --from=build /usr/bin/htop /usr/bin/htop
#
RUN touch /var/log/cron.log
RUN chmod a+x /nfeimport/NFeRun.sh
# RUN chmod a+x /nfeimport/entrypoint.sh
# RUN /nfeimport/entrypoint.sh
RUN crontab /nfeimport/cronfile
# RUN crond -f -L /var/log/cron.log
#
RUN mkdir processed
#
ENTRYPOINT ["crond", "-l", "0", "-d", "0", "-f"]
#
CMD ["/bin/bash"]
