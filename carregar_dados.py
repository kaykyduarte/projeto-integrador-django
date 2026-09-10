import pandas as pd
import sqlite3

df = pd.read_csv("dados/IBGE_populacaobrasil_2025.csv")

df["populacao"] = df["populacao"].str.replace(".", "", regex=False).astype(int)

colunas = ['estado', 'uf', 'regiao', 'populacao', 'ano']
registros = list(df[colunas].itertuples(index=False, name=None))

conexao = sqlite3.connect("db.sqlite3")
cursor = conexao.cursor()

sql_insert = """
INSERT INTO populacao_estados (
    estado,
    uf,
    regiao,
    populacao,
    ano
)
VALUES (?, ?, ?, ?, ?);
"""

try:
    cursor.executemany(sql_insert, registros)
    conexao.commit()
    print(f"{len(registros)} registros inseridos.")
except Exception:
    conexao.rollback()
    raise
finally:
    conexao.close()