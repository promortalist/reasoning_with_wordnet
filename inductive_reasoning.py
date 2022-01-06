print  ("Please wait a while - WordNethack is uppered into memory.")
print ("Its RIP is the beginnning")
import dicthack
dish = raw_input("What do you eat? ")
answ1 = dicthack.hyperonym(dish)
dish2 = raw_input("What do you eat? ")
answ2 = dicthack.hyperonym(dish2)
setF = set(answ1)
print (setF)
setF2 = set(answ2)
print (setF2)
print ("zbior wspolny to: ")
print (setF.intersection(setF2))
#reasoning = setF.intersection(setF2)
#reason = list(reasoning)
#print ("I see that you like ",reason[0], " and ", reason[1])
print ("Nice RIPe food!")
wspolnota = setF.intersection(setF2)
wspolnota2 = list(wspolnota)
print ("You like: ")
print (wspolnota2[1])



