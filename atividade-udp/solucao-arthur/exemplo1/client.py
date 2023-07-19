from pypoller import poller
import sys,time
import os
 
class CallbackStdin(poller.Callback):
  
   def __init__(self, tout:float):
       poller.Callback.__init__(self, sys.stdin, tout)
       self._cnt = 0
 
   def handle(self):
       l = sys.stdin.readline()
       self._cnt = 0
       if l == "S\n" or l == "s\n":
           #os.remove(fname)
           self.disable_timeout()        
           self.disable()
       if l == "N\n" or l == "n\n":
           self.disable_timeout()        
           self.disable()
           sys.exit()
 
   def handle_timeout(self):
         # desativa o timeout deste callback, e também o evento leitura !
         print("timeout")
         self.disable_timeout()        
         self.disable()
         sys.exit()
 
####################################  
 
try:
   fname = sys.argv[1]
   print('filename obtained by argument successfully')
except Exception as Argument:
   print('Error. There is no Filename passed by argument: \n', Argument)
   sys.exit()
 
# instancia um callback
cb = CallbackStdin(10)
 
# cria o poller (event loop)
sched = poller.Poller()
 
# registra o callback no poller
sched.adiciona(cb)
print('Quer mesmo apagar esses arquivos (S/N) ?:')
# entrega o controle pro loop de eventos
sched.despache()
