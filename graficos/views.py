from django.shortcuts import render
from django.db import connection

from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import CDN
from bokeh.models import NumeralTickFormatter, HoverTool

import pandas as pd

# Create your views here.

def exibir_grafico(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT estado, uf, regiao, populacao, ano
            FROM populacao_estados
            ORDER BY populacao DESC;
    """)
        resultados = cursor.fetchall()

    df = pd.DataFrame(
    resultados,
    columns=['estado', 'uf', 'regiao', 'populacao', 'ano']
    )

    estados = df['uf'].tolist()
    populacoes = df['populacao'].tolist()

    grafico = figure(
        x_range=estados,
        title="População dos estados brasileiros - 2025",
        x_axis_label="Estados",
        y_axis_label="População",
        height=500,
        sizing_mode="scale_width"
    )

    grafico.vbar(
        x=estados,
        top=populacoes,
        width=0.8,
    )

    hover = HoverTool(
    tooltips=[
        ("UF", "@x"),
        ("População", "@top{0,0}"),
    ]
)
    grafico.add_tools(hover)

    grafico.xgrid.grid_line_color = None
    grafico.y_range.start = 0
    grafico.yaxis.formatter = NumeralTickFormatter(format="0.0a")

    script, div = components(grafico)
    recursos_bokeh = CDN.render()

    print("Tamanho script:", len(script))
    print("Tamanho div:", len(div))
    print("Tamanho recursos:", len(recursos_bokeh))

    contexto = {
        "script": script,
        "div": div,
        "recursos_bokeh": recursos_bokeh,
    }

    

    return render(
        request,
        "graficos/exibir_grafico.html",
        contexto
    )

