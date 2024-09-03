import pandas as pd
from sqlalchemy import TEXT, BigInteger, Column, DateTime, Float, Integer, String


<<<<<<< Updated upstream
def schema_creator(sample_chunk):
=======
def schemaCreator(sample_chunk):
>>>>>>> Stashed changes
    columns = []
    for col_name in sample_chunk.columns:
        col_data = sample_chunk[col_name]
        if col_name == 'phone_number' or col_name == 'whatsapp_number' or col_name=='alternate_phone_number':
            columns.append(Column(col_name, String(150)))
        elif col_name == 'created_at_epoch' or col_name == 'updated_at_epoch':
            columns.append(Column(col_name, BigInteger))
        elif col_name == 'comment':
            columns.append(Column(col_name, TEXT))
        elif col_name == 'latest_comment':
            columns.append(Column(col_name, TEXT))
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