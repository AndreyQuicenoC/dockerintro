# syntax=docker/dockerfile:1.7
FROM python:3.12-alpine

# Create non-root user
RUN addgroup -S app && adduser -S app -G app

# Set working directory
WORKDIR /app

# Install wget (and optionally curl) in the image
RUN apk add --no-cache wget

# Install dependencies (separate layer for better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Create logs directory and set permissions for the app user
RUN mkdir -p /var/log/app && chown -R app:app /var/log/app

# Switch to non-root user
USER app

# Expose port 8080
EXPOSE 8080

# Simple healthcheck with wget (already installed)
HEALTHCHECK --interval=10s --timeout=3s --retries=5 \
  CMD wget -qO- http://localhost:8080/health >/dev/null || exit 1

# Start the application
CMD ["python","/app/app.py"]