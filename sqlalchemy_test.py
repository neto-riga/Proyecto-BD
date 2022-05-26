# %%
from sqlalchemy import create_engine
import pandas as pd
import pyodbc

# %%
DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-EKPLE5V'
DATABASE_NAME = 'AGENCIA'

DATABASE_CONNECTION = f"mssql://@{SERVER_NAME}/{DATABASE_NAME}?driver={DRIVER_NAME}"
engine = create_engine(DATABASE_CONNECTION)
conn = engine.connect()

# %%
connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""
con_odbc = pyodbc.connect(connection_string)

# %%
pd.read_sql_query("SELECT * FROM CARRO", conn)
# %%
cursor = con_odbc.cursor()
cursor.execute("""
UPDATE CARRO
SET modelo = 2024
WHERE matricula = 'HG8899'
""")
con_odbc.commit()
cursor.close()