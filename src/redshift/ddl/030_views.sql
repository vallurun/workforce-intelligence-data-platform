CREATE OR REPLACE VIEW ita.v_hiring_funnel AS
SELECT c.candidate_id, c.applied_ts::date AS applied_dt, c.stage, c.country, c.source
FROM ita.candidates c;

CREATE OR REPLACE VIEW ita.v_open_reqs AS
SELECT req_id, role, location, opened_dt, department FROM ita.requisitions;
