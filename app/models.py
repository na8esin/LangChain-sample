from sqlmodel import Field, SQLModel


class Product(SQLModel, table=True):
    __tablename__ = "products"

    # idはpython上は、Noneにできるけど、DDL上はちゃんと↓のようになってる
    # `id` int NOT NULL AUTO_INCREMENT
    # https://sqlmodel.tiangolo.com/tutorial/insert/#whats-next
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str | None = None


# SQLModelのチュートリアルのコードをコピペ
class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None