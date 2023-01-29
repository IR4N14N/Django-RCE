# Django-RCE
Simple django rce exploitation with leaked SECRET_KEY variable. <br />
# Installation and Usage (python 3)
```bash
git clone https://github.com/IR4N14N/Django-RCE.git
cd Django-RCE
pip install -r requirements.txt
cd exploit
```
now you need to set an environment variable : <br />
```bash
export DJANGO_SETTINGS_MODULE=exploit.settings
```
now just put SECRET_KEY , Sites_COOKIE , Your_Command on Django_RCE.py file and run the code
```bash
python3 Django_RCE.py
```
