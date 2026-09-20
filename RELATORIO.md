# RELATÓRIO — Laboratório Estatístico Interativo

## 2. Dataset
Foi escolhido o **Adult / Census Income**, do UCI Machine Learning Repository, com 48.842 instâncias e 14 atributos de entrada. Os dados foram extraídos de registros censitários de 1994 e incluem variáveis como idade, escolaridade, horas trabalhadas por semana, classe de trabalho, ocupação e faixa de renda.

Fonte: https://archive.ics.uci.edu/dataset/2/adult  
DOI: https://doi.org/10.24432/C5XW20

Há valores ausentes em algumas variáveis categóricas. Na aplicação, operações numéricas usam `dropna()` apenas na(s) coluna(s) selecionada(s), preservando o restante do dataset.

## 3. Núcleo estatístico próprio
As medidas são implementadas em `minhastats.py`.

- Média: $\bar{x}=\frac{1}{n}\sum x_i$
- Variância populacional: $\sigma^2=\frac{\sum(x_i-\bar{x})^2}{n}$
- Variância amostral: $s^2=\frac{\sum(x_i-\bar{x})^2}{n-1}$
- Desvio padrão: $s=\sqrt{s^2}$
- CV: $CV=\frac{s}{\bar{x}}\times100\%$
- Covariância amostral: $cov(X,Y)=\frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{n-1}$
- Pearson: $r=\frac{cov(X,Y)}{s_Xs_Y}$
- Regressão: $\hat{y}=b_0+b_1x$, com mínimos quadrados.

Percentis usam a posição $p(n-1)/100$ e interpolação linear.

## 4. Validação
`test_minhastats.py` compara média, mediana, amplitude, variâncias, desvios, percentis/quartis, CV, covariância, Pearson e regressão com NumPy. As comparações de ponto flutuante usam `np.isclose`, tipicamente com `rtol=1e-9`; percentis usam `rtol=1e-6` devido à interpolação.

## 5. Módulos da aplicação
### Módulo 0 — Dados reais
Inspeção do dataset, quantidade de registros, tipos e nulos.

### Módulos 1 e 2 — Descritiva
Medidas próprias, histograma com Sturges, boxplot, IQR, outliers e interpretação automática de assimetria.

### Módulo 3 — Simulação
LGN por lançamentos de moeda e TCL por reamostragem de variável real, com tamanho amostral e repetições controláveis.

### Módulo 4 — Distribuições
Sobreposição de Normal, Exponencial, Uniforme ou Poisson ao histograma, com parâmetros estimados a partir dos dados.

### Módulo 5 — Correlação e regressão
Pearson próprio, mínimos quadrados, equação, R², gráfico e predição limitada à faixa observada.

## 6. Três descobertas
**Preencher depois de executar a aplicação com o dataset baixado. Não inventar resultados.** Para cada descoberta, registrar: afirmação + valor estatístico + gráfico/print + limitação.

1. **Escolaridade e renda:** PREENCHER COM RESULTADO OBSERVADO.
2. **Idade e horas semanais:** PREENCHER COM RESULTADO OBSERVADO.
3. **Outliers em capital/horas:** PREENCHER COM RESULTADO OBSERVADO.

## 7. Limitações
O dataset representa um recorte censitário histórico de 1994. Associações observadas não demonstram causalidade. Algumas variáveis possuem valores ausentes, e os resultados não devem ser tratados como descrição da população atual.

## 8. Links finais
**Repositório público:** PREENCHER  
**Vídeo (3–5 min):** PREENCHER
