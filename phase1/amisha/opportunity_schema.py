import pandas as pd
from sqlalchemy import TEXT, Column, DateTime, Float, Integer, String

def opportunity_schema(sample_chunk):
    columns = []
    for col_name in sample_chunk.columns:
        col_data = sample_chunk[col_name]
        if col_name in ['phone_number', 'whatsapp_number', 'alternate_phone_number']:
            columns.append(Column(col_name, String(150)))
        elif col_name == 'metadata':
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