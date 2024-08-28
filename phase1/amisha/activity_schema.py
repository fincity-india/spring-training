import pandas as pd
from sqlalchemy import TEXT, BigInteger, Column, DateTime, Float, Integer, String


def activity_schema(sample_chunk):
    columns = []
    for col_name in sample_chunk.columns:
        col_data = sample_chunk[col_name]
        if col_name in ['created_at_epoch', 'updated_at_epoch']:
            columns.append(Column(col_name, BigInteger))
        elif col_name == 'comment':
            columns.append(Column(col_name, TEXT))
        elif pd.api.types.is_integer_dtype(col_data) and not col_data.isna().all():
            columns.append(Column(col_name, Integer))
        elif pd.api.types.is_float_dtype(col_data) and not col_data.isna().all():
            columns.append(Column(col_name, Float))
        elif pd.api.types.is_datetime64_any_dtype(col_data) and not col_data.isna().all():
            columns.append(Column(col_name, DateTime))
        else:
            columns.append(Column(col_name, String(255)))
    return columns
