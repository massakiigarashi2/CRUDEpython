# myFirstStreamlitApp.py
#import the libraries
import streamlit as st
import sqlite3
import pandas as pd
import time
import pandas as pd
import numpy as np

vet = str(np.zeros(4))
def exibir():
    conn = sqlite3.connect('ListaCompras.db')
    cursor = conn.execute(""" SELECT * FROM L_COMPRAS """)
    rows = cursor.fetchall()
    for row in cursor:
       st.write("ID: ", row[0])
       st.write("QTD: ", row[1])
       st.write("UNIDADE: ", row[2])
       st.write("DESCRIÇÃO: ", row[3])
       st.write("VALOR: ", row[4])
       st.write("Situação: ", row[5])   
    if len(rows) != 0:
        db = pd.DataFrame(rows)    
        db.columns = ['ID' , 'QTD' , 'UNIDADE', 'DESCRIÇÃO' , 'VALOR ESTIMADO', 'SITUACAO']
        st.dataframe(db)
    conn.close()

#1º)Para criar um banco de dados SQL , usamos o seguinte comando:
conn = sqlite3.connect('ListaCompras.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS L_COMPRAS(ID INT PRIMARY KEY     NOT NULL,
                                                       QTD            REAL    NOT NULL,
                                                       UNIDADE        TEXT    NOT NULL,
                                                       DESCRICAO      TEXT    NOT NULL,
                                                       VALOR          REAL    NOT NULL,
                                                       SITUACAO       TEXT    NOT NULL);''')
conn.close()

#2º)INSERT data and READ this data
#   Following Python program shows how to create records in the COMPANY table created in the above example.
conn = sqlite3.connect('ListaCompras.db')
tab1, tab2 = st.tabs(["Cadastrar", "EXIBIR"])
with tab1:
    txtID = st.text_input("ID: ")
    txtQTD = st.text_input("Quantidade")
    txtUN = st.text_input("Unidade")
    txtDESC = st.text_input("Descrição do produto: ")
    txtVAL = st.text_input("Valor estimado do produto: ")
    txtSITUACAO = st.text_input("SITUAÇÃO: ")
    if st.button('Salvar'):
        conn.execute("""INSERT INTO L_COMPRAS (ID, QTD, UNIDADE, DESCRICAO, VALOR, SITUACAO) \
                        VALUES (?,?,?,?,?,?)
                        """, (txtID, txtQTD, txtUN, txtDESC, txtVAL, txtSITUACAO))
        conn.commit()
        st.write("Records created successfully")
        conn.close()
        exibir() 
with tab2: 
    exibir()