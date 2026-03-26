# 📊 Análise do Brasileirão com Python

Projeto de análise exploratória de dados do Campeonato Brasileiro utilizando Python.

## 🔧 Ferramentas
- Python
- Pandas
- Matplotlib

## 📁 Estrutura
- data/raw → base original
- data/processed → dados tratados
- notebooks → análises
- images → gráficos

## 📊 Análises realizadas
- Média de gols por temporada
- Resultados (casa x fora)
- Ranking de ataques
- Ranking de defesas
- Evolução temporal do campeonato

## 📈 Principais insights

- A média de gols sofreu variações ao longo das temporadas, com tendência de queda em determinados períodos
- Clubes com maior consistência defensiva se destacam quando analisados por média de gols sofridos
- A análise evidencia a importância de normalizar dados para evitar interpretações distorcidas

## 📌 Metodologia

Inicialmente, foi analisado o total de gols sofridos por equipe, porém esse critério pode favorecer clubes com menor número de participações.

Para uma análise mais justa, foi utilizada a média de gols sofridos por jogo, com filtro mínimo de partidas disputadas.

Essa abordagem permite uma comparação mais precisa entre os clubes ao longo das temporadas.

## 📸 Exemplo de visualização
![Média de gols por temporada](images/media_gols_temporada.png)

## Como executar
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
