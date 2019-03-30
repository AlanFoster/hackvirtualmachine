FROM python:3.8.0a3-alpine3.9

WORKDIR /app

## Setup antlr
RUN apk add --no-cache curl openjdk8-jre \
    && curl https://www.antlr.org/download/antlr-4.7.2-complete.jar -o /usr/local/lib/antlr-4.7.2-complete.jar \
    && echo "java -Xmx500M -cp \"/usr/local/lib/antlr-4.7.2-complete.jar:$CLASSPATH\" org.antlr.v4.Tool \$@" >> /usr/local/bin/antlr4 \
    && chmod u+x /usr/local/bin/antlr4

## Install python dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --deploy --dev --ignore-pipfile --system

COPY . .