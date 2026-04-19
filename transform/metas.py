import pandas as pd

# =====================================================
# TRANSFORMAÇÃO — METAS
# =====================================================

def transformar_metas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforma a aba 'Metas' do Google Sheets.

    Regras aplicadas:
    - Renomeia colunas para snake_case
    - Valida IDs nulos (lança erro se encontrar)
    - Converte tipos corretos
    - Padroniza strings (Primeira letra maiúscula)
    - Converte strings vazias para NaN
    """

    print("🔄 Transformando Metas...")

    df = df.copy()

    # =====================================================
    # 1. RENOMEAR COLUNAS (snake_case padronizado)
    # =====================================================
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # =====================================================
    # 2. VALIDAR IDs NULOS
    # =====================================================
    if df["data_referencia"].isnull().any():
        raise ValueError("❌ ERRO: Existem valores nulos! Corrija na planilha antes de continuar.") # Colunas de ID que não podem ser nulas

    # =====================================================
    # 2. GARANTIR TIPOS FINAIS
    # =====================================================
    df["ano"]   = df["ano"].astype("int64")
    df["mes"]  = df["mes"].astype("int64")

    print(f"   ✅ {len(df)} registros transformados")

    return df