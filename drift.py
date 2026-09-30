from __future__ import annotations
import numpy as np
import pandas as pd
from data import FEATURES

def psi(expected,actual,bins:int=10)->float:
    expected=np.asarray(expected,dtype=float)
    actual=np.asarray(actual,dtype=float)
    cuts=np.unique(np.quantile(expected,np.linspace(0,1,bins+1)))
    if len(cuts)<3: return 0.0
    cuts[0],cuts[-1]=-np.inf,np.inf
    e=np.histogram(expected,bins=cuts)[0]/max(1,len(expected))
    a=np.histogram(actual,bins=cuts)[0]/max(1,len(actual))
    e=np.clip(e,1e-6,None);a=np.clip(a,1e-6,None)
    return float(np.sum((a-e)*np.log(a/e)))

def drift_report(reference:pd.DataFrame,current:pd.DataFrame)->dict:
    features={}
    for col in FEATURES:
        value=round(psi(reference[col],current[col]),4)
        level="high" if value>=.25 else "moderate" if value>=.1 else "low"
        features[col]={"psi":value,"level":level}
    high=sum(1 for x in features.values() if x["level"]=="high")
    moderate=sum(1 for x in features.values() if x["level"]=="moderate")
    return {"features":features,"high_drift_features":high,"moderate_drift_features":moderate,"review_required":high>0}
