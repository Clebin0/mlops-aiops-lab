from __future__ import annotations
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from data import FEATURES,generate_dataset,shifted_batch
from drift import drift_report
from model import metrics,predict,reference
from registry import read_registry

app=FastAPI(title="MLOps AIOps Lab",version="1.0.0")

class PredictIn(BaseModel):
    cpu:float=Field(ge=0,le=100)
    memory:float=Field(ge=0,le=100)
    latency_ms:float=Field(ge=0)
    error_rate:float=Field(ge=0)
    packet_loss:float=Field(ge=0)
    disk_io:float=Field(ge=0)

@app.get("/",response_class=HTMLResponse)
def home():
    with open("frontend.html","r",encoding="utf-8") as f:return f.read()

@app.get("/health")
def health():return {"status":"ok","version":"1.0.0"}

@app.get("/model")
def model_info():return {"metrics":metrics(),"registry":read_registry()}

@app.post("/predict")
def inference(body:PredictIn):return predict(body.model_dump())

@app.get("/drift")
def drift_demo():
    return drift_report(reference(),shifted_batch())

@app.get("/drift/stable")
def drift_stable():
    return drift_report(reference(),generate_dataset(seed=123,rows=300)[FEATURES])
