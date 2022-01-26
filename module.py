from hashlib import new
import re
from card import Deck, Suit,Rank,Card,Set3Card,Member
import random

def menu():
    """Menu game"""
    print("=========================")
    print("Thêm người chơi mới [A]")
    print("Xóa người chơi [D]")
    print("Bắt đầu ván mới [N]")
    print("Thoát [Q]")
    print("=========================")
    return (input (">>")).upper()
def menu_in_game(step:int):
    if step==0:
        print("Chia bài [C]")
    if step==1:
        print("Lật bài [L]")
   
    return (input (">>")).upper()

def startGame(listMember:list[Member])->list[Member]:
    if len(listMember)<2 or len(listMember)>12:
        print("Số người chơi k hợp lệ") 
        return
    else:
        step=0
        flag = menu_in_game(step)
        while flag !="C" and flag !="B":
            flag = menu_in_game(step)
        
        if flag == "C":
            listMember = chia_bai(listMember)
            step=1
            print("Đã chia bài xong")
            flag= menu_in_game(step)
            if flag =="L":
                lat_bai(listMember)

def addMember(listMember:list[Member])->list[Member]:
    """Thêm người chơi"""
    if len(listMember)==0:
        print("Nhập số người muốn chơi")
        count = int(input(">>"))
        while count<2 or count>12:
            print("Số lượng người chơi k hợp lệ, vui lòng nhập lại")
            count = int(input(">>"))
        for x in range(count):
            print("Người chơi số ",x+1)
            name = input(">>")
            id=x+1
            listMember.append(Member(id,name,[]))
    else:
        if len(listMember)<12:
            print("Nhập tên người chơi mới")
            name = input(">>")
            id=0
            listMember.append(Member(listMember[-1].id+1, name,[]))
        else:
            print("Hết slot")
def removeMember(listMember:list[Member])->list[Member]:
    print("Xóa người chơi số:")
    index = int(input(">>"))
    while index<1 or index> (len(listMember)+1):
        print("Chọn lại")
        index = int(input(">>"))
    return listMember.remove(listMember[index-1])
def chia_bai(listMember:list[Member])->list[Member]:
    newDeck = Deck()
    newDeck.shuffle()
    for x in listMember:
        x.set_card = Set3Card(newDeck.pop())
    return listMember

def lat_bai(listMember:list[Member]):
    for x in listMember:
        x.show_card()
    winer = listMember[0]
    for x in listMember:
        if x.set_card>winer.set_card:
            winer=x
    print("==> Người chiến thắng là:", winer.name,"  ",winer.set_card.get_scrore(), " điểm, với quân bài lớn nhất ",winer.set_card.get_max_card().show_card())
    