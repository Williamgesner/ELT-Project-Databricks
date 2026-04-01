# Responsável por definir a estrutura de tabelas dim_categorias no schema processed

import pandas as pd
from datetime import datetime

# =====================================================
# MODELO TA TABELA — DIM_CATEGORIAS
# =====================================================

SCHEMA_DIM_CATEGORIAS = {
    "categoria_id"      : {"tipo": "int64",    "nullable": False, "pk": True,  "fk": None},
    "categoria"         : {"tipo": "string",   "nullable": False, "pk": False, "fk": None},
    "tipo_categoria"    : {"tipo": "string",   "nullable": False, "pk": False, "fk": None},
    "data_ingestao"     : {"tipo": "datetime", "nullable": False, "pk": False, "fk": None},
    "data_processamento": {"tipo": "datetime", "nullable": False, "pk": False, "fk": None},
}

def aplicar_schema_dim_categorias(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica o schema final da dim_categorias.
    
    - Garante os tipos finais de cada coluna
    - Adiciona metadados de processamento
    """

    print("🔄 Aplicando schema — dim_categorias...")

    df = df.copy()

    # =====================================================
    # 1. GARANTIR TIPOS FINAIS
    # =====================================================
    df["categoria_id"]   = df["categoria_id"].astype("int64")
    df["categoria"]      = df["categoria"].astype("string")
    df["tipo_categoria"] = df["tipo_categoria"].astype("string")

    # =====================================================
    # 2. METADADOS
    # =====================================================
    agora = datetime.now()
    df["data_ingestao"]      = agora
    df["data_processamento"] = agora

    print(f"   ✅ Schema aplicado! {len(df)} registros | Colunas: {list(df.columns)}")

    return df