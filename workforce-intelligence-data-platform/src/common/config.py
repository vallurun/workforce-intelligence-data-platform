import os

S3_BUCKET = os.getenv("S3_BUCKET", "your-etl-bucket")
RAW_PREFIX = os.getenv("RAW_PREFIX", "raw/")
CURATED_PREFIX = os.getenv("CURATED_PREFIX", "curated/")
REDSHIFT_IAM_ROLE = os.getenv("REDSHIFT_IAM_ROLE", "arn:aws:iam::123456789012:role/RedshiftCopyRole")
REDSHIFT_DB = os.getenv("REDSHIFT_DB", "workforce")
REDSHIFT_SCHEMA = os.getenv("REDSHIFT_SCHEMA", "ita")
