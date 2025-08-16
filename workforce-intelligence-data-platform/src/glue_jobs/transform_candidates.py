from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, trim, to_timestamp
from src.common.config import S3_BUCKET, RAW_PREFIX, CURATED_PREFIX

spark = SparkSession.builder.appName("transform_candidates").getOrCreate()

raw_path = f"s3://{S3_BUCKET}/{RAW_PREFIX}candidates/*/*.jsonl"
curated_path = f"s3://{S3_BUCKET}/{CURATED_PREFIX}candidates/"

df = spark.read.json(raw_path)

df = (
    df.withColumn("stage", lower(trim(col("stage"))))
      .withColumn("applied_ts", to_timestamp(col("applied_at")))
      .drop("applied_at")
)

(df.write.mode("overwrite")
   .partitionBy("stage")
   .parquet(curated_path))

print("Wrote curated candidates →", curated_path)
