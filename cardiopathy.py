# -*- coding: utf-8 -*-
#TODO
# 0.LEDINIT
# 1.UI
# 2.Packing

import sys,time,random,os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFrame, QApplication
from PyQt5.QtCore import *
from halli import Ui_MainWindow
from galli import Ui_Frame
from PyQt5.QtGui import QPixmap

#tuple

Redpt =    (1,1,1,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,3,3,3,0,0,0,0,0,0,0,0,0,4,4,4,0,0,0,0,0,0,0,0,0,5,5,0,0,0,0,0,0,1,1,1,0,0,0,3,3,3,1,0,0,1,0,0,1,0,0,1,1,1,1,1,1,2,2,2,1,0,0,1,0,0,1,0,0,2,2,2,1,1,0,1,1,0,1,1,0,1,1,1,0,1,1,4,0,0,0,0,0,0,0,0,0,0)
Greenpt =  (0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,3,3,3,0,0,0,0,0,0,0,0,0,4,4,4,0,0,0,0,0,0,0,0,5,5,0,0,0,0,1,0,0,1,1,0,1,0,0,3,3,3,0,1,0,0,1,0,1,1,1,0,1,1,1,0,0,2,2,2,0,1,0,0,1,0,1,1,0,2,2,2,1,0,1,1,0,1,1,1,0,1,1,0,1,4,0,0,0,0,0,0,0,0,0)
Bluept =   (0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,3,3,3,0,0,0,0,0,0,0,0,0,4,4,4,0,0,0,0,0,0,0,5,5,0,0,0,1,0,1,0,1,0,1,0,0,1,0,3,3,3,0,0,1,1,1,1,1,0,1,0,1,0,0,1,0,2,2,2,0,0,1,1,0,1,1,0,1,2,2,2,0,1,1,1,0,1,1,1,0,0,1,4,0,0,0,0,0,0,0,0)
Yellowpt = (0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,3,3,3,0,0,0,0,0,0,0,0,0,4,4,4,0,0,0,0,0,0,5,5,0,0,1,0,1,1,0,0,1,0,0,1,0,0,1,3,3,3,1,1,0,1,1,0,0,0,1,0,0,1,0,0,1,2,2,2,0,1,1,0,1,1,0,1,1,2,2,2,0,1,1,1,1,4,0,0,1,0,0,0,0,0,0,0,0)
SPpt =     (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,2,2,3,3,4,0)
A    =     (0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0)
ArrowXPos=(113,266,419,572,725,878)
class Main(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)

