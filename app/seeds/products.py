import logging

from sqlmodel import Session
from app.db import engine
from app.models import Product

# https://github.com/tiangolo/full-stack-fastapi-template/blob/master/backend/app/crud.py

with Session(engine) as session:
    products = [
        Product.model_validate(
            {'name': "Test Product", 'description': "This is a test product"}),
        Product.model_validate(
            {'name': "Another Test Product", 'description': "This is another test product"}),
    ]

    session.add_all(products)

    session.commit()
    session.refresh(products[0])
    session.refresh(products[1])

    logging.info("Created products with IDs: %s and %s", products[0].id, products[1].id)
