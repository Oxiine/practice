# -*- coding: utf-8 -*-'
mensagem=raw_input("escreva seu mensagem: ")
tamanho_de_mensagem=len(mensagem)
if (tamanho_de_mensagem<5)or(tamanho_de_mensagem>=140):
    print("nao foi enviado, porque é menor que 5 caracteres ou maior que 140 caracteres")
else:
    print "sucesso seu twett foi enviado"
print "o tamanho foi de "+str(tamanho_de_mensagem)+" caracteres"