# Hack Compiler

## Generate parser

```bash
docker-compose build
docker-compose run --rm service /bin/sh /usr/local/bin/antlr4 VM.g4 -Dlanguage=Python3 -visitor -o parser
```

## Run tests

```shell
docker-compose build
docker-compose run test
```