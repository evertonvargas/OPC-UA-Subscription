## 🚀 Como funciona

O servidor a cada 2 segundos envia valores de temperatura e umidade aleatórios. O cliente plota em um gráfico de linhas os primeiros 15 valores gerados.

## :arrow_forward: Instalação e uso

Para instalar as bibliotecas python necessárias, execute:
```bash
pip install -r requirements.txt
```
Ou pode instalar manualmente via pip
```bash
pip install plotly
pip install opcua
pip install pandas
pip install datetime
```
Execute o servidor:
```bash
python server.py
```
Execute o client:
```bash
python client.py
```
