import pandas as pd
import sqlite3

def export_to_excel(filename='clientes.xlsx'):
    conn = sqlite3.connect("clientes.db")
    df = pd.read_sql_query("SELECT * FROM clientes", conn)
    df.to_excel(filename, index=False)
    conn.close()