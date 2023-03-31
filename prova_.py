# Para a criação dos ambientes do venv será necessário os seguintes comandos: 
# c:\>c:\Python35\python -m venv c:\path\to\myenv


# pip install SQLALchemy # instalação do SQLALchemy 

#importações das principais bibliotecas 
from flask import session
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


engine = create_engine("sqlite://", echo=True) #criação ddas novas conexões do banco de dados

class Base(DeclarativeBase): # criação de classe do mapeamento declarativo das tabelas 

    pass 

class NomedoJogo(Base): 
    __tablename__ = "NomedoJogo"
    id: Mapped[int] = mapped_column(primary_key=True)

class Plataforma(): 
    __tablename__ = "Plataforma"
    id: Mapped[int] = mapped_column(primary_key=True)

class Preço(): 
    __tablename__ = "Preço"
    id: Mapped[int] = mapped_column(primary_key=True)

class Quantidade(): 
    __tablename__ = "Quantidade"
    id: Mapped[int] = mapped_column(primary_key=True)


# POST para enivar as informações para o banco de dados e integrar com o front-end 

with Session(engine) as Session:

    nome = NomedoJogo(
    nome1 = ["DEAD SPACE REMAKE"], 
    nome2 = ["FORSPOKEN"], 
    nome3 = ["DEAD ISLAND"],
    nome4 = ["HOGWARTS LEGACY"],
    nome5 = ["WILD HEARTS"],
    nome6 = ["RESIDENT EVIL 4"],
    nome7= ["THE LEGEND OF ZELDA: TEARS OF THE KINGDOM"])
    

    plataforma = Plataforma(
    plataforma1 = ["PS5"], 
    plataforma2 = ["PC"], 
    plataforma3 = ["XBox Series"],
    plataforma4= ["Switch"]) 

    preço = Preço(
    preço1 = ["R$ 350,00"], 
    preço2 = ["R$ 299,00"], 
    preço3= ["R$ 219,00"], 
    preço4= ["R$ 289,00"], 
    ) 

    quantidade = Quantidade(
    quantidade1 = ["7"], 
    quantidade2 = ["8"], 
    quantidade3= ["10"], 
    ) 
    
    nome = NomedoJogo(nome1="DEAD SPACE REMAKE",plataforma="PS5", preço="R$ 350,00", quantidade="10" )

    session.add_all([DEAD SPACE REMAKE, FORSPOKEN, DEAD ISLAND, HOGWARTS LEGACY, WILD HEARTS,RESIDENT EVIL 4, THE LEGEND OF ZELDA: TEARS OF THE KINGDOM])
    session.comit()


    








