from data import shifted_batch
from drift import drift_report
from model import metrics,predict,reference

def test_training_artifacts_exist():
    m=metrics()
    assert m["selected_model"] in {"logistic_regression","random_forest"}
    assert 0 <= m["selected_metrics"]["f1"] <= 1

def test_prediction_shape():
    x=predict({"cpu":90,"memory":92,"latency_ms":160,"error_rate":10,"packet_loss":5,"disk_io":300})
    assert 0 <= x["incident_risk"] <= 1
    assert x["prediction"] in {"incident","normal"}

def test_shifted_batch_has_drift_signal():
    report=drift_report(reference(),shifted_batch())
    assert report["high_drift_features"]+report["moderate_drift_features"] >= 1
