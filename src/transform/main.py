import pandas as pd
import sqlite3 
from datetime import datetime

df = pd.read_json('../data/data.jsonl', lines=True)

pd.options.display.max_columns = None

df['source'] = "https://lista.mercadolivre.com.br/acessorios-veiculos/som-automotivo/_Loja_all_NoIndex_True?original_category_landing=true#applied_filter_id%3Dofficial_store%26applied_filter_name%3DLojas+oficiais%26applied_filter_order%3D9%26applied_value_id%3Dall%26applied_value_name%3DSomente+lojas+oficiais%26applied_value_order%3D1%26applied_value_results%3D320372%26is_custom%3Dfalse"
df['date'] = datetime.now()

df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)
df['old_price_centavos'] = df['old_price_centavos'].fillna(0).astype(float)
df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
df['new_price_centavos'] = df['new_price_centavos'].fillna(0).astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)


df['reviews_amount'] = df['reviews_amount'].str.replace('[\(\)]', '', regex=True)
df['reviews_amount'] = df['reviews_amount'].fillna(0).astype(int)


df['old_price'] = df['old_price_reais'] + df['old_price_centavos'] / 100
df['new_price'] = df['new_price_reais'] + df['new_price_centavos'] / 100


df.drop(columns=['old_price_reais', 'old_price_centavos', 'new_price_reais', 'new_price_centavos'], inplace=True)


#salvar um arquivo json do dataframe tratado
df.to_json('../data/data_transformed.json', lines=True, orient='records')


