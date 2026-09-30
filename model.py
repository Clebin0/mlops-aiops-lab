from __future__ import annotations
import json
from pathlib import Path
import joblib
import pandas as pd
from data import FEATURES
from train import MODEL,METRICS,REFERENCE,train

def ensure():
    if not MODEL.exists() or not METRICS.exists() or not REFERENCE.exists(): train(True)

def load_model():
    ensure();return joblib.load(MODEL)

def metrics():
    ensure();return json.loads(METRICS.read_text(encoding="utf-8"))

def reference():
    ensure();return pd.read_csv(REFERENCE)

def predict(payload:dict)->dict:
    model=load_model()
    row=pd.DataFrame([[payload[k] for k in FEATURES]],columns=FEATURES)
    proba=float(model.predict_proba(row)[0,1])
    return {"incident_risk":round(proba,4),"prediction":"incident" if proba>=.5 else "normal","review_required":proba>=.5}
