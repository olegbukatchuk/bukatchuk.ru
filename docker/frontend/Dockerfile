FROM nginx:1.29.1

MAINTAINER Oleg Bukatchuk <oleg@bukatchuk.com>

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
