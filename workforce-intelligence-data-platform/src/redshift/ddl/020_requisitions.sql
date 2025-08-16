CREATE TABLE IF NOT EXISTS ita.requisitions (
  req_id VARCHAR(64) DISTKEY,
  role VARCHAR(128),
  location VARCHAR(128),
  opened_dt DATE,
  department VARCHAR(64)
) SORTKEY(opened_dt);
