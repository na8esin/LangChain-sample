from omymodels import create_models

# カレントディレクトリにmodels.pyが生成される

ddl = """
CREATE TABLE products (
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(200),
    PRIMARY KEY (id)
);


"""
result = create_models(ddl, models_type='pydantic')['code']

print(result)

# $ py app/models_generate.py
# <unknown>:1: SyntaxWarning: invalid escape sequence '\#'
# <unknown>:1: SyntaxWarning: invalid escape sequence '\-'
# from typing import Optional
# from pydantic import BaseModel


# class Products(BaseModel):

#     id: int
#     name: str
#     description: Optional[str]
