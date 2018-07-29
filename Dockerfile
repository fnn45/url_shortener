FROM smebberson/alpine-confd:2.0.0

ENV RABBITMQ_VERSION=3.6.1 \
    ERLANG_PKG_VERSION=18.1-r5

# Setup Erlang, download RabbitMQ and setup the management plugin
RUN apk add --update --no-cache curl tar xz bash \
        erlang=${ERLANG_PKG_VERSION} erlang-mnesia=${ERLANG_PKG_VERSION} \
        erlang-public-key=${ERLANG_PKG_VERSION} erlang-crypto=${ERLANG_PKG_VERSION} \
        erlang-ssl=${ERLANG_PKG_VERSION} erlang-sasl=${ERLANG_PKG_VERSION} \
        erlang-asn1=${ERLANG_PKG_VERSION} erlang-inets=${ERLANG_PKG_VERSION} \
        erlang-os-mon=${ERLANG_PKG_VERSION} erlang-xmerl=${ERLANG_PKG_VERSION} \
        erlang-eldap=${ERLANG_PKG_VERSION} erlang-syntax-tools=${ERLANG_PKG_VERSION} && \
    curl -sSL https://www.rabbitmq.com/releases/rabbitmq-server/v${RABBITMQ_VERSION}/rabbitmq-server-generic-unix-${RABBITMQ_VERSION}.tar.xz | tar -xJ -C / --strip-components 1 && \
    rm -rf /share/**/rabbitmq*.xz && \
    apk del --purge curl tar xz && \
    addgroup rabbitmq && \
    adduser -DS -g "" -G rabbitmq -s /bin/sh -h /var/lib/rabbitmq rabbitmq && \
    mkdir -p /data/rabbitmq && \
    chown -R rabbitmq:rabbitmq /data/rabbitmq

# Install python, bash, git
RUN apk add --no-cache python3 bash git  && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools

# Copy files to /usr/src directory
WORKDIR /usr/src
COPY . .

# Install dependencies and init db
RUN pip3 install -r requirements.txt && \
    python3 manage.py makemigrations && \
    python3 manage.py migrate && \
    chmod 700 start_server.sh

EXPOSE 8000
VOLUME ["/data/rabbitmq"]
CMD source start_server.sh
