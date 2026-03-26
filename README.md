# 📊 Análise do Brasileirão com Python

Projeto de análise exploratória de dados do Campeonato Brasileiro utilizando Python, com foco em métricas ofensivas, defensivas e evolução da média de gols ao longo das temporadas.

## Objetivo
Explorar dados históricos do Brasileirão para identificar padrões de desempenho, comportamento de gols e variações ao longo dos anos.

## Ferramentas utilizadas
- Python
- Pandas
- Matplotlib
- Jupyter Notebook

## Estrutura do projeto
- `data/raw`: base original
- `data/processed`: saídas tratadas
- `notebooks`: análises
- `images`: gráficos gerados
- `src`: funções auxiliares

## Análises realizadas
- Média de gols por temporada
- Resultados de mandante, visitante e empates
- Ranking de ataques
- Ranking de defesas
- Melhores defesas por ano
- Melhores ataques por ano

## Principais insights
- Houve queda na média de gols em parte do período analisado.
- Após 2020, observa-se leve recuperação na média de gols.
- O campeonato apresenta alternância entre equipes com melhor desempenho defensivo.
- A análise histórica mostra mudanças no perfil ofensivo do Brasileirão ao longo do tempo.

## Exemplo de visualização
![Média de gols por temporada](images/media_gols_temporada.png)

## Como executar
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
