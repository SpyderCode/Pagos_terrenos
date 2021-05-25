import db_tools as db_tool
import discord
import json
from datetime import datetime

def get_token():
    with open("token.json") as json_file:
        data = json.load(json_file)

    return data["token"]

token = get_token()
conn = db_tool.create_connection()
client = discord.Client()
pagos_channel = client.get_channel("846812228728127498")

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
        
    if message.author == client.user:
        return

    print(message.content)

    if message.content.startswith("!Pago"):
        valor_pago = message.content.split()[1]
        try:
            test = int(valor_pago)
        except Exception as e:
            await message.channel.send("ERROR: Valor no numerico")
            return
        
        today = datetime.today().strftime('%Y-%m-%d')
        db_tool.insert_pagos(conn,today,valor_pago)
        await message.channel.send(f"Listo! {valor_pago} fue agregado a la base de datos ")

    if message.content.startswith("!Total"):
        sumatoria_pagos = db_tool.sum_pagos(conn)
        await message.channel.send(f"Total de este mes es: {sumatoria_pagos}")





if __name__ == '__main__':
    client.run(token)
