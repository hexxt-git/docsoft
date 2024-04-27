from flask import Flask, request
from pdfminer.high_level import extract_text
import collections
import re
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Configuration de la base de données PostgreSQL avec SQLAlchemy
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:agoudjil@localhost:5017/api"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class RepeatedWord(Base):
    __tablename__ = "repeated_words"

    id = Column(Integer, primary_key=True, index=True)
    word = Column(String, index=True)
    count = Column(Integer)
    file_name = Column(String, index=True)  # Ajout d'un champ pour le nom du fichier
    workspace_id = Column(Integer)  # Ajout du champ pour l'identifiant de l'espace de travail

Base.metadata.create_all(bind=engine)

def extract_and_process_text(pdf_file_path):
    # Extraction du texte du PDF
    text = extract_text(pdf_file_path)

    # Tokenization et comptage des occurrences de chaque mot
    words = re.findall(r'\b\w{3,}\b', text.lower())
    word_counts = collections.Counter(words)

    # Filtrage des mots répétés plus de 3 fois
    repeated_words = {word: count for word, count in word_counts.items() if count > 3}

    return repeated_words

@app.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file:
        # Enregistrer le fichier sur le disque
        file_path = 'uploads/' + file.filename
        file.save(file_path)

        # Extraire et traiter le texte du PDF
        repeated_words = extract_and_process_text(file_path)

        # Insérer les mots répétés dans la base de données
        db = SessionLocal()
        try:
            for word, count in repeated_words.items():
                db_word = RepeatedWord(word=word, count=count, file_name=file.filename, workspace_id=request.form.get('workspace_id'))
                db.add(db_word)
            db.commit()
            return 'File uploaded successfully and words processed'
        finally:
            db.close()
    else:
        return 'Error uploading file'

if __name__ == '__main__':
    app.run(debug=True, port=5001)
