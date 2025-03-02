from src.contato.infra.contato_model import Contato
from sqlalchemy.orm import Session

from ... import db


class ContatoRepository:
    def __init__(self):
        self.db = db.session

    def create(self, contato: Contato):
        try:
            self.db.add(contato)
            self.db.commit()
            self.db.refresh(contato)
            return contato.toJson()
        except Exception as e:
            self.db.rollback()
            print(f"Erro ao criar contato: {e}")
            return None

    def get_all(self):
        contatos = self.db.query(Contato).all()
        return [contato.toJson() for contato in contatos] if contatos else []

    def get_by_id(self, id: int):
        contato = self.db.query(Contato).filter(Contato.con_id == id).first()
        return contato.toJson() if contato else None

    def get_by_doc(self, doc: str):
        contato = self.db.query(Contato).filter(Contato.con_doc == doc).first()
        return contato.toJson() if contato else None

    def update(self, id: int, updated_data: dict):
        existing_contato = self.db.query(Contato).filter(Contato.con_id == id).first()

        if not existing_contato:
            return None

        try:
            for key, value in updated_data.items():
                if hasattr(existing_contato, key):  # Verifica se o campo existe no modelo
                    setattr(existing_contato, key, value)

            self.db.commit()
            updated_rows = self.db.query(Contato).filter(Contato.con_id == id).count()
            return updated_rows 
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Erro ao atualizar o contato {id}: {e}")

    def delete(self, id: int):
        contato = self.db.query(Contato).filter(Contato.con_id == id).first()
        if not contato:
            return False
        try:
            self.db.delete(contato)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Erro ao deletar contato {id}: {e}")
