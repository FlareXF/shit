

from main.models import Sites
from django.contrib.auth.models import User
from django.core.files import File
import json 
import io


with open('stass.json', encoding='utf-8') as f:
    vuzs_json = json.load(f)

#mifi = {}
#for vuz in vuzs_json:
#    if vuz.count('МИФИ') != 0:
#        mifi[vuz] = vuzs_json[vuz]
# site logo_file
num = len(vuzs_json)
for vuz in vuzs_json:
    num -= 1
    print(vuz)
    if vuz.count('МИФИ') > 0:
        site = Sites(name=vuz, url=vuzs_json[vuz]['site'])
        site.save()
        site.siteprofile.image.save(f'{vuz}.png', File(open(vuzs_json[vuz]['logo_file'], 'rb')))
        print(vuz, vuzs_json[vuz])


# import re
# url = "https://www.synergy.ru/lp/dpvuz/"

# print(re.search(r'https?://(www.)?([A-Za-z_0-9.-]+).*', url).group(2))