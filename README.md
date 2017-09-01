# baidubaike_spider
the baidubaike maybe change the web item
change the "heml_parser.py" getNewUrls method

for example, older usage is:

links = soup.find_all('a',href = re.compile(r"/view/\d+\.htm"))

this doesn't work for baidubaike now

newer usage is like this:

links = soup.find_all('a',href = re.compile(r"/item/\w*"))
