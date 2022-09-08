from fastapi import FastAPI

import sqlite3

conn = sqlite3.connect('contract_registry.db')
c = conn.cursor()


app = FastAPI()

@app.get("/")
def get_abi(contract_addr):
    c.execute("SELECT abi_json FROM contract_registry WHERE address = '{}'".format(contract_addr))
    return c.fetchall()