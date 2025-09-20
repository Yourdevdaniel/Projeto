from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, DateTime
from backend.database.base import Base
from typing import List, Optional
from datetime import datetime

class User(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(30))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    email: Mapped[str] = mapped_column(String)
    cpf: Mapped[str] = mapped_column(String(11), nullable=False, unique=True )

    logins: Mapped[List["Logins"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

class Logins(Base):
    __tablename__ = "login"
    id: Mapped[int] = mapped_column(primary_key=True)
    cpf: Mapped[str] = mapped_column(ForeignKey("usuarios.cpf"))
    password_hash: Mapped[str] = mapped_column(String, nullable=False)

    user: Mapped["User"] = relationship(back_populates="logins")



