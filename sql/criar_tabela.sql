CREATE TABLE populacao_estados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    estado TEXT NOT NULL,
    uf TEXT NOT NULL,
    regiao TEXT NOT NULL,
    populacao INTEGER NOT NULL,
    ano INTEGER NOT NULL,
    UNIQUE (uf, ano)
);