import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meu_projeto.settings")

import django
django.setup()

import pandas as pd
from django.conf import settings
from django.db import connection, transaction

df = pd.read_csv(
    settings.BASE_DIR / "dados" / "IBGE_populacaobrasil_2025.csv"
)

df["populacao"] = (
    df["populacao"]
    .astype(str)
    .str.replace(".", "", regex=False)
    .astype(int)
)

colunas = ["estado", "uf", "regiao", "populacao", "ano"]
registros = list(df[colunas].itertuples(index=False, name=None))

sql_insert = """
INSERT INTO populacao_estados (
    estado, uf, regiao, populacao, ano
)
VALUES (%s, %s, %s, %s, %s);
"""

with transaction.atomic():
    with connection.cursor() as cursor:
        cursor.executemany(sql_insert, registros)

print(f"{len(registros)} registros inseridos.")