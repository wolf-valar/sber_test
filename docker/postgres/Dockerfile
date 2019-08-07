FROM postgres:10
RUN localedef -i ru_RU -c -f UTF-8 -A /usr/share/locale/locale.alias ru_RU.UTF-8
ENV LANG ru_RU.utf8
RUN apt-get update \
    && apt-get install -y -f \
        sudo \
    && rm -rf /var/lib/apt/lists/*
ENV POSTGRES_PASSWORD=PG_PWD
RUN echo "apt update && apt install sudo -y" >> sd && chmod +x sd
RUN echo "sudo -u postgres psql" >> pl && chmod +x pl
COPY pg_hba.conf /var/lib/postgresql/data/
COPY db_init .
#RUN sudo -u postgres /usr/lib/postgresql/10/bin/postgres -D /var/lib/postgresql/data/ && sudo -u postgres /usr/bin/psql -f db_init
