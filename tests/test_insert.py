
from backend.models.user import User, Logins
from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.database.connection import SessionLocal

session = SessionLocal()

user = User(
    nome="akira",
    email="akira@example.com",
    cpf="12345678900",
    created_at=datetime.now()
)

login = Logins(cpf='12345678900', password_hash='1234')
user.logins.append(login)

session.add(user)
session.commit()

usuarios = session.query(User).all()
for u in usuarios:
    print(f"ID: {u.id}, Nome: {u.nome}, CPF: {u.cpf}, Email: {u.email}")
    for l in u.logins:
        print(f"  Login ID: {l.id}, Password: {l.password_hash}")