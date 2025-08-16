terraform { required_providers { aws = { source = "hashicorp/aws", version = "~> 5.0" } } }
provider "aws" { region = var.region }

resource "aws_s3_bucket" "etl" { bucket = var.bucket_name }

# Placeholders for Redshift, Glue job(s), Lambda, IAM roles.
# Add modules/resources per your account constraints.
