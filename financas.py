import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Carregar o dataset
file_path = 'fatura.csv'
df = pd.read_csv(file_path)

# Manipulação de dados
df['data_compra'] = pd.to_datetime(df['data_compra'])

# Funções para gráficos
def gastos_por_categoria_filtrado(df, nome_selecionado, categoria_selecionada):
    df_filtrado = df if nome_selecionado == "Todos" else df[df['Nome'] == nome_selecionado]
    if categoria_selecionada != "Todas":
        df_filtrado = df_filtrado[df_filtrado['categoria'] == categoria_selecionada]
    
    categoria_sum = df_filtrado.groupby('categoria')['ValorCompra'].sum().sort_values()
    fig = px.bar(categoria_sum, orientation='h', labels={'value':'Total Gasto', 'index':'Categoria'})
    fig.update_layout(template='plotly_dark', title="Gastos por Categoria")
    return fig

def gastos_por_pessoa(df, categoria_selecionada):
    if categoria_selecionada == "Todas":
        pessoa_sum = df.groupby('Nome')['ValorCompra'].sum()
    else:
        pessoa_sum = df[df['categoria'] == categoria_selecionada].groupby('Nome')['ValorCompra'].sum()
    
    fig = px.pie(values=pessoa_sum, names=pessoa_sum.index, labels={'value':'Valor Gasto', 'Nome':'Pessoa'})
    fig.update_layout(template='plotly_dark', title="Distribuição de Gastos por Pessoa")
    return fig

def total_fatura(df, nome_selecionado, categoria_selecionada):
    df_filtrado = df if nome_selecionado == "Todos" else df[df['Nome'] == nome_selecionado]
    if categoria_selecionada != "Todas":
        df_filtrado = df_filtrado[df_filtrado['categoria'] == categoria_selecionada]
    
    total = df_filtrado['ValorCompra'].sum()
    return total

def dias_com_mais_gastos(df, nome_selecionado, categoria_selecionada):
    df_filtrado = df if nome_selecionado == "Todos" else df[df['Nome'] == nome_selecionado]
    if categoria_selecionada != "Todas":
        df_filtrado = df_filtrado[df_filtrado['categoria'] == categoria_selecionada]

    gastos_por_dia = df_filtrado.groupby(df_filtrado['data_compra'].dt.date)['ValorCompra'].sum()
    fig = px.scatter(gastos_por_dia, labels={'index':'Data', 'value':'Valor Gasto'})
    fig.update_layout(template='plotly_dark', title="Gastos por Dia")
    return fig

def maiores_compras(df, nome_selecionado, categoria_selecionada):
    df_filtrado = df if nome_selecionado == "Todos" else df[df['Nome'] == nome_selecionado]
    if categoria_selecionada != "Todas":
        df_filtrado = df_filtrado[df_filtrado['categoria'] == categoria_selecionada]

    top_compras = df_filtrado.nlargest(5, 'ValorCompra')
    fig = px.bar(top_compras, x='estabelecimento', y='ValorCompra', labels={'ValorCompra':'Valor da Compra', 'estabelecimento':'Estabelecimento'})
    fig.update_layout(template='plotly_dark', title="Top 5 Compras de Maior Valor")
    return fig

def tabela_completa(df, nome_selecionado, categoria_selecionada):
    df_filtrado = df if nome_selecionado == "Todos" else df[df['Nome'] == nome_selecionado]
    if categoria_selecionada != "Todas":
        df_filtrado = df_filtrado[df_filtrado['categoria'] == categoria_selecionada]

    table = dash.dash_table.DataTable(
        data=df_filtrado.to_dict('records'),
        columns=[{'name': i, 'id': i} for i in df.columns],
        filter_action='native',
        sort_action='native',
        page_size=10,
        style_header={
            'backgroundColor': 'rgb(30, 30, 30)',
            'color': 'white',
        },
        style_data={
            'backgroundColor': 'rgb(50, 50, 50)',
            'color': 'white',
        },
    )
    return table

# Lista de nomes e categorias únicas, adicionando a opção "Todos" e "Todas"
nomes = df['Nome'].unique()
nomes = ['Todos'] + list(nomes)

categorias = df['categoria'].unique()
categorias = ['Todas'] + list(categorias)

# Layout do Dash com menu lateral
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H2("Menu Lateral", className="text-light"),
                
                # Caixa de seleção para nome
                html.Label("Selecione um nome:", className="text-light"),
                dcc.Dropdown(
                    id='nome-selecao',
                    options=[{'label': nome, 'value': nome} for nome in nomes],
                    value='Todos',  # Valor inicial
                    clearable=False,
                    style={'margin-bottom': '20px', 'color': 'black', 'background-color': 'white'}
                ),

                # Caixa de seleção para categoria
                html.Label("Selecione uma categoria:", className="text-light"),
                dcc.Dropdown(
                    id='categoria-selecao',
                    options=[{'label': categoria, 'value': categoria} for categoria in categorias],
                    value='Todas',  # Valor inicial
                    clearable=False,
                    style={'margin-bottom': '20px', 'color': 'black', 'background-color': 'white'}
                ),
            ], style={'background-color': '#1c1e22', 'padding': '20px', 'height': '100vh'})
        ], width=2),

        # Área de gráficos
        dbc.Col([
            dbc.Row([
                dbc.Col(dcc.Graph(id='grafico-categoria'), width=6),
                dbc.Col(dcc.Graph(id='grafico-pessoa'), width=6),
            ]),

            dbc.Row([
                dbc.Col(html.H2(id='total-fatura-card', className="text-center text-light bg-dark py-3"), width=12),
            ]),

            dbc.Row([
                dbc.Col(dcc.Graph(id='grafico-dias-gastos'), width=6),
                dbc.Col(dcc.Graph(id='grafico-maiores-compras'), width=6),
            ]),

            dbc.Row([
                dbc.Col(html.Div(id='tabela-dados'), width=12),
            ]),
        ], width=10),
    ])
], fluid=True)

# Callback para atualizar todos os gráficos com base na seleção de nome e categoria
@app.callback(
    [
        Output('grafico-categoria', 'figure'),
        Output('grafico-pessoa', 'figure'),
        Output('total-fatura-card', 'children'),
        Output('grafico-dias-gastos', 'figure'),
        Output('grafico-maiores-compras', 'figure'),
        Output('tabela-dados', 'children')
    ],
    [Input('nome-selecao', 'value'), Input('categoria-selecao', 'value')]
)
def update_dashboard(nome_selecionado, categoria_selecionada):
    fig_categoria = gastos_por_categoria_filtrado(df, nome_selecionado, categoria_selecionada)
    fig_pessoa = gastos_por_pessoa(df, categoria_selecionada)
    total_fatura_valor = f"Valor Total da Fatura: R$ {total_fatura(df, nome_selecionado, categoria_selecionada):.2f}"
    fig_dias = dias_com_mais_gastos(df, nome_selecionado, categoria_selecionada)
    fig_compras = maiores_compras(df, nome_selecionado, categoria_selecionada)
    tabela = tabela_completa(df, nome_selecionado, categoria_selecionada)

    return fig_categoria, fig_pessoa, total_fatura_valor, fig_dias, fig_compras, tabela

if __name__ == '__main__':
    app.run_server(debug=True)
