"""Lambda handler to ingest JSONL payloads to S3 raw prefix.
In production this might receive payloads via API Gateway / EventBridge.
"""
import json
import boto3
from datetime import datetime
from src.common.config import S3_BUCKET, RAW_PREFIX

s3 = boto3.client("s3")

def _object_key(dataset: str) -> str:
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    return f"{RAW_PREFIX}{dataset}/dt={ts[:8]}/payload_{ts}.jsonl"

def lambda_handler(event, context):
    # Expect event like {"dataset":"candidates", "records":[{...},{...}]}
    dataset = event.get("dataset", "candidates")
    records = event.get("records", [])
    body = "\n".join(json.dumps(r) for r in records)
    key = _object_key(dataset)
    s3.put_object(Bucket=S3_BUCKET, Key=key, Body=body.encode("utf-8"))
    return {"statusCode": 200, "key": key, "count": len(records)}
