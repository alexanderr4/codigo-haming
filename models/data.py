class Data:
    def __init__(self, text) :
        self.text=text

    def covertTextDecimal(self):
        listText = []
        for i in range(0,len(self.text)):
            listText.insert(i,ord(self.text[i]))
        return listText
    
    def convertTextBynary(self):
        strm=''
        listText = self.covertTextDecimal()
        for i in range(len(listText)):
            listText[i]=bin(listText[i])[2:]
        return listText
"""m= Data('h')
m.convertTextBynary()"""