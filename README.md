# MLOps / AIOps Lab

Projeto de portfólio para demonstrar o ciclo completo de um modelo aplicado a risco operacional sintético.

## Pipeline

`DATA -> TRAIN -> EVALUATE -> REGISTER -> SERVE -> MONITOR`

O projeto:
- gera dados sintéticos de infraestrutura;
- compara Logistic Regression e Random Forest;
- mede accuracy, precision, recall, F1 e ROC AUC;
- salva o modelo selecionado;
- registra versão, métricas e SHA-256 do artefato;
- serve inferência via FastAPI;
- calcula drift por Population Stability Index (PSI);
- sinaliza revisão humana quando a distribuição muda.

## Por que este projeto existe?

Treinar um modelo é só uma parte do problema. O objetivo aqui é demonstrar como o modelo vira um componente versionado, testado, servido por API e observado depois do deploy.

## Executar

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python train.py
uvicorn app:app --reload
```

Abra `http://127.0.0.1:8000`.

## Limitações

Todos os dados são sintéticos. A variável `incident` é gerada por uma regra probabilística controlada e não representa incidentes reais. PSI é usado aqui para demonstrar monitoramento de distribuição; drift não implica queda automática de performance.

## Próximos passos

- container registry;
- promoção de modelo por estágio;
- histórico de drift;
- monitoramento de latência e erro da API;
- comparação de performance do modelo ao longo do tempo.
