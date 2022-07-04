import nest_asyncio
import pandas as pd

nest_asyncio.apply()
import twint
from datetime import datetime
import glob
import time

arquivo = 'Users_All.csv'

users = list(pd.read_csv(arquivo).UserTwitter)

lista_raspados = glob.glob('raspados/*.csv')

def deleta_dupli(raspados):
    print(f'Procurando tweets duplicados...')
    for df in lista_raspados:
        pd.read_csv(df, engine = 'python').drop_duplicates(subset = ['id', 'tweet', 'created_at']).to_csv(df, index = False)


deleta_dupli(raspados=lista_raspados)

c = twint.Config()
c.Store_csv = True
c.Stats = True
c.Limit = 2000
c.Profile_full = True
c.User_full = True
c.Retweets = True
c.Hide_output = False
c.Pandas = True
# c.Until = datetime.now().strftime("%Y-%m-%d")
c.Since = str(datetime(2022, 6, 8)) # Rodando dia 4/07/2022
# c.Resume = 'twint-request_urls.log'
c.Debug = True

inicio = time.time()

for user in users:
    try:
        print(f'[{datetime.now().strftime("%H:%M:%S")}] Baixando {user}')
        c.Username = user
        # c.Since = str(ano)+'-'+str(mes)+'-01'
        c.Output = 'raspados/'+user+'.csv'
        # c.Database = 'tweets.db'
        twint.run.Search(c)
    except Exception as e:
        response = e.response
        raise

deleta_dupli(raspados=lista_raspados)
print(f'A sessão durou {round((time.time()-inicio)/60)} minutos')