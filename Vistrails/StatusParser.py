'''
Created on Dec 2, 2012

@author: normanxin
'''
from sgmllib import SGMLParser
class StatusParser(SGMLParser):
    def reset(self):
        self.datas=[]
        SGMLParser.reset(self)
    def parse(self,data):
        self.feed(data)
        self.close()
    def handle_data(self,data):
        if not data.isspace(): 
            self.datas.append(data.strip())
