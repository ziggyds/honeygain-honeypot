FROM python:alpine
COPY honeypot.py honeypot.py
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pyHoneygain discord-webhook
RUN echo "0 22 * * * /bin/bash /honeypot.py" >> /var/spool/cron/crontabs/root
CMD crond -f -l 2 -L /dev/stdout