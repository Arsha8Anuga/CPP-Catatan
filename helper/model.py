from sqlalchemy import ForeignKey, String, Enum, DateTime
from typing import List, Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Status(Enum):
    pending = "PENDING"
    in_progress = "IN PROGRESS"
    finished = "FINISHED"
    submitted = "SUBMITTED"

class Book(Base):
    __tablename__ = 'book'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    author: Mapped[str] = mapped_column(String(30))
    subject_id: Mapped[int] = mapped_column(ForeignKey('subject.id'))

    subject: Mapped['Subject'] = relationship(back_populates='books')


class Subject(Base):
    __tablename__ = 'subject'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    lecturer: Mapped[str] = mapped_column(String(30))
    code: Mapped[str] = mapped_column(String(20), unique=True, nullable=True)

    books: Mapped[List['Book']] = relationship(back_populates='subject', cascade='all, delete-orphan')
    todos: Mapped[List['Todo']] = relationship(back_populates='subject', cascade='all, delete-orphan')
    schedules: Mapped[List['Schedule']] = relationship(back_populates='subject', cascade='all, delete-orphan')

class Todo(Base):
    __tablename__ = 'todolist'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    class_name: Mapped[str] = mapped_column(String(30))
    status: Mapped[Enum] = mapped_column(Enum(Status), nullable=False)
    deadline: Mapped[DateTime] = mapped_column(DateTime)
    subject_id: Mapped[int] = mapped_column(ForeignKey('subject.id'))
    note: Mapped[str] = mapped_column(String(30), nullable=True)

    subject: Mapped['Subject'] = relationship(back_populates='todos')

class Schedule(Base):
    __tablename__ = 'schedule'

    id: Mapped[int] = mapped_column(primary_key=True)
    subject_id: Mapped[int] = mapped_column(ForeignKey('subject.id'))
    date: Mapped[DateTime] = mapped_column(DateTime)

    subject: Mapped['Subject'] = relationship(back_populates='schedules')