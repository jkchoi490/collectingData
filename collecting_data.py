import os
import sys
from urllib.request import urlopen
import json
import pandas as pd
import requests
import time

url = 'http://openapi.foodsafetykorea.go.kr/api/3495f5476f4e4e24bdfc/I2790/json/53001/53314'

data = urlopen(url).read()
output = json.loads(data)

ingredientDDF = pd.DataFrame()
ingredientDF = ingredientDDF.append(
    {"NUM":"","GROUP_NAME":"",
    "DESC_KOR":"","SERVING_SIZE":"","NUTR_CONT1":"",
    "NUTR_CONT2":"","NUTR_CONT3":"","NUTR_CONT4":"",
    "NUTR_CONT5":"","NUTR_CONT6":"","NUTR_CONT7":"",
    "NUTR_CONT8":"","NUTR_CONT9":""}, 
    ignore_index=True)

total = output["I2790"]["total_count"]
num = len(output["I2790"]["row"])

for i in range(0,num):
    ingredientDDF.loc[i,"NUM"] = output["I2790"]["row"][i]["NUM"]
    ingredientDDF.loc[i,"GROUP_NAME"] = output["I2790"]["row"][i]["GROUP_NAME"]
    ingredientDDF.loc[i,"DESC_KOR"] = output["I2790"]["row"][i]["DESC_KOR"]
    ingredientDDF.loc[i,"SERVING_SIZE"] = output["I2790"]["row"][i]["SERVING_SIZE"]
    ingredientDDF.loc[i,"NUTR_CONT1"] = output["I2790"]["row"][i]["NUTR_CONT1"]
    ingredientDDF.loc[i,"NUTR_CONT2"] = output["I2790"]["row"][i]["NUTR_CONT2"]
    ingredientDDF.loc[i,"NUTR_CONT3"] = output["I2790"]["row"][i]["NUTR_CONT3"]
    ingredientDDF.loc[i,"NUTR_CONT4"] = output["I2790"]["row"][i]["NUTR_CONT4"]
    ingredientDDF.loc[i,"NUTR_CONT5"] = output["I2790"]["row"][i]["NUTR_CONT5"]
    ingredientDDF.loc[i,"NUTR_CONT6"] = output["I2790"]["row"][i]["NUTR_CONT6"]
    ingredientDDF.loc[i,"NUTR_CONT7"] = output["I2790"]["row"][i]["NUTR_CONT7"]
    ingredientDDF.loc[i,"NUTR_CONT8"] = output["I2790"]["row"][i]["NUTR_CONT8"]
    ingredientDDF.loc[i,"NUTR_CONT9"] = output["I2790"]["row"][i]["NUTR_CONT9"]
ingredientDDF.to_csv('FoodData.csv', mode='a', header=False, index=False, encoding='UTF-8')
time.sleep(60)