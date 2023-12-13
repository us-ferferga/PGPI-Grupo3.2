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
ARG ADMIN_USER=root
ARG ADMIN_EMAIL=root@root.com
# Set environment variables
ENV ADMIN_USER=$ADMIN_USER
ENV ADMIN_EMAIL=$ADMIN_EMAIL

COPY .docker /scripts
COPY backend /app/backend/
COPY assets /app/assets/
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
