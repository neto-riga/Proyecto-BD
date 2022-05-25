# %%
import pypyodbc as odbc
import pandas as pd
import PySimpleGUI as sg
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
print(Q1.head())
# %%
sg.theme("DarkBlue3")
headings = Q1.columns.to_list()
layout1 = [[sg.Table(values = Q1.values.tolist(), headings = headings,
    # Set column widths for empty record of table
    auto_size_columns=False,
    col_widths=list(map(lambda x:len(x)+1, headings)))]]
sg.Window(title='Hellow bitches!', layout=layout1).read()
# %%
