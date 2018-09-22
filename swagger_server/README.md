# Introduction

Web interface for media-center.

# Generate Swagger Server skeleton

```shell
docker run -u "`id -u`:`id -g`" -v "`pwd`":/local swaggerapi/swagger-codegen-cli:v2.3.1 generate -i /local/swagger.json -l python-flask -o /local
```
