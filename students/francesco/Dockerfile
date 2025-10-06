FROM python:3.12-alpine

RUN addgroup -S app && adduser -S app -G app

WORKDIR /app

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
    apk add --no-cache wget

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN mkdir -p /var/log/app && chown -R app:app /var/log/app

USER app

EXPOSE 8080

HEALTHCHECK --interval=10s --timeout=3s --retries=5 \
  CMD wget -qO- http://localhost:8080/health >/dev/null || exit 1

CMD ["python","/app/app.py"]
