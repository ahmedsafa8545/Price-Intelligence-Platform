"""اختبار سريع إن Spark + Iceberg REST + MinIO متوصلين."""
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("smoke_test").getOrCreate()

spark.sql("CREATE NAMESPACE IF NOT EXISTS lake.bronze")
spark.sql("CREATE TABLE IF NOT EXISTS lake.bronze.smoke (id INT, name STRING) USING iceberg")
spark.sql("INSERT INTO lake.bronze.smoke VALUES (1, 'ok')")
spark.sql("SELECT * FROM lake.bronze.smoke").show()
spark.stop()
