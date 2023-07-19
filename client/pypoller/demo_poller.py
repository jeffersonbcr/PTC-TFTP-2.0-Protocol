#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 10:24:35 2018

@author: msobral
"""

import poller
import sys,time

class CallbackStdin(poller.Callback):
    
    def __init__(self, cb):
      poller.Callback.__init__(self, sys.stdin, 0)
      self.disable_timeout()
      self.cb = cb

    def handle(self):
        l = sys.stdin.readline()
        self.cb.envia(l)
        
        

class CallbackCoisa(poller.Callback):
    
    def __init__(self, tout):
        poller.Callback.__init__(self, None, tout)
        self.disable_timeout()
  
    def envia(self, dado):
      print('Dado:', dado)
      self.enable_timeout()
      self.reload_timeout()

    def handle_timeout(self):
        print('Timeout !')
        self.disable_timeout()
   
        
obj = CallbackCoisa(3)
cb = CallbackStdin(obj)

sched = poller.Poller()
sched.adiciona(cb)
sched.adiciona(obj)


sched.despache()
