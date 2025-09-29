import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore

# 1. Authenticate with Firebase
cred = credentials.Certificate("service-account-key.json")  # Path to your Firebase service account JSON
firebase_admin.initialize_app(cred)

# 2. Firestore client
db = firestore.client()

# 3. Load your CSV file
df = pd.read_csv("migrants-dets.csv")  # Make sure this file is in the same folder as the script

# 4. Upload each row as a document
for i, row in df.iterrows():
    doc_ref = db.collection("patients").document()  # auto-generate doc ID
    doc_ref.set(row.to_dict())  # Upload all columns as-is

print("✅ All CSV records uploaded successfully to Firestore!")
