FROM mysql:8.0

# 환경 변수만 정의하고 실제 값은 빌드/실행 시점에 주입
ENV MYSQL_ROOT_PASSWORD=
ENV MYSQL_DATABASE=
ENV MYSQL_USER=
ENV MYSQL_PASSWORD=

RUN microdnf update && microdnf install -y ncurses

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306