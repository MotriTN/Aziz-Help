from math import*
dc= int (input ("donner la note de controle:"))
ds= int (input ("donner la note de synthese:"))
M= int (dc+(ds*2))/3
print ("note devoir de controle:",dc)
print ("note devoir de synthese:",ds)
if M<8:
    print (M,"moyenne tres faible")
elif 8<=M>10:
    print(M,"moyenne faible")
elif 10<=M>12:
    print (M,"passable")
elif 12<=M>14:
    print (M,"assez bien")
elif 14<=M>16:
    print (M,"bien")
else:
    print (m,"tres bien")