COPY ita.candidates
FROM 's3://YOUR_BUCKET/curated/candidates/'
IAM_ROLE 'arn:aws:iam::123456789012:role/RedshiftCopyRole'
FORMAT AS PARQUET;
