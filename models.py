from sqlmodel import Field, SQLModel

# omymodelsで生成して、ちょっと修正
class Products(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    description: str | None = None

# SQLModelのチュートリアルのコードをコピペ
class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None