import os
from google.cloud import firestore

async def store_memory(case):
    db = firestore.Client()
    col = os.getenv('FIRESTORE_COLLECTION', 'agent_memory')
    doc_ref = db.collection(col).document()
    doc_ref.set({"case": case})
    return {"id": doc_ref.id, "case": case}
