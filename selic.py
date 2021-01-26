#import urllib.request
from urllib.request import urlopen
import requests
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
    TI= (sum(lista))
    I=(TI/100+1)
    F =(I*VC)
    VF =(round(F,2))
    return VF
    
    
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
    response = urlopen(url).read()
   
    print(url)
    data = (json.loads(response))
    #print(data)    
    
    for dados in data:
        dt = (dados['data'])
        vlr = str(dados['valor'])
        

        if ConvertStringToDate(dt) <= ConvertStringToDate(di)  :
            pass
             
        else:  
            
           # print(dados)
                    
            vl.append(vlr)
            dvl.append(dt) 
    
    VP =TotalIndice_Selic(vl,v)
    
    print("Valor Inicial: R$ "+ str(v),"Data Inicio:"+ str(di), "Data Final:"+str(df), "Valor Corrigido: R$" + str(VP)  )


 

def Captura_IGPDI(di,df,v):
    
    url='https://api.bcb.gov.br/dados/serie/bcdata.sgs.190/dados?formato=json&dataInicial='+di+'&dataFinal='+df
    print(url)
    response = urlopen(url).read()
    print("Resultado da Correção pelo IGP-DI (FGV)")
    data = (json.loads(response))
    pprint.pprint(data)
  
    
    for dados in data:
        dt = (dados['data'])
        vlr = str(dados['valor'])
                    
        vl.append(vlr)
        dvl.append(dt) 
    
    VP =TotalIndice_IGPDI(vl,v)
 
    print("Valor Inicial: R$ "+ str(v),"Data Inicio:"+ str(di), "Data Final:"+str(df), "Valor Corrigido: R$" + str(VP)  )


  
  
  
di="01/01/2020"
df="31/12/2020"
v1 = 200
#Captura_Selic(di,df,v1) 
Captura_IGPDI(di,df,v1) 

