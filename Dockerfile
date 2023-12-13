# slim image can't be used since we need git to fetch the commit hash
FROM node:20-slim AS build

COPY package.json package-lock.json .npmrc /app/
COPY frontend /app/frontend
WORKDIR /app/frontend

# Install dependencies
RUN npm ci --no-audit

# Build client
RUN npm run build

# Deploy built frontend to Django
FROM python:slim

# Set build arguments
ARG DJANGO_SUPERUSER_USERNAME=admin
ARG DJANGO_SUPERUSER_EMAIL=admin@admin.com
ARG DJANGO_SUPERUSER_PASSWORD=admin
# Set environment variables
ENV DJANGO_SUPERUSER_USERNAME=$DJANGO_SUPERUSER_USERNAME
ENV DJANGO_SUPERUSER_EMAIL=$DJANGO_SUPERUSER_EMAIL
ENV DJANGO_SUPERUSER_PASSWORD=$DJANGO_SUPERUSER_PASSWORD

COPY .docker /scripts
COPY backend /app/backend/
COPY assets/sample_data /app/assets/sample_data
COPY --from=build /app/frontend/dist/ /app/backend/static/
RUN mkdir -p /data \
    && rm -rf /bin/sh \
    && ln -s /bin/bash /bin/sh \
    && ln -s /data /app/backend/data \
    && rm -rf .dockerenv \
    && chmod +x /scripts/*.sh

WORKDIR /app/backend
RUN pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT [ "/scripts/entrypoint.sh" ]
CMD [ "/scripts/run.sh" ]
LABEL org.opencontainers.image.source = "https://github.com/us-ferferga/PGPI-Grupo3.2"
