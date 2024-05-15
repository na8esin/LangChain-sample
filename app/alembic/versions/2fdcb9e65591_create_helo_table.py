"""create helo table

Revision ID: 2fdcb9e65591
Revises: dfebef2f0749
Create Date: 2024-05-14 10:37:52.590211

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '2fdcb9e65591'
down_revision: Union[str, None] = 'dfebef2f0749'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hero',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('secret_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('products', 'name',
               existing_type=mysql.VARCHAR(collation='utf8mb4_bin', length=50),
               type_=sqlmodel.sql.sqltypes.AutoString(),
               existing_nullable=False)
    op.alter_column('products', 'description',
               existing_type=mysql.VARCHAR(collation='utf8mb4_bin', length=200),
               type_=sqlmodel.sql.sqltypes.AutoString(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'description',
               existing_type=sqlmodel.sql.sqltypes.AutoString(),
               type_=mysql.VARCHAR(collation='utf8mb4_bin', length=200),
               existing_nullable=True)
    op.alter_column('products', 'name',
               existing_type=sqlmodel.sql.sqltypes.AutoString(),
               type_=mysql.VARCHAR(collation='utf8mb4_bin', length=50),
               existing_nullable=False)
    op.drop_table('hero')
    # ### end Alembic commands ###
