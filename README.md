<div align="center">

# MLOps / AIOps Lab

**Treino · Avaliação · Registro · Serving · Monitoramento**

<img src="https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/FastAPI-000000?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
<img src="https://img.shields.io/badge/scikit--learn-000000?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="scikit-learn" />
<img src="https://img.shields.io/badge/Docker-000000?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
<img src="https://img.shields.io/badge/CI-000000?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions" />

</div>

---

Projeto de portfólio para demonstrar o ciclo completo de um modelo de Machine Learning aplicado a risco operacional sintético.

## Fluxo

~~~text
DATA
  ↓
TRAIN
  ↓
EVALUATE
  ↓
REGISTER
  ↓
SERVE
  ↓
MONITOR
~~~

O laboratório gera dados sintéticos de infraestrutura, compara modelos, registra o artefato selecionado, publica inferência por API e monitora mudanças na distribuição dos dados.

## O que o projeto demonstra

- geração controlada de dados sintéticos;
- comparação entre Logistic Regression e Random Forest;
- accuracy, precision, recall, F1 e ROC AUC;
- seleção e persistência do melhor modelo;
- registro de versão, métricas e SHA-256 do artefato;
- API de inferência com FastAPI;
- monitoramento de drift com Population Stability Index;
- revisão humana quando a distribuição muda;
- testes automatizados e execução em container.

## Executar

~~~bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
python train.py
uvicorn app:app --reload
~~~

A aplicação fica disponível em <code>http://127.0.0.1:8000</code>.

## Estrutura

~~~text
app.py        API e serving
data.py       geração/preparo dos dados
train.py      treinamento e avaliação
model.py      pipeline de ML
registry.py   registro/versionamento do modelo
drift.py      monitoramento de distribuição
tests/        testes automatizados
docs/         documentação complementar
~~~

## Limitações

Todos os dados são sintéticos. A variável <code>incident</code> é gerada por uma regra probabilística controlada e não representa incidentes reais.

O PSI é utilizado para demonstrar monitoramento de distribuição; drift não significa automaticamente queda de performance do modelo.

## Próximas evoluções

- registry externo;
- promoção de modelo por estágio;
- histórico de drift;
- métricas de latência e erro da API;
- avaliação contínua de performance.

---

<div align="center">

Projeto de laboratório. O objetivo é demonstrar engenharia de ML, não apresentar um modelo como pronto para produção.

</div>
