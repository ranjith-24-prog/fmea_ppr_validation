# backend/telemetry.py
import uuid
import datetime as dt

def _ensure_ts(rec: dict) -> None:
    rec.setdefault("created_at", dt.datetime.utcnow().isoformat())

def log_llm_run(sb, rec: dict) -> str:
    run_id = rec.get("id") or str(uuid.uuid4())
    rec["id"] = run_id
    _ensure_ts(rec)
    sb.table("llm_runs").insert(rec).execute()
    return run_id

def log_retrieval_event(sb, rec: dict) -> str:
    event_id = rec.get("id") or str(uuid.uuid4())
    rec["id"] = event_id
    _ensure_ts(rec)
    sb.table("retrieval_events").insert(rec).execute()
    return event_id
