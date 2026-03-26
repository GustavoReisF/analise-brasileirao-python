import pandas as pd


def carregar_dados(caminho_arquivo: str) -> pd.DataFrame:
    df = pd.read_csv(caminho_arquivo)
    return df


def padronizar_colunas(df: pd.DataFrame) -> pd.DataFrame:
    mapa_colunas = {
        "mandante": "home_team",
        "visitante": "away_team",
        "mandante_Placar": "home_goals",
        "visitante_Placar": "away_goals",
        "data": "match_date",
        "rodada": "matchday",
        "ano_campeonato": "season",
        "campeonato": "competition"
    }

    colunas_existentes = {k: v for k, v in mapa_colunas.items() if k in df.columns}
    df = df.rename(columns=colunas_existentes)
    return df


def criar_variaveis_analiticas(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["home_goals"] = pd.to_numeric(df["home_goals"], errors="coerce")
    df["away_goals"] = pd.to_numeric(df["away_goals"], errors="coerce")

    df = df.dropna(subset=["home_goals", "away_goals"])

    df["total_goals"] = df["home_goals"] + df["away_goals"]

    def classificar_resultado(row):
        if row["home_goals"] > row["away_goals"]:
            return "Casa"
        elif row["home_goals"] < row["away_goals"]:
            return "Fora"
        return "Empate"

    df["match_result"] = df.apply(classificar_resultado, axis=1)

    return df


def calcular_ataques(df: pd.DataFrame) -> pd.Series:
    gols_casa = df.groupby("home_team")["home_goals"].sum()
    gols_fora = df.groupby("away_team")["away_goals"].sum()
    ataques = gols_casa.add(gols_fora, fill_value=0).sort_values(ascending=False)
    return ataques


def calcular_defesas(df: pd.DataFrame) -> pd.Series:
    sofridos_casa = df.groupby("home_team")["away_goals"].sum()
    sofridos_fora = df.groupby("away_team")["home_goals"].sum()
    defesas = sofridos_casa.add(sofridos_fora, fill_value=0).sort_values()
    return defesas


def resumo_resultados(df: pd.DataFrame) -> pd.Series:
    return df["match_result"].value_counts()


def media_gols(df: pd.DataFrame) -> float:
    return df["total_goals"].mean()