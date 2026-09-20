# Laboratório Estatístico Interativo
Projeto desenvolvido a partir do Guia de Sistematização de Matemática e Estatística para Computação (2026).

## Requisitos atendidos
- núcleo próprio em `minhastats.py`, sem NumPy nas contas estatísticas;
- média, mediana, moda, amplitude, variâncias, desvio, percentis/quartis, CV, covariância, Pearson e regressão linear;
- testes contra NumPy;
- Streamlit com descritiva, Sturges, IQR, LGN, TCL, distribuições, correlação/regressão e predição limitada;
- dataset com > 1.000 registros, 4+ numéricas e 2+ categóricas.

## Executar
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
pytest -v
streamlit run app.py
```

## Dataset
O CSV incluído é **sintético/demonstrativo**, gerado para tornar o projeto executável imediatamente e satisfazer os requisitos estruturais do guia. Para a entrega acadêmica, substitua-o por um dataset de fonte original (Kaggle/UCI/dados.gov.br etc.) e registre a URL original no relatório/PDF.
