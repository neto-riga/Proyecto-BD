# %%
import pypyodbc as odbc
import pandas as pd
import PySimpleGUI as sg
import os
# %%
# DRIVER_NAME = 'SQL SERVER'
# SERVER_NAME = 'DESKTOP-EKPLE5V'
# DATABASE_NAME = 'AGENCIA'

# connection_string = f"""
#     DRIVER={{{DRIVER_NAME}}};
#     SERVER={SERVER_NAME};
#     DATABASE={DATABASE_NAME};
#     Trust_Connection=yes;
# """

# conn = odbc.connect(connection_string)

# # %%
# Q1 = pd.read_sql_query('''SELECT * FROM CLIENTE''', conn)
# print(Q1.head())

# %%
layout = [
    [sg.Button('Inserción'), sg.Button('Visualización')],
    [sg.Button('Cerrar')]
]

v_principal = sg.Window('Menu Principal', layout)
while True:
    event, values = v_principal.read()
    if event == 'Cerrar' or event == sg.WINDOW_CLOSED:
        break
    elif event == 'Inserción':
        layout2 = [
            [sg.Text('Seleccione la tabla a la cual añadirá datos')],
            [sg.Button('CLIENTE'), sg.Button('CARRO'), sg.Button('COMPRA'),
            sg.Button('MECANICO'), sg.Button('REPARACION')],
            [sg.Button('Regresar')]
        ]
        v_menu_insercion = sg.Window('Menu Inserción', layout2)
        while True:
            event2, values2 = v_menu_insercion.read()
            if event2 == 'Regresar' or event2 == sg.WINDOW_CLOSED:
                break
            elif event2 == 'CLIENTE':
                pass
v_principal.close()

# %%
# sg.theme("DarkBlue3")
# headings = Q1.columns.to_list()
# layout1 = [
#     [sg.Table(values = Q1.values.tolist(), headings = headings,
#     # Set column widths for empty record of table
#     auto_size_columns=True,
#     #col_widths=list(map(lambda x:len(x)+1, headings)))
#     )]

#     ]
# sg.Window(title='Hellow bitches!', layout=layout1).read()
# %%
