import requests
from lxml import etree
from io import StringIO

resp = requests.get('https://www.google.com/').text
# xml = etree.fromstring(resp)
# f = open('lxml_pretty.xml', 'w')
# f.write(etree.tostring(xml, pretty_print=True))
parser = etree.XMLParser(remove_blank_text=True)
file_obj = StringIO(resp)
tree = etree.parse(file_obj, parser)
print(etree.tostring(tree, pretty_print=True))
# soup = BeautifulSoup(resp, features="lxml")
# pretty = soup.prettify().encode('utf-8').strip()
# with open('pretty.xml', 'wb+') as fp:
#    fp.write(pretty)
print("ping")
