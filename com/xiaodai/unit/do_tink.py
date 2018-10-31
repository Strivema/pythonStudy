# -*- coding:utf-8 -*- 
# @Author: Marie
# @Time:  2018/10/17 下午3:25
# @Software: PyCharm
from tkinter import *
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()
app = Application()
app.master.title('hello')
app.mainloop()