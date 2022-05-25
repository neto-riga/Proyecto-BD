# %%
from sqlalchemy import create_engine
import pandas as pd
import PySimpleGUI as sg
import os
# %%
DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-EKPLE5V'
DATABASE_NAME = 'AGENCIA'

DATABASE_CONNECTION = f"mssql://@{SERVER_NAME}/{DATABASE_NAME}?driver={DRIVER_NAME}"
engine = create_engine(DATABASE_CONNECTION)
conn = engine.connect()

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
                layout_cliente = [
                    [sg.Text('Ingrese los valores que desee añadir', font=(sg.DEFAULT_FONT, 15))],
                    [sg.Text('Nombre completo', size=(20, 1)), sg.Input(key='-NOMBRE-')],
                    [sg.Text('RFC', size=(20, 1)), sg.Input(key='-RFC-')],
                    [sg.Text('Direccion', size=(20, 1)), sg.Input(key='-DIR-')],
                    [sg.Text('Teléfono', size=(20, 1)), sg.Input(key='-TEL-')],
                    [sg.Button('Ingresar'), sg.Button('Cancelar')]
                ]
                v_datos_cliente = sg.Window('Inserción Cliente', layout_cliente)
                while True:
                    event_insercion, values_insercion = v_datos_cliente.read()
                    if event_insercion == 'Cancelar' or event_insercion == sg.WINDOW_CLOSED:
                        break
                    elif event_insercion == 'Ingresar': 
                        ### HACER CONSULTA AQUÍ
                        sg.popup_auto_close("Cliente añadido con éxito")
                v_datos_cliente.close()
            elif event2  == 'CARRO':
                layout_carro = [
                    [sg.Text('Ingrese los valores que desee añadir', font=(sg.DEFAULT_FONT, 15))],
                    [sg.Text('Matrícula', size=(20, 1)), sg.Input(key='-MATRICULA-')],
                    [sg.Text('Modelo', size=(20, 1)), sg.Input(key='-MODELO-')],
                    [sg.Text('Color', size=(20, 1)), sg.Input(key='-COLOR-')],
                    [sg.Text('Precio', size=(20, 1)), sg.Input(key='-PRECIO-')],
                    [sg.Text('Marca', size=(20, 1)), sg.Input(key='-MARCA-')],
                    [sg.Button('Ingresar'), sg.Button('Cancelar')]
                ]
                v_datos_carro = sg.Window('Inserción Cliente', layout_carro)
                while True:
                    event_insercion, values_insercion = v_datos_carro.read()
                    if event_insercion == 'Cancelar' or event_insercion == sg.WINDOW_CLOSED:
                        break
                    elif event_insercion == 'Ingresar': 
                        ### HACER CONSULTA AQUÍ
                        sg.popup_auto_close("Cliente añadido con éxito")
                v_datos_carro.close()
            elif event2 == 'COMPRA':
                rfc_cliente = pd.read_sql_query('''SELECT RFC FROM CLIENTE''', conn)

                layout_cliente = [
                    [sg.Text('Ingrese los valores que desee añadir', font=(sg.DEFAULT_FONT, 15))],
                    [sg.Text('Fecha de Compra', size=(20, 1)), sg.Input(key='-FECHA_COMPRA-')],
                    [sg.Text('Forma de Pago', size=(20, 1)), sg.Input(key='-PAGO-')],
                    [sg.Text('RFC Cliente', size=(20, 1)), sg.Listbox(rfc_cliente.values.tolist(), key='-RFC_CLIENTE-', size=(15, 2))],
                    [sg.Text('Teléfono', size=(20, 1)), sg.Input(key='-TEL-')],
                    [sg.Button('Ingresar'), sg.Button('Cancelar')]
                ]
                v_datos_cliente = sg.Window('Inserción Cliente', layout_cliente)
                while True:
                    event_insercion, values_insercion = v_datos_cliente.read()
                    if event_insercion == 'Cancelar' or event_insercion == sg.WINDOW_CLOSED:
                        break
                    elif event_insercion == 'Ingresar':
                        for llave, val in values_insercion.items():
                            print(f"{llave}  {val}")
                        ### HACER CONSULTA AQUÍ
                        sg.popup_auto_close("Cliente añadido con éxito")
                v_datos_cliente.close()
        v_menu_insercion.close()
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
