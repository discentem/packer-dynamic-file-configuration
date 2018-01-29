import json
import xmltodict

with open("Autounattend.xml") as autounattend:
    autounattendDict = xmltodict.parse(autounattend.read())

print(autounattendDict)
