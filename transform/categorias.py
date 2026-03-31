import pandas as pd

# =====================================================
# TRANSFORMAÇÃO — CATEGORIAS
# =====================================================

def transformar_categorias(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforma a aba 'Categorias' do Google Sheets.

    Regras aplicadas:
    - Renomeia colunas para snake_case
    - Valida IDs nulos (lança erro se encontrar)
    - Converte tipos corretos
    - Padroniza strings (Primeira letra maiúscula)
    - Converte strings vazias para NaN
    """

    print("🔄 Transformando Categorias...")

    df = df.copy()

    # =====================================================
    # 1. RENOMEAR COLUNAS (snake_case padronizado)
    # =====================================================
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # =====================================================
    # 2. VALIDAR IDs NULOS
    # =====================================================
    if df["categoria_id"].isnull().any():
        raise ValueError("❌ ERRO: Existem categoria_id nulos! Corrija na planilha antes de continuar.")

    # =====================================================
    # 3. CONVERTER TIPOS
    # =====================================================
    df["categoria_id"] = df["categoria_id"].astype("int64")

    # =====================================================
    # 4. STRINGS VAZIAS → NaN
    # =====================================================
    df["categoria"]      = df["categoria"].replace("", pd.NA)
    df["tipo_categoria"] = df["tipo_categoria"].replace("", pd.NA)

    # =====================================================
    # 5. PADRONIZAR STRINGS (Primeira letra maiúscula)
    # =====================================================
    df["categoria"]      = df["categoria"].str.strip().str.capitalize()
    df["tipo_categoria"] = df["tipo_categoria"].str.strip().str.capitalize()

    # =====================================================
    # 6. GARANTIR TIPOS FINAIS
    # =====================================================
    df["categoria"]      = df["categoria"].astype("string")
    df["tipo_categoria"] = df["tipo_categoria"].astype("string")

    print(f"   ✅ {len(df)} registros transformados")
    print(f"   ✅ Nulos em 'categoria': {df['categoria'].isnull().sum()}")
    print(f"   ✅ Nulos em 'tipo_categoria': {df['tipo_categoria'].isnull().sum()}")

    return df