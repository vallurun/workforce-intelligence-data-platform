CREATE TABLE IF NOT EXISTS ita.candidates (
  candidate_id VARCHAR(64) DISTKEY,
  applied_ts TIMESTAMP,
  stage VARCHAR(32),
  country VARCHAR(8),
  source VARCHAR(64)
) SORTKEY(applied_ts);
