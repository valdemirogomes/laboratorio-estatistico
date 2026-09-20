# RELATÓRIO — Laboratório Estatístico Interativo

## 1. Dataset e justificativa
Versão executável acompanha dataset sintético de hábitos de estudo, com 1.500 registros, variáveis numéricas e categóricas. **Para a entrega, substituir por dataset público real e inserir aqui a fonte original.**

## 2. Tratamento
A aplicação remove valores ausentes apenas da(s) coluna(s) selecionada(s) antes dos cálculos. Conversões/decisões adicionais devem ser documentadas ao trocar o dataset.

## 3. Núcleo estatístico
As medidas exibidas são calculadas em `minhastats.py`: média; mediana; moda; amplitude; variância populacional/amostral; desvio padrão; percentis; quartis; coeficiente de variação; covariância; Pearson; regressão por mínimos quadrados e R². NumPy é usado nos testes como referência, não no núcleo.

## 4. Validação
Execute `pytest -v`. Os testes comparam o núcleo com NumPy, incluindo `ddof=1` para variância/covariância amostral e tolerâncias numéricas.

## 5. Módulos
A interface Streamlit oferece: inspeção do dataset; descritiva com Sturges e outliers IQR; LGN; TCL sobre os dados; sobreposição de Normal/Exponencial/Uniforme/Poisson; correlação, regressão, R² e predição dentro da faixa observada.

## 6. Três descobertas
Use a própria aplicação para produzir três afirmações sustentadas por número + gráfico. Sugestões: relação horas de estudo × nota; contraste de notas por método/curso; investigação dos outliers. Registre limites e evite linguagem causal para simples associação.

## 7. Entrega
Adicionar integrantes/matrículas, URL original do dataset, URL do repositório público, URL do vídeo e resumo executivo. O histórico de commits deve ser real e distribuído pela equipe.
