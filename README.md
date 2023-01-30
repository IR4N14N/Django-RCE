# Django-RCE
Simple django rce exploitation with leaked SECRET_KEY variable. <br />
# Installation and Usage (python 3)
```bash
git clone https://github.com/IR4N14N/Django-RCE.git
cd Django-RCE
pip install -r requirements.txt
django-admin startproject exploit
mv exploit/exploit/settings.py .
```
now put SECRET_KEY , Sites_COOKIE , setting path on settings.json file <br />
then you just need to Enter your OS command on Django_RCE.py and run the code
```bash
python3 Django_RCE.py
```
