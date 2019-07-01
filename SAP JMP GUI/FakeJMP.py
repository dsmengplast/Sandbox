#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 22:31:37 2019

@author: XiaoshiZhang
"""
import tkinter as tk
import pygubu

class Application:
    def __init__(self,master):
        self.master = master
        
        self.builder = builder = pygubu.Builder()
        
        builder.add_from_file('FakeJMP.ui')
        
        self.Frame_1 = builder.get_object('Frame_1',master)
        
#        builder.Select_SAP_File_Botton(self)
        
if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    
    root.mainloop()
