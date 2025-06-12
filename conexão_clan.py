import requests
import pprint

# :) chave api
api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjhlYzAxN2E5LTg5YTYtNDI2OC1hZGFiLWI5NTMzNjlkNzA5NSIsImlhdCI6MTc0OTY1NzA3NSwic3ViIjoiZGV2ZWxvcGVyLzQ4NjllZmI3LTE4YzktY2I2NC1hNDFjLWNhZGE0NmE4YjI0OSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjQ1LjIzOS4xNDguMjgiXSwidHlwZSI6ImNsaWVudCJ9XX0.QEU8OLd8MjDFgCrIEP3du0NVpSM1UAGuy2ExyFZwd0T7IrMLhDFJ3u1Esp30SZbbrTMYs4jVn_NJcqznPdVAzw"

# :) tag da minha conta Kalimbinha em asciid #2RQQRUUYR
clan_tag = "%232RQQRUUYR" 

# :) URL da API 
url = f"https://api.clashofclans.com/v1/clans/{clan_tag}"

# :) Cabeçalhos HTTP com autenticação
headers = {
    "Authorization": f"Bearer {api_key}",
    "Accept": "application/json"
    
}

# :) Requisição GET
response = requests.get(url, headers=headers)   

# :) Exibindo os dados
if response.status_code == 200:
    data = response.json()
    pprint.pprint(data)

else:
    print("Erro:", response.status_code, response.text)
