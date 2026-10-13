FROM spark:3.5.5-scala2.12-java17-python3-ubuntu

USER root

ARG ICEBERG_VERSION=1.10.1
ARG MAVEN=https://repo1.maven.org/maven2

ADD --chmod=644 ${MAVEN}/org/apache/iceberg/iceberg-spark-runtime-3.5_2.12/${ICEBERG_VERSION}/iceberg-spark-runtime-3.5_2.12-${ICEBERG_VERSION}.jar /opt/spark/jars/
ADD --chmod=644 ${MAVEN}/org/apache/iceberg/iceberg-aws-bundle/${ICEBERG_VERSION}/iceberg-aws-bundle-${ICEBERG_VERSION}.jar /opt/spark/jars/
ADD --chmod=644 ${MAVEN}/org/postgresql/postgresql/42.7.4/postgresql-42.7.4.jar /opt/spark/jars/

RUN pip3 install --no-cache-dir boto3 requests pandas pyarrow beautifulsoup4 lxml psycopg2-binary pytest

COPY spark-defaults.conf /opt/spark/conf/spark-defaults.conf

USER spark
