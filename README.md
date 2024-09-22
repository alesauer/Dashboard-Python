
# 💰 Painel de Gastos Pessoais com Dash

Este repositório contém um projeto desenvolvido com o framework **Dash** para visualização de dados de uma fatura de compras. O objetivo do painel é ajudar os usuários a visualizar e analisar seus gastos pessoais de forma interativa, utilizando gráficos de barras, pizza, e tabelas dinâmicas.

## 📋 Conteúdo

1. [Descrição do Projeto](#descrição-do-projeto)
2. [Instalação](#instalação)
3. [Estrutura do Código](#estrutura-do-código)
4. [Visualizações](#visualizações)
5. [Conclusão](#conclusão)

## 🖥️ Descrição do Projeto

Este projeto utiliza dados de um arquivo CSV (`fatura.csv`) que contém informações sobre as compras realizadas. O Dash é usado para criar gráficos interativos que permitem a análise dos gastos por categoria, pessoa e dia. As funcionalidades principais incluem:

- Filtros dinâmicos por **Nome** e **Categoria**.
- Gráfico de barras mostrando os gastos totais por categoria.
- Gráfico de pizza exibindo a distribuição de gastos por pessoa.
- Exibição dos dias com mais gastos e as 5 maiores compras.
- Tabela com todos os dados filtrados.

## 🛠️ Instalação

### Pré-requisitos:

- Python 3.7 ou superior
- Pip (gerenciador de pacotes do Python)

### Passos para instalação:

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/painel-de-gastos.git
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Coloque o arquivo `fatura.csv` na mesma pasta do arquivo `financasv3.py`.

4. Execute o aplicativo:
   ```bash
   python financasv3.py
   ```

5. Acesse o painel no seu navegador no endereço:
   ```
   http://127.0.0.1:8050/
   ```

## 🧾 Estrutura do Código

- `financasv3.py`: Código principal da aplicação Dash, que carrega os dados, define os gráficos e executa o servidor.
- `fatura.csv`: Arquivo CSV contendo as informações de compras.
- `README.md`: Este arquivo de documentação.
- `requirements.txt`: Lista de dependências necessárias para o projeto.

## 📊 Visualizações

O painel inclui as seguintes visualizações:

1. **Gastos por Categoria**: Gráfico de barras horizontal que exibe o total gasto por categoria.
   
   ![Gráfico de Gastos por Categoria](exemplo_categoria.png)

2. **Distribuição de Gastos por Pessoa**: Gráfico de pizza que mostra como os gastos estão distribuídos entre diferentes pessoas.
   
   ![Gráfico de Gastos por Pessoa](exemplo_pessoa.png)

3. **Dias com Mais Gastos**: Gráfico de dispersão mostrando os dias em que os maiores gastos foram feitos.

4. **Top 5 Compras de Maior Valor**: Gráfico de barras mostrando as 5 compras mais caras em termos de valor.

5. **Tabela de Gastos**: Uma tabela filtrada por nome e categoria, com a possibilidade de busca e ordenação dos dados.

## 🏁 Conclusão

Este painel de controle fornece uma maneira eficaz de visualizar e analisar os gastos pessoais de forma interativa. Ele pode ser expandido para incluir mais categorias, mais gráficos e outras funcionalidades conforme as necessidades dos usuários.
