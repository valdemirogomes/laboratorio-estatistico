"""Baixa o dataset Adult da UCI e salva em dados/dataset.csv."""
from pathlib import Path
import pandas as pd

URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
COLUNAS = ["age","workclass","fnlwgt","education","education_num","marital_status","occupation","relationship","race","sex","capital_gain","capital_loss","hours_per_week","native_country","income"]

def main():
    destino = Path(__file__).parent / "dados" / "dataset.csv"
    destino.parent.mkdir(exist_ok=True)
    df = pd.read_csv(URL, names=COLUNAS, skipinitialspace=True, na_values="?")
    df.to_csv(destino, index=False)
    print(f"Dataset salvo em {destino} — {len(df)} registros, {df.shape[1]} colunas.")

if __name__ == "__main__": main()
