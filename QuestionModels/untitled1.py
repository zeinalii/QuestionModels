# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:25:26 2020

@author: Amir Zeinali
@email: ah.zeinali94@gmail.com

"""
import json
import importlib


for i in range(1,34):
    name = "model_" + str(i)
    module = "QuestionModels." + name
    module = importlib.import_module(module)
    model = eval("module.%s()"%name)    
    s = ""
    for i in range(N):
        d= model.generate(Print=False)
        app_json = json.dumps(d)
        s += str(app_json) + "\n"
    with open(name+ ".json","w") as fh:
        fh.write(s)
        
