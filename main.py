import imp
import module
tag=""
listMember=[]
tag= module.menu()
while tag!="Q":
    if(tag=="A"):
        module.addMember(listMember)
        tag= module.menu()
    if(tag=="D"):
        module.removeMember(listMember)
        tag= module.menu()
    if(tag=="N"):
        module.startGame(listMember)
        tag= module.menu()