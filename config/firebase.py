import firebase_admin
from firebase_admin import firestore, credentials
from modal.todo import Todo

class Firebase:
    """
    A class to interact with Firebase Firestore for CRUD operations on Todo items.
    """

    def __init__(self) -> None:
        """
        Initializes the Firebase client with the provided credentials.

        This method sets up the Firebase application using a service account key
        and initializes the Firestore client. However feel free to add your service account.json
        """
        # Load credentials from a JSON file
        self.cred = credentials.Certificate('/usr/local/google/home/rachitmohan/Downloads/FastAPI/auth/fastapi.json')
        # Initialize the Firebase application with the provided credentials
        self._app = firebase_admin.initialize_app(self.cred)
        # Initialize Firestore client
        self._db = firestore.client()
    
    def read_docs(self, collection_name: str) -> list[dict]:
        """
        Reads documents from a specified Firestore collection.

        Args:
            collection_name (str): The name of the Firestore collection to read from.

        Returns:
            list[dict]: A list of dictionaries, each representing a document in the collection.
        """
        docs = []
        # Reference to the Firestore collection
        docs_ref = self._db.collection(collection_name).stream()
        # Iterate over the documents in the collection
        for doc in docs_ref:
            docs.append(doc.to_dict())
        return docs
    
    def create_doc(self, collection_name: str, payload: dict):
        """
        Creates a new document in a specified Firestore collection.

        Args:
            collection_name (str): The name of the Firestore collection to add the document to.
            payload (dict): The document data to be stored in Firestore.

        Returns:
            None: The Firestore `set` operation does not return a reference.
        """
        # Create a document with the specified data in the Firestore collection
        doc_ref = self._db.collection(collection_name).document(payload["subject"]).set(payload)
        return doc_ref
    
    def update_doc(self, collection_name: str, payload: dict, id: str):
        """
        Updates an existing document in a specified Firestore collection.

        Args:
            collection_name (str): The name of the Firestore collection containing the document.
            payload (dict): The updated document data.
            id (str): The identifier of the document to update.

        Returns:
            None: The Firestore `update` operation does not return a reference.
        """
        # Placeholde
