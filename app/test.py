import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase app
cred = credentials.Certificate('path/to/your/serviceAccountKey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

class Repository:
    def __init__(self, collection_name):
        self.collection = db.collection(collection_name)

    def document_exists(self, document_id):
        doc_ref = self.collection.document(document_id)
        doc = doc_ref.get()
        return doc.exists

# Example usage
if __name__ == "__main__":
    repo = Repository('your_collection_name')
    document_id = 'your_document_id'
    if repo.document_exists(document_id):
        print(f"Document {document_id} exists in the collection.")
    else:
        print(f"Document {document_id} does not exist in the collection.")