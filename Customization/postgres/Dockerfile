# 1. Update the base image version
FROM postgres:18

# 2. Update the extension package name to match the new version
RUN apt-get update \
    && apt-get install -y --no-install-recommends postgresql-18-pgvector \
    && rm -rf /var/lib/apt/lists/*