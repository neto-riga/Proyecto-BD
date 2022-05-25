# %%
from sqlalchemy import create_engine
import pandas as pd

# %%
DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-EKPLE5V'
DATABASE_NAME = 'AGENCIA'

DATABASE_CONNECTION = f"mssql://@{SERVER_NAME}/{DATABASE_NAME}?driver={DRIVER_NAME}"
engine = create_engine(DATABASE_CONNECTION)
conn = engine.connect()

# %%
pd.read_sql_query("SELECT * FROM CARRO", conn)
# %%
