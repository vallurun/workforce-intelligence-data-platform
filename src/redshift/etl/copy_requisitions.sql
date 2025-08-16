COPY ita.requisitions
FROM 's3://YOUR_BUCKET/curated/requisitions/'
IAM_ROLE 'arn:aws:iam::123456789012:role/RedshiftCopyRole'
FORMAT AS PARQUET;
