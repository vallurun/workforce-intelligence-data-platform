# Workforce Intelligence Data Platform

End-to-end AWS ETL to ingest **hiring funnel and workforce datasets** into **Amazon Redshift** using **S3 → Lambda → Glue → Redshift**. Delivers **modeled tables + secure views** for self-service analytics (BIE/HR/TA).

## Architecture
1. **Lambda** ingests JSONL files to S3 (`raw/`).
2. **Glue** jobs (PySpark) cleanse + model into S3 (`curated/`, parquet).
3. **Redshift** `COPY` loads curated parquet → warehouse tables.
4. **Views** expose governed, analyst-friendly schemas.

## Quickstart
- Local test: run Glue scripts with local PySpark, using `data_samples/`.
- Deploy (high level): provision infra in `infra/terraform`, create Redshift + S3 + Glue IAM; upload Lambda zip; schedule Glue jobs.

## Commands to Push
```bash
git init && git add .
git commit -m "init: workforce intelligence data platform"
git branch -M main
git remote add origin https://github.com/<your-user>/workforce-intelligence-data-platform.git
git push -u origin main
```
