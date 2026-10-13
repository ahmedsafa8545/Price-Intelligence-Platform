FROM docker:27-cli AS dockercli

FROM apache/airflow:3.0.6
USER root
COPY --from=dockercli /usr/local/bin/docker /usr/local/bin/docker
USER airflow
