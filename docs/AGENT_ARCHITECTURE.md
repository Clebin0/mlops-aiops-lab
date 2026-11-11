# Multi-agent architecture

## Roles

- **Experiment analyst**: summarizes training runs and compares metrics with the correct split and dataset provenance.
- **Model evaluator**: checks metric regressions, calibration evidence, subgroup limitations, and leakage warnings.
- **Registry reviewer**: verifies model artifact hash, version, evaluation report, and required approvals.
- **Drift analyst**: explains PSI and distribution changes without treating drift as automatic performance failure.
- **Release advisor**: prepares a promotion recommendation; never promotes a model.

## Workflow

Run artifacts and metrics -> deterministic validation -> specialist review -> consolidated report -> human approval.

## Safety

All datasets are synthetic in the current lab. Outputs must state this limitation. Agents cannot execute training jobs, replace registered artifacts, promote models, deploy services, or alter monitoring thresholds. The existing pipeline remains authoritative.

## Acceptance criteria

Reports link every conclusion to a run ID, artifact hash, metric, and dataset version. No recommendation is framed as an automatic deployment decision.
