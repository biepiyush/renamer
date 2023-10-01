import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "27640355")

API_HASH = os.environ.get("API_HASH", "a44bd8cf56719db4d32011594ad15d50")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6608783674:AAHwHiRABegPuX0ocdDRLJtCUrz7l074CFs") 

FORCE_SUB = os.environ.get("FORCE_SUB", "") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://panda:<x4IE6ybee8WhIcZI>@cluster0.kueaumu.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get("PORT", "8080")
