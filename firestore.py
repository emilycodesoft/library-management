import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

# Application Default credentials are automatically created.
cred = credentials.Certificate("./service-account.json")

app = firebase_admin.initialize_app(cred)
db = firestore.client()
