from __future__ import annotations
import json
from pathlib import Path
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,f1_score,precision_score,recall_score,roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from data import FEATURES,generate_dataset
from registry import register

ROOT=Path(__file__).resolve().parent
ARTIFACTS=ROOT/"artifacts"
MODEL=ARTIFACTS/"incident_model.joblib"
METRICS=ARTIFACTS/"metrics.json"
REFERENCE=ARTIFACTS/"reference.csv"

def candidates():
    return {
        "logistic_regression":Pipeline([("scale",StandardScaler()),("model",LogisticRegression(max_iter=1500,class_weight="balanced",random_state=42))]),
        "random_forest":RandomForestClassifier(n_estimators=280,max_depth=8,min_samples_leaf=3,class_weight="balanced",random_state=42),
    }

def evaluate(model,x_test,y_test):
    pred=model.predict(x_test)
    proba=model.predict_proba(x_test)[:,1]
    return {"accuracy":round(float(accuracy_score(y_test,pred)),4),"precision":round(float(precision_score(y_test,pred,zero_division=0)),4),"recall":round(float(recall_score(y_test,pred,zero_division=0)),4),"f1":round(float(f1_score(y_test,pred,zero_division=0)),4),"roc_auc":round(float(roc_auc_score(y_test,proba)),4)}

def train(save:bool=True):
    df=generate_dataset()
    train_df,test_df=train_test_split(df,test_size=.25,random_state=42,stratify=df["incident"])
    results=[]
    fitted={}
    for name,model in candidates().items():
        model.fit(train_df[FEATURES],train_df["incident"])
        metrics=evaluate(model,test_df[FEATURES],test_df["incident"])
        results.append({"model":name,**metrics});fitted[name]=model
    results.sort(key=lambda x:(x["f1"],x["roc_auc"]),reverse=True)
    selected=results[0]["model"];model=fitted[selected]
    summary={"selected_model":selected,"dataset":"synthetic","rows":len(df),"train_rows":len(train_df),"test_rows":len(test_df),"comparison":results,"selected_metrics":next(x for x in results if x["model"]==selected),"note":"Synthetic portfolio data; metrics are not production estimates."}
    if save:
        ARTIFACTS.mkdir(exist_ok=True)
        joblib.dump(model,MODEL)
        METRICS.write_text(json.dumps(summary,indent=2),encoding="utf-8")
        train_df[FEATURES].to_csv(REFERENCE,index=False)
        register(MODEL,summary["selected_metrics"],selected)
    return model,summary

if __name__=="__main__":
    _,summary=train(True)
    print(json.dumps(summary,indent=2))
