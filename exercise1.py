# -*- coding: utf-8 -*-'
mensagem=raw_input("escreva seu mensagem: ")
tamanho_de_mensagem=len(mensagem)
if tamanho_de_mensagem>=140:
    print("seu twett é muito grande para ser enviado")
elif tamanho_de_mensagem<5:
    print "Seu tweet é muito pequeno "+str(tamanho_de_mensagem)+" caracteres para ser enviado"
else:
    print "sucesso seu twett foi enviado"
print "o tamanho foi de "+str(tamanho_de_mensagem)+" caracteres"