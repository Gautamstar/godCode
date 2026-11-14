# godCode sync service: one Python file, no dependencies.
FROM python:3.12-alpine
RUN adduser -D -u 10001 godcode && mkdir /data && chown godcode /data
COPY server.py /app/server.py
USER godcode
WORKDIR /app
ENV SYNC_HOST=0.0.0.0 SYNC_DB=/data/godcode-sync.db PYTHONUNBUFFERED=1
EXPOSE 8787
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8787/health', timeout=4)"
CMD ["python", "server.py", "serve"]
