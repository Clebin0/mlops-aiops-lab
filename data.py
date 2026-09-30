from __future__ import annotations
import numpy as np
import pandas as pd

FEATURES=["cpu","memory","latency_ms","error_rate","packet_loss","disk_io"]

def generate_dataset(seed:int=42,rows:int=1200)->pd.DataFrame:
    rng=np.random.default_rng(seed)
    cpu=np.clip(rng.normal(48,18,rows),1,100)
    memory=np.clip(rng.normal(62,15,rows),5,100)
    latency=np.clip(rng.lognormal(3.25,.45,rows),3,450)
    error_rate=np.clip(rng.beta(1.6,18,rows)*100,0,35)
    packet_loss=np.clip(rng.beta(1.2,28,rows)*100,0,25)
    disk_io=np.clip(rng.lognormal(4.0,.55,rows),5,900)
    risk=(cpu>82).astype(int)+(memory>88).astype(int)+(latency>110).astype(int)+(error_rate>9).astype(int)+(packet_loss>4).astype(int)+(disk_io>260).astype(int)
    noise=rng.random(rows)<.035
    incident=((risk>=2)|((risk>=1)&(rng.random(rows)<.16))|noise).astype(int)
    return pd.DataFrame({"cpu":cpu.round(2),"memory":memory.round(2),"latency_ms":latency.round(2),"error_rate":error_rate.round(3),"packet_loss":packet_loss.round(3),"disk_io":disk_io.round(2),"incident":incident})

def shifted_batch(seed:int=99,rows:int=300)->pd.DataFrame:
    df=generate_dataset(seed,rows)
    df["latency_ms"]=(df["latency_ms"]*1.55).clip(upper=600)
    df["packet_loss"]=(df["packet_loss"]*1.8).clip(upper=35)
    return df
