import yaml
import subprocess 
from tkinter import filedialog
from tkinter import *
# import argparse
# document = """
#     dns: [10.241.80.49]
#     environment: ['VLAB_URL=https://vlab.emc.com', PRODUCTION=beta, AUTH_TOKEN_ALGORITHM=RS256]
#     image: willnx/vlab-gateway-api:2019.03.29
#     restart: unless-stopped
#     sysctls:
#     volumes
#     )

# parser = argparse.ArgumentParser(description='Process some integers.')

#Variables

# global inputchoice

#Function

#Questions:
#How do we want to handle empties? 

#Functions
def funcname(parameter_list):
    inputchoice = input("Press C to create a Config File, U to update a Config File, and A to add a new deployment service:")
    while inputchoice not in ('C','U','A'):
        inputchoice = input("Please enter C or U or A: ")


def create_object (input1,input2,input3,input4,input5,input6):
     x = yaml.safe_load("""
     dnsstring: 
     environmentstring: 
     imagestring: 
     restartstring:
     sysctls: 
     volumes: 
     """)
     #Change this to a list or a dictionary of some sort
    
     x['dnsstring'] = input1
     x['environmentstring'] = input2
     x['imagestring'] = input3
     x['restartstring'] = input4
     x['sysctls'] = input5
     x['volumes'] = input6
    
     for key, value in x.items():
        if value == '':
            x[key] = None
     
     return x
     

#note to self see if there's a way to make this function better because i know there is

    
def update(self):
    return

def add(self):
    return

#Program
inputchoice = input("Press C to create a Config File, U to update a Config File, and A to add a new deployment service:")
while inputchoice not in ('C','U','A'):
    inputchoice = input("Please enter C or U or A: ")

#Creating a file 
if inputchoice == 'C':
    print("Okay. So let's get started on creating a config file.\nBy the way if you don't have a value don't enter it.")
    
    #Input
    dsstring = input("What's the DNS string for your profile? ")
    evstring = input("What about the environment string? ")
    imgstring = input("The image string? ")
    rstrtstring = input("The restart string? ")
    scstring = input("Any sysctls? ")
    vstring = input("Volumes? ")

    print("Okay, please hold while we create your profile:")
    
    #newcode
    print("Okay input your config")
    print("okay enter the value ")
    

    # Saving File
    with open(input("What name would you like for this config?") + ".yaml","w") as f:
        newobject = create_object(dsstring,evstring,imgstring, rstrtstring, scstring,vstring)
        (yaml.dump(newobject, stream =f))
    
    print(f.name)
    print("Created!")
    

elif inputchoice == 'U':
    print("I see you want to update your config file!")
    print("")
    root = Tk()
    # root.withdraw()
    root.filename =  filedialog.askopenfilename(initialdir = "",title = "Choose Your Config File",filetypes = (("YAML files","*.yaml"),("all files","*.*")))
    filed = root.filename
    f = open(filed, "r")
    currentyamldocument = yaml.load(f) 
    f.close()
    print(filed)

    # print(yaml.load(f))
    print("Okay, here are the things you can edit:")
    print(currentyamldocument.keys())
    for key in currentyamldocument:
        print(key)
    ip = input("Which would you like to edit?")
    currentyamldocument[ip] = input("Got it. What would you like to change it to?")
    print(currentyamldocument[ip]) 
    print(currentyamldocument)
    answer = input("Got it, would you like to edit more? [Y/N]")

    while answer not in ('y','n'):
        print("trip")
        answer = input("please enter y or n")
    
    while answer is not 'n':
        print("Understood")
        ip = input("Which would you like to edit?")
        currentyamldocument[ip] = input("Got it. What would you like to change it to?")
        print(currentyamldocument[ip]) 
        print(currentyamldocument)
        answer = input("please enter y or n")

    #Saving
    with open(filed,"w") as f:
        (yaml.dump(currentyamldocument, stream =f))

    pass

elif inputchoice == 'A':
    pass
    print("Got it, so you want to add to your config file then.")
    
    #Loading 
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "",title = "Choose Your Config File",filetypes = (("YAML files","*.yaml"),("all files","*.*")))
    filed = root.filename
    f = open(filed, "r")
    currentyamldocument = yaml.load(f) 
    f.close()
    
    print("Here's what it currently looks like.")
    print(currentyamldocument.keys())
    for key in currentyamldocument:
        print(key)
    newentryname = input("What is the name of what you want to add?")
    newentryvalues = input("Got it, what about its values? ")
    x = {newentryname : newentryvalues}
    x.update(currentyamldocument)
    print(currentyamldocument)
    print(x[newentryname])

    

    f=open("test.yaml","w+")
    yaml.dump(currentyamldocument, stream=f)
    f.close()


else: 
    print("Test")



# X = yaml.safe_load("""
#     dnsstring: [test]
#     environmentstring: [test2]
#     imagestring: [test3]
#     restartstring: [test4]
#     sysctls: [test5]
#     volumes: [test6]
#     """)  
# print(X)


#Classes