class Child(QFrame,Ui_Frame):
    def __init__(self):
        super(Child, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)
        self.onseat=[]
        self.arrNo=7
        self.Aka = 0
        self.Mid = 0
        self.Aoi = 0
        self.Kii = 0
        self.Spon = 0 
        self.Fin = 0
        self.OnDesk=[]
        self.OnVoid=[]
        self.onTop=[120,120,120,120,120,120]  

    def Judge(self,numm):
        self.label_phase.setText("判定阶段")
        jug = 0 
        for i in range(len(self.onseat)):
                if numm ==self.onseat[i].number:
                    break
        for j in self.onTop:
            if j == 119:
                jug = 1
                break
            elif j == 118 or j == 117:
                if int(self.Mid):
                    jug = 1
                    break
            elif j == 116 or j == 115:
                if int(self.Aoi):
                    jug = 1
                    break
            elif j == 114 or j == 113:
                if int(self.Kii):
                    jug = 1
                    break
            else:
                pass
        # jug = int(self.Spon == 4)
        # if self.Spon == 3:
        #     jug += int((self.Mid))
        # if self.Spon == 2:
        #     jug += int((self.Aoi))
        # if self.Spon == 1:
        #     jug += int((self.Kii))
        if self.Spon == 0:
            temp = not(self.Aka % 5) and (self.Aka)
            temp = temp or (not(self.Mid % 5) and (self.Mid))
            temp = temp or (not(self.Aoi % 5) and (self.Aoi))
            temp = temp or (not(self.Kii % 5) and (self.Kii))
            jug += int(temp)
        print(jug)
        if jug:
            self.label.setText("Success！")
            self.onseat[i].getCard(self)
        else:
            self.label.setText("Foul！")
            self.onseat[i].lostCard(self)

    def OPEN(self,maid):
        for m in range(0,6):
            if main.isckd[m]:
                a=Player(m)
                self.onseat.append(a)
        self.TimerLabel.setText("3")
        self.GamePrep()
       
        self.LogoIndex = 0
        self.label.setText(str(main.ind))
        self.Gamestart()
    def Gamestart(self):
        # self.s=1             
          #TODO
          self.dictdesk={0:self.label_5,1:self.label_6,2:self.label_7,3:self.label_8,4:self.label_9,5:self.label_10}
          self.dictnum={0:self.P1_2,1:self.P2_2,2:self.P3_2,3:self.P4_2,4:self.P5_2,5:self.P6_2}
          self.timer0=QTimer()
          self.timer0.timeout.connect(self.refreshLogo)
          self.timer1=QTimer()
          self.timer1.timeout.connect(self.pause2)
          self.show()
          self.timer0.start(1000)
         # self.label.setText("玩家人数")
          self.label_phase.setText("玩家人数")
         # self.Gameroll()

    def GamePrep(self):
        limit=120/len(self.onseat)
        for j in range(120):
            k=random.randint(0,len(self.onseat)-1)
            while len(self.onseat[k].motsu)>=limit:
                k=random.randint(0,len(self.onseat)-1)
            self.onseat[k].motsu.append(cardset[j])
        if main.isckd[0]:
            self.P1_2.setText(str(int(limit)))
        if main.isckd[1]:    
            self.P2_2.setText(str(int(limit)))
        if main.isckd[2]:
            self.P3_2.setText(str(int(limit)))
        if main.isckd[3]:
            self.P4_2.setText(str(int(limit)))
        if main.isckd[4]:
            self.P5_2.setText(str(int(limit)))
        if main.isckd[5]:
            self.P6_2.setText(str(int(limit)))    
        self.label_arr.move(153*(self.onseat[0].number)+113,140)
        self.arrNo=self.onseat[0].number


   # def Gameroll(self):
      #  rolln=len(self.onseat)
    def moveArr(self,ing):
        if self.arrNo == self.onseat[-1].number:
            self.arrNo = self.onseat[0].number
            self.label_arr.move(153*(self.onseat[0].number)+113,140)
            if ing:
                self.onseat[-1].CastCard(self)
        else:
            for i in range(len(self.onseat)):
                if self.arrNo == self.onseat[i].number:
                    self.arrNo = self.onseat[i+1].number
                    self.label_arr.move(153*(self.onseat[i+1].number)+113,140)
                    if ing:
                        self.onseat[i].CastCard(self)
                    break

    def Calc(self,car):
        self.Aka = 0
        self.Aoi = 0
        self.Mid = 0
        self.Kii = 0
        self.Spon = 0
        for cal in self.onTop:
            if cal != 120: 
                self.Aka += car[cal].r
                self.Aoi += car[cal].b
                self.Mid += car[cal].g
                self.Kii += car[cal].y
                self.Spon = self.Spon or car[cal].sp
        print(self.onTop)
        print(self.Aka)
        print(self.Aoi)
        print(self.Mid)
        print(self.Kii)
        print(self.Spon)




    def refreshLogo(self):
        if self.LogoIndex == 0:
            self.TimerLabel.setText("3")
        elif self.LogoIndex == 1:
            self.TimerLabel.setText("2")
        elif self.LogoIndex == 2:
            self.TimerLabel.setText("1")
        elif self.LogoIndex == 3:
            self.Fin=1
            self.TimerLabel.setText("Start!")
            self.label_4.setText("剩余时间")
        elif self.LogoIndex > 4 and self.LogoIndex < 305:
            self.TimerLabel.setText(str((305-self.LogoIndex)//60)+":"+str((305-self.LogoIndex)%60))
        elif self.LogoIndex == 305:
            self.TimerLabel.setText("00:00 Game Over")
            self.Fin = 0
        self.LogoIndex +=1

#2->5 5->3 3->2
    def keyPressEvent(self, event):
        if self.Fin:
            li=[]
            for i in self.onseat:
                li.append(i.number)
            if event.key() == Qt.Key_A:
                self.TimerLabel.setText(str(self.label_arr.geometry().x()))
            if event.key() == Qt.Key_C:
                self.label_5.setPixmap(QPixmap("C:/Users/ht864/Documents/贪玩蓝月/十周年/img/120.png"))
            if event.key() == Qt.Key_Q:
              #  if self.arrNo == 0:
                try:
                    li.index(0)
                except Exception as e:
                    pass
                else:
                    self.Judge(0)
            if event.key() == Qt.Key_E:
                try:
                    li.index(1)
                except Exception as e:
                    pass
                else:
              #  if self.arrNo == 1:
                    self.Judge(1)
            if event.key() == Qt.Key_T:
                try:
                    li.index(2)
                except Exception as e:
                    pass
                else:
             #   if self.arrNo == 2:
                    self.Judge(2)
            if event.key() == Qt.Key_R:
                try:
                    li.index(3)
                except Exception as e:
                    pass
                else:
            #    if self.arrNo == 3:
                    self.Judge(3)
            if event.key() == Qt.Key_W:
                try:
                    li.index(4)
                except Exception as e:
                    pass
                else:
             #   if self.arrNo == 4:
                    self.Judge(4)
            if event.key() == Qt.Key_Y:
                try:
                    li.index(5)
                except Exception as e:
                    pass
                else:
             #   if self.arrNo == 5:
                    self.Judge(5)
            if event.key() == Qt.Key_1:
                if self.arrNo == 0:
                    self.moveArr(1)
            if event.key() == Qt.Key_3:
                if self.arrNo == 1:
                    self.moveArr(1)
            if event.key() == Qt.Key_5:
                if self.arrNo == 2:
                    self.moveArr(1)
            if event.key() == Qt.Key_4:
                if self.arrNo == 3:
                    self.moveArr(1)
            if event.key() == Qt.Key_2:
                if self.arrNo == 4:
                    self.moveArr(1)
            if event.key() == Qt.Key_6:
                if self.arrNo == 5:
                    self.moveArr(1)

    def pause(self):
      #  self.timer0.stop()
        self.Fin=0
        self.timer1.start(2000)
        #TODO FAIL
    def pause2(self):
        self.label_phase.setText("出牌阶段")
        self.label.setText("")
        self.timer1.stop()
   #     self.timer0.start(1000)
        self.Fin=1
        #TODO FAIL FADE

      
class HGCard(object): 
    def __init__(self,id):
        self.cid=id
        self.r=Redpt[id]
        self.g=Greenpt[id]
        self.b=Bluept[id]
        self.y=Yellowpt[id]
        self.sp=SPpt[id]
    def __del__(self):
        pass
        #TODO


class Player(object):
    def __init__(self,nb):
        self.number=nb
        self.motsu=[]  
        #possession
    #def RollCard(self,n):
    #    len(Obj.motsu)
    #    self.motsu.append(n)

    def CastCard(self,chi):
        cache=int(len(self.motsu))
        if cache>0:
            cardid=self.motsu[random.randint(0,cache-1)].cid
            chi.onTop[self.number]=cardid  
            chi.dictdesk[self.number].setPixmap(QPixmap("./img/"+str(cardid)+".png"))
            chi.OnDesk.append(cardid)
            self.motsu.remove(cardset[cardid])
            chi.dictnum[self.number].setText(str(len(self.motsu)))
            chi.Calc(cardset)
            chi.label_deskn.setText(str(int(chi.label_deskn.text())+1))
        else:
            chi.dictnum[self.number].setText("GG")
            chi.onseat.remove(self)

    def getCard(self,chi):
        print("get!")
        for i in chi.OnDesk:
            self.motsu.append(cardset[i])
        for l in chi.OnVoid:
            self.motsu.append(cardset[l])
        chi.OnDesk = []
        chi.OnVoid = []
        chi.label_deskn.setText("0")
        chi.label_voidn.setText("0")
        chi.onTop = [120,120,120,120,120,120]
        for j in range(6):
            chi.dictdesk[j].setPixmap(QPixmap(""))
        chi.Aka = 0
        chi.Aoi = 0
        chi.Mid = 0
        chi.Kii = 0
        chi.Spon = 0
        for k in chi.onseat:
                chi.dictnum[k.number].setText(str(len(k.motsu)))
                print(len(k.motsu))
        print("A"+str(len(self.motsu)))
        print("B"+str(len(chi.OnVoid)))
        chi.pause()

    def lostCard(self,chi):
        if len(self.motsu) < len(chi.onseat):
            for i in self.motsu:
                chi.OnVoid.append(i.cid)
            chi.dictnum[self.number].setText("GG")
            chi.moveArr(0)
            chi.onseat.remove(self)
            chi.label_voidn.setText(str(len(chi.OnVoid)))


        else:
            for j in chi.onseat:
                j.motsu.append(self.motsu.pop())
            for k in chi.onseat:
                chi.dictnum[k.number].setText(str(len(k.motsu)))
            if chi.dictnum[self.number].text=="0":
                chi.dictnum[self.number].setText("GG")
        chi.pause()





def restart_program(inndex):
        if inndex == 0:
            print('ready to restart program......')
            python = sys.executable
            os.execl(python, python, *sys.argv)
        else:
            sys.exit(0)

if __name__ =="__main__":
    cardset=[]
    for i in range(120):
        cardset.append(HGCard(i))
    app = QApplication(sys.argv)
    main = Main()
    ch = Child()
    main.show()
    main.pushButton.clicked.connect(ch.OPEN)
    restart_program(app.exec_())

            
 #arrow 



 # #updateplayercount
 #    def updatelabel(self):
 #        self.isckd=[self.checkBox_1.isChecked(),self.checkBox_2.isChecked(),self.checkBox_3.isChecked(),self.checkBox_4.isChecked(),self.checkBox_5.isChecked(),self.checkBox_6.isChecked()]
 #        self.ind=0
 #        for i in range(0,6):
 #            self.ind+=self.isckd[i]
 #        self.label.setText(str(self.ind))
 #      