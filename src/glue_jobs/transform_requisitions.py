from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, to_date
from src.common.config import S3_BUCKET, RAW_PREFIX, CURATED_PREFIX

spark = SparkSession.builder.appName("transform_requisitions").getOrCreate()

raw_path = f"s3://{S3_BUCKET}/{RAW_PREFIX}requisitions/*/*.jsonl"
curated_path = f"s3://{S3_BUCKET}/{CURATED_PREFIX}requisitions/"

df = spark.read.json(raw_path)

df = df.withColumn("opened_dt", to_date(col("opened_at"))).drop("opened_at").withColumn(
    "role", trim(col("role"))
)

(df.write.mode("overwrite").parquet(curated_path))

print("Wrote curated requisitions →", curated_path)
