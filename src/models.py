from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from eralchemy2 import render_er

db = SQLAlchemy()

## new comment
class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
class Post(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    image_url: Mapped[str] = mapped_column(String(255), nullable=False)
    caption: Mapped[str] = mapped_column(String(255))
    user_id: Mapped[int] = mapped_column(db.ForeignKey("user.id"))
class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(255), nullable=False)
    user_id: Mapped[int] = mapped_column(db.ForeignKey("user.id"))
    post_id: Mapped[int] = mapped_column(db.ForeignKey("post.id"))
class Like(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey("user.id"))
    post_id: Mapped[int] = mapped_column(db.ForeignKey("post.id"))


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            # do not serialize the password, its a security breach
        }
    def serialize(self):
        return {
            "id": self.id,
            "image_url": self.image_url,
            "caption": self.caption,
            "user_id": self.user_id
            # do not serialize the password, its a security breach
        }
    def serialize(self):
        return {
            "id": self.id,
            "image_url": self.image_url,
            "caption": self.caption,
            "post_id": self.user_id
            # do not serialize the password, its a security breach
        }
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "user_id": self.user_id,
            "post_id": self.post_id
            # do not serialize the password, its a security breach
        }
render_er(db.Model, "diagram.png")