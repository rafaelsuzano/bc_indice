#import urllib.request
from urllib.request import urlopen
import requests
import datetime
import json 

#Listas
vl =[]
dvl =[]

#Calculo      
def TotalIndice(V,VC):
    del V[0]
  
    lista = [float(i) for i in V]
    TI= (sum(lista))
    I=((TI/100)+1)
    F =(I*VC)
    VF =(round(F,2))
    
    #for i, j in zip((dvl), (vl)):
        
     #   print("Data:"+str(i),"Valor:"+(j))
      


    
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
        
    
    for dados in data:
        dt = (dados['data'])
        vlr = str(dados['valor'])
        

        if ConvertStringToDate(dt) <= ConvertStringToDate(di)  :
            pass
             
        else:  
            print (dados)    
            vl.append(vlr)
            dvl.append(dt) 
    
    VP =TotalIndice(vl,v)
    
    

    
    print("Valor Inicial: R$ "+ str(v),"Data Inicio:"+ str(di), "Data Final:"+str(df), "Valor Corrigido: R$" + str(VP)  )

di="01/01/2020"
df="31/01/2020"
v1 = 200
Captura_Selic(di,df,v1) 
  
