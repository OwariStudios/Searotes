import os

from .document import Document


class Documents:
    def __init__(self, path):
        self.path = path;
        self.documents = [];

        self.load_data();

    def load_data(self):
        documents = [os.path.join(dp, f) for dp, dn, filenames in os.walk(self.path) for f in filenames if os.path.splitext(f)[1] == '.pdf' or os.path.splitext(f)[1] == ".docx"];

        for document in documents:
            self.documents.append(Document(document));
    
    def search(self, text):
        results = [];
        for document in self.documents:
            data = document.search(text, 500);

            for result in data:
                results.append({"fullpath": document.fullpath, "file": document.name + document.extension, "data": result });

        return results;
