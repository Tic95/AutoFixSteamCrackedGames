import shutil
import os
import patoolib

listobj = os.listdir()
numb_file = len(listobj)
import os
absolute_path = os.path.abspath(__file__)
print("Full path: " + absolute_path)
print("Directory Path: " + os.path.dirname(absolute_path))


for x in range(numb_file):
    testif = (".rar" in listobj[x])
    
    if testif == True:
        
        
        
        newlistobj = listobj[x].replace(".rar","")
        

        newlistobj = newlistobj.replace(" ","")
        newlistobj = newlistobj.replace(".","")
        os.mkdir(newlistobj)
        patoolib.extract_archive(str(listobj[x]), outdir=os.path.dirname(absolute_path)+"/"+newlistobj) #extract the rar file
        os.remove(listobj[x])     #remove the rar file after extraction 


listobjafter = os.listdir()

newnumbfile = len(listobjafter)
Folderlist = []

for y in range(newnumbfile):
    testrar = (".rar" in listobjafter[y])
    testbat = (".bat" in listobjafter[y])
    testpy = (".py" in listobjafter[y])
    
    
    if testbat or testpy or testrar == True:
        continue
    else:
        Folderlist.append(listobjafter[y])
        print(Folderlist)


def foldercheck(x):
    global path1
    global z
    if  os.path.isdir(x):
        print("folder",listofpath[z],x)
        
        path1 = (path1 + "/" + listofpath[z])
    else:
        print("files", listofpath[z],path1)
    

path1 = Folderlist[0]




def toutcheck():
    global z
    global listofpath
    global nombrefiles
    listofpath = os.listdir(path1)
    nombrefiles = len(os.listdir(path1))
    
    
    for z in range(nombrefiles):
    
    
        foldercheck(path1+"/" + listofpath[z])

for r in range(5):
    toutcheck()
    if len(os.listdir(path1)) > 4:
        
        DestinationPath = path1
        break

    else:
        continue


print(DestinationPath)

path1 = Folderlist[1]

for r in range(5):
    toutcheck()
    if len(os.listdir(path1)) > 4:
        
        DestinationPath2 = path1
        break

    else:
        continue

print(DestinationPath2,DestinationPath)



shutil.copytree(DestinationPath2, DestinationPath, dirs_exist_ok=True)
shutil.rmtree(Folderlist[1])