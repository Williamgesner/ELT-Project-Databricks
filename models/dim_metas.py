# Responsável por definir a estrutura de tabelas dim_metas no schema processed

import pandas as pd
from datetime import datetime

# =====================================================
# MODELO TA TABELA — DIM_METAS
# =====================================================

SCHEMA_DIM_METAS = {
    "data_referencia"    : {"tipo": "datetime",  "nullable": False, "pk": True, "fk": None},
    "ano"                : {"tipo": "int64",     "nullable": False, "pk": False, "fk": None},
    "mes"                : {"tipo": "int64",     "nullable": False, "pk": False, "fk": None},
    "meta_faturamento"   : {"tipo": "float",     "nullable": False, "pk": False, "fk": None},
    "data_ingestao"      : {"tipo": "datetime",  "nullable": False, "pk": False, "fk": None},
    "data_processamento" : {"tipo": "datetime",  "nullable": False, "pk": False, "fk": None},
}

def aplicar_schema_dim_metas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica o schema final da dim_metas.
    
    - Garante os tipos finais de cada coluna
    - Adiciona metadados de processamento
    """

    print("🔄 Aplicando schema — dim_metas...")

    df = df.copy()

    # =====================================================
    # 1. GARANTIR TIPOS FINAIS
    # =====================================================
    df["data_referencia"]  = pd.to_datetime(df["data_referencia"]).dt.date
    df["ano"]              = df["ano"].astype("int64")
    df["mes"]              = df["mes"].astype("int64")
    df["meta_faturamento"] = df["meta_faturamento"].astype("float")
    
    # =====================================================
    # 2. METADADOS
    # =====================================================
    agora = datetime.now()
    df["data_ingestao"]      = agora
    df["data_processamento"] = agora

    print(f"   ✅ Schema aplicado! {len(df)} registros | Colunas: {list(df.columns)}")

    return df