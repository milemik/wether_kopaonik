from bs4 import BeautifulSoup as bs
import requests


class Kop_vreme():

    def __init__(self):
        r = requests.get("https://www.infokop.net/ski-prognoza/19.html")
        status_ = r.status_code
        if status_ == 200:
            print("Status ok")
        self.soup = bs(r.text, "html.parser")
        

    def get_info(self):
        info = []
        td = self.soup.select("td")
        for t in range(len(td)):
            if "Temperatura" in td[t].text:
                try:
                    info.append(td[t+1].text.replace("\n","").replace("\t",""))
                except IndexError:
                    pass
        return info

    def nice_info(self, inf):
        inf0 = inf[1:-1]
        data = dict()
        for i in range(0, len(inf0), 2):
            try:
                #print("{}: {}".format(inf0[i].strip(), inf0[i+1]))
                datum = inf0[i].strip()
                temp = inf0[i+1]
                data[datum]=temp
            except IndexError:
                pass
        print(data)

if __name__=="__main__":
    c = Kop_vreme()
    text = c.get_info()
    c.nice_info(text)

