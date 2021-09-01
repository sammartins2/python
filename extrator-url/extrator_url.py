import re

class extratorURL:
    def __init__(self,url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)
        if not match:
            raise ValueError ("A URL não é valida.")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else: 
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parametros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url        


url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=euro"

extrator_url = extratorURL(url)
extrator_url_2 = extratorURL(url)

print(extrator_url == extrator_url_2)
#print("O tamanho da URL: ", len(extrator_url))
#print(extrator_url)


#valor_quantidade = extrator_url.get_valor_parametro("quantidade")

#print(valor_quantidade)

url = "bytebank.com/cambio?quantidade=500&moedaOrigem=euro&moedaDestino=real"
extrator_url = extratorURL(url)

VALOR_EURO = 6.12  # 1 EURO = 5.17 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

if moeda_origem == "real" and moeda_destino == "euro":
    valor_conversao = int(quantidade) / VALOR_EURO
    print("O valor de R$" + quantidade + " reais é igual a $" + str(valor_conversao) + " euros.")
elif moeda_origem == "euro" and moeda_destino == "real":
    valor_conversao = int(quantidade) * VALOR_EURO
    print("O valor de $" + quantidade + " euros é igual a R$" + str(valor_conversao) + " reais.")
else:
    print(f"Câmbio de {moeda_origem} para {moeda_destino} não está disponível.")