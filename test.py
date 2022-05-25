# %%
import pypyodbc as odbc
import pandas as pd

# %%
DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-EKPLE5V'
DATABASE_NAME = 'AGENCIA'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""

conn = odbc.connect(connection_string)

# %%
Q1 = pd.read_sql_query('''SELECT * FROM CLIENTE''', conn)
Q1.head()
# %%
