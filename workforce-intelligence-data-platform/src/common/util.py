from datetime import datetime

def iso_to_date(iso_ts: str) -> str:
    try:
        return datetime.fromisoformat(iso_ts.replace("Z", "+00:00")).date().isoformat()
    except Exception:
        return None
