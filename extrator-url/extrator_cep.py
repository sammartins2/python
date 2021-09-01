endereço = "Hermes da Fonseca 509, apto 103, bessa, Rio de Janeiro, RJ, 53035190"

import re #Regular Expression -- RegEx

# 5 digitos + hifen (opcional) + 3 digitos

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

busca = padrao.search(endereço) #Match
if busca:
    cep = busca.group()
    print (cep)