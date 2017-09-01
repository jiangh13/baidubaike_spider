#-*- coding: UTF-8 -*-
#将爬取之后的网页保存到本地文件中，保存为网页格式

class HtmlOutputer(object):
    
    def __init__(self):
        self.datas=[]
        
    
    def collectData(self,data):
        if data is None:
            return
        self.datas.append(data)

    def outputHtml_csv(self):
        fout = open('output.csv','w')
        fout.write("\"url\",\"title\",\"summary\"\n") 
        for data in self.datas:
            fout.write(data['url'] + "\n")
            fout.write(data['title'].encode('utf-8') + "\n")
            fout.write(data['summary'].encode('utf-8') + "\n")

    def outputHtml(self):
        fout = open('output.html','w')
        
        fout.write("<html>")
        fout.write("<body>")
        fout.write('<head><meta charset="utf-8"></head>')   #告诉浏览器使用何种编码
        fout.write("<table>")
        
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data['url'])
            fout.write("<td>%s</td>"%data['title'].encode('utf-8'))
            fout.write("<td>%s</td>"%data['summary'].encode('utf-8'))
            fout.write("</tr>")
            
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
