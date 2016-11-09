import requests
from bs4 import BeautifulSoup as bs

for line in open("ELECTION_ID"):
    ids = line.split()[-1]
    addr = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/".format(ids)
    resp = requests.get(addr)
    soup = bs(resp.text, "html.parser")
    year = line.split()[0]
    file_name = year+".csv"
    with open(file_name,"w") as out:
        out.write(resp.text)
