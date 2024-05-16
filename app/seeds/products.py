import logging

from sqlmodel import Session
from app.db import engine
from app.models import Product
from sqlalchemy.sql import text as sa_text

# https://github.com/tiangolo/full-stack-fastapi-template/blob/master/backend/app/crud.py
with Session(engine) as session:
    session.exec(sa_text('''TRUNCATE TABLE products''').execution_options(autocommit=True))

    products = [
        Product.model_validate({
                'name': "Test Product",
                'description': "This is a test product",
                "price": "100.00"
        }),
        Product.model_validate({
                'name': "Another Test Product",
                'description': "This is another test product",
                "price": "200.00"
        }),
    ]

    session.add_all(products)

    session.commit()
    session.refresh(products[0])
    session.refresh(products[1])

    logging.info("Created products with IDs: %s and %s", products[0].id, products[1].id)
