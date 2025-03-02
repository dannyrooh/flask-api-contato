from sqlalchemy import Column, Integer, String, DateTime, func, inspect

from ... import db


class Contato(db.Model):
    __tablename__ = 'contato'

    con_id = Column(Integer, primary_key=True, autoincrement=True)
    con_root = Column(Integer, nullable=True)
    con_tipo = Column(Integer, nullable=True)
    con_ident = Column(String(32), nullable=False)
    con_nome = Column(String(128), nullable=False)
    con_codigo = Column(Integer, nullable=True)
    con_doc = Column(String(64), nullable=True)
    con_hash = Column(String(64), nullable=True)
    con_private_token = Column(Integer, nullable=True)
    con_createdat = Column(DateTime, server_default=func.current_timestamp(), nullable=False)
    con_updatedat = Column(DateTime, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), nullable=False)

    __table_args__ = (
        db.Index('idx_con_nome', 'con_nome'),
        db.Index('idx_con_codigo', 'con_codigo'),
        db.Index('idx_con_doc', 'con_doc'),
        db.Index('idx_con_hash', 'con_hash'),
    )


    def toDict(self): 
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
    
    def __repr__(self):
        return "<%r>" % self.toJson()    
    
    def toJson(self):   
            return {"id": self.con_id, 
                    "nome": self.con_nome, 
                    "ident": self.con_ident, 
                    "codigo": self.con_codigo, 
                    "doc": self.con_doc, 
                    "tipo": self.con_tipo, 
                    "hash": self.con_hash, 
                    "root": self.con_root}     
