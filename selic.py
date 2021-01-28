# -*- coding: utf-8 -*-


from urllib2 import Request

import datetime
import json 
import pprint
import numpy as np
from functools import reduce

#Listas
vl =[]
dvl =[]

#Calculo      
def TotalIndice_Selic(V,VC):
    del V[0]
    
    lista = [float(i) for i in V]
    #print(lista)
    TI= (sum(lista))
    I=(TI/100+1)
    #print(I)
    F =(I*VC)
    
    VF =(round(F,2))
    return VF
    #
    
def TotalIndice_IGPDI(V,VC):
    ln=[]

    lista = [float(i) for i in V]
    for xx in lista:
        x = (xx/100)+1
        ln.append((x))
   
    I= (reduce(lambda x, y: x*y, ln))
    VF =(I*VC)
    VF =(round(VF,2))
    return VF
     

#Convert string para data    
def ConvertStringToDate(d):
    date_time_obj = datetime.datetime.strptime(d, "%d/%m/%Y").strftime("%Y-%m-%d")
    return date_time_obj


#Captura dados da selic
def Captura_Selic(di,df,v):

    url='https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial='+di+'&dataFinal='+df
    print("Resultado da Correção pela Selic")
    response = urlib.request.urlopen(url)
   
    print(url)
    data = (json.loads(response))
    pprint.pprint(data)  
    
   
    for dados in data:
        dt = (dados['data'])
        vlr = str(dados['valor'])
        

        if ConvertStringToDate(dt) <= ConvertStringToDate(di)  :
            pass
             
        else:  
            vl.append(vlr)
            dvl.append(dt) 
   #pprint.pprint(data)
    VP =TotalIndice_Selic(vl,v)
    print("Valor Inicial: R$ "+ str(v),"Data Inicio:"+ str(di), "Data Final:"+str(df), "Valor Corrigido: R$" + str(VP)  )


 

def Captura_IGPDI(di,df,v):
    print("Resultado da Correção pelo IGP-DI (FGV)")
    url='https://api.bcb.gov.br/dados/serie/bcdata.sgs.190/dados?formato=json&dataInicial='+di+'&dataFinal='+df
    print(url)
    response = urlib.request.urlopen(url)
    data = (json.loads(response))
    pprint.pprint(data)
  
    
    for dados in data:
        dt = (dados['data'])
        vlr = str(dados['valor'])
        vl.append(vlr)
        dvl.append(dt) 
        VP =TotalIndice_IGPDI(vl,v)
    print("Valor Inicial: R$ "+ str(v),"Data Inicio:"+ str(di), "Data Final:"+str(df), "Valor Corrigido: R$" + str(VP)  )


  
  
  
di="01/01/2021"
df="25/01/2021"
v1 = 200
Captura_Selic(di,df,v1)
print("---") 
Captura_IGPDI(di,df,v1) 

