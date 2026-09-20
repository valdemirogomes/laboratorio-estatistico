# 🧮 Laboratório Estatístico Interativo

Projeto desenvolvido para a disciplina **Matemática e Estatística para Computação**, na atividade de Sistematização — Construindo o Seu Laboratório Estatístico.

A aplicação utiliza **Python + Streamlit** para explorar um conjunto de dados real por meio de estatística descritiva, probabilidade, simulações, distribuições teóricas, correlação e regressão linear. As principais operações estatísticas são implementadas manualmente em `minhastats.py` e validadas por testes automatizados.

## 📊 Dataset

A versão final foi estruturada para utilizar o dataset público **Adult / Census Income**, do **UCI Machine Learning Repository**.

**Fonte original:** https://archive.ics.uci.edu/dataset/2/adult

O conjunto possui mais de 48 mil registros e contém variáveis numéricas e categóricas adequadas aos requisitos da atividade.

### Variáveis numéricas disponíveis

- `age`
- `fnlwgt`
- `education-num`
- `capital-gain`
- `capital-loss`
- `hours-per-week`

### Variáveis categóricas disponíveis

- `workclass`
- `education`
- `marital-status`
- `occupation`
- `relationship`
- `race`
- `sex`
- `native-country`
- `income`

## 🎯 Módulos

### Módulo 0 — Dados Reais
Carregamento e preparação do dataset público para exploração interativa.

### Módulo 1 — Núcleo Estatístico Próprio
O arquivo `minhastats.py` implementa média, mediana, moda, amplitude, variância populacional e amostral, desvio padrão, quartis/percentis, coeficiente de variação, covariância, correlação de Pearson e regressão linear simples.

As medidas estatísticas exibidas ao usuário são calculadas pelas implementações próprias. NumPy é utilizado como referência nos testes automatizados.

### Módulo 2 — Estatística Descritiva Interativa
Seleção de variáveis, medidas de tendência central e dispersão, tabela de frequências, histogramas, boxplots, detecção de outliers pela regra do IQR e interpretação da distribuição.

### Módulo 3 — Probabilidade e Simulação
Simulações da **Lei dos Grandes Números** e do **Teorema Central do Limite**, com parâmetros controláveis pelo usuário.

### Módulo 4 — Distribuições Teóricas
Comparação do histograma observado com distribuições teóricas candidatas, usando parâmetros estimados a partir dos dados.

### Módulo 5 — Correlação e Regressão Linear
Diagrama de dispersão, coeficiente de Pearson, regressão por mínimos quadrados, equação da reta, R² e predição interativa.

> **Correlação não implica causalidade.**

### Módulo 6 — Descobertas Estatísticas
Registro das três descobertas mais relevantes obtidas a partir dos números e gráficos produzidos pela aplicação.

## 🧪 Testes automatizados

Os testes ficam em `test_minhastats.py` e comparam as implementações próprias com referências consolidadas, considerando tolerância numérica para ponto flutuante.

Execute:

```bash
pytest -v
```

## 🗂️ Estrutura

```text
laboratorio-estatistico/
├── app.py
├── baixar_dataset.py
├── minhastats.py
├── test_minhastats.py
├── requirements.txt
├── README.md
├── RELATORIO.md
└── dados/
```

## ⚙️ Tecnologias

- Python
- Streamlit
- Pandas
- NumPy
- SciPy
- Matplotlib
- Pytest

## 🚀 Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/valdemirogomes/laboratorio-estatistico.git
cd laboratorio-estatistico
```

### 2. Criar o ambiente virtual

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Obter/preparar o dataset

```bash
python baixar_dataset.py
```

### 5. Executar os testes

```bash
pytest -v
```

### 6. Executar a aplicação

```bash
streamlit run app.py
```

Normalmente a aplicação ficará disponível em `http://localhost:8501`.

## 📄 Relatório

O arquivo `RELATORIO.md` documenta o dataset, decisões de implementação, fórmulas, validação, módulos, descobertas estatísticas e limitações da análise.

## 👨‍💻 Autor

**Valdemiro Gomes Rodrigues de Aguiar**  

