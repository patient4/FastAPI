
import firebase_admin
from firebase_admin import firestore, credentials

from modal.todo import Todo

# Application Default credentials are automatically created.

class Firebase():
    def __init__(self) -> None:    
        self.cred = credentials.Certificate('/usr/local/google/home/rachitmohan/Downloads/FastAPI/auth/fastapi.json')
        self._app = firebase_admin.initialize_app(self.cred)
        self._db = firestore.client()
    
    def read_docs(self, collection_name) -> list[Todo]:
        docs = []
        docs_ref = self._db.collection(collection_name).stream()
        for doc in docs_ref:
            docs.append(doc.to_dict())  
        return docs
    
    def create_doc(self, collection_name, payload: Todo):
        doc_ref = self._db.collection(collection_name).document(payload["subject"]).set(payload)
        return doc_ref
    
    def update_doc(self, payload: Todo, id: str):
        pass
    
    def delete_doc(self, id: str):
        pass
    
        
        
        