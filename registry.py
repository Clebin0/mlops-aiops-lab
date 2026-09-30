from __future__ import annotations
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parent
ARTIFACTS=ROOT/"artifacts"
REGISTRY=ARTIFACTS/"registry.json"

def sha256(path:Path)->str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()

def register(model_path:Path,metrics:dict,model_name:str)->dict:
    ARTIFACTS.mkdir(exist_ok=True)
    previous=[]
    if REGISTRY.exists():
        previous=json.loads(REGISTRY.read_text(encoding="utf-8")).get("versions",[])
    version=f"v{len(previous)+1}"
    row={"version":version,"model":model_name,"created_at":datetime.now(timezone.utc).isoformat(),"artifact_sha256":sha256(model_path),"metrics":metrics}
    payload={"active_version":version,"versions":previous+[row]}
    REGISTRY.write_text(json.dumps(payload,indent=2),encoding="utf-8")
    return row

def read_registry()->dict:
    if not REGISTRY.exists(): return {"active_version":None,"versions":[]}
    return json.loads(REGISTRY.read_text(encoding="utf-8"))
