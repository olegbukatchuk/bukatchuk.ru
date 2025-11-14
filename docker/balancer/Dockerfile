FROM nginx:1.27.3-alpine

COPY conf/nginx.conf /etc/nginx/nginx.conf

COPY docker-entrypoint.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/docker-entrypoint.sh

COPY certbot.sh /certbot.sh
COPY etc/service.conf /etc/nginx/service.conf

RUN \
 rm /etc/nginx/conf.d/default.conf && \
 chmod +x /certbot.sh && \
 apk add  --update certbot tzdata openssl && \
 rm -rf /var/cache/apk/*

CMD ["/usr/local/bin/docker-entrypoint.sh"]
