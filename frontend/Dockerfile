FROM node:21-bullseye
LABEL maintainer="paulopereira.dev"

EXPOSE 3000

COPY ./app /app
COPY ./entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

RUN FILE=/app/package.json && \
    if [ -f "$FILE" ]; \
    then \
        npm install ; \
    fi

ENTRYPOINT ["/entrypoint.sh"]
