"""null

Revision ID: 2621ca26f956
Revises: 0068408ee64b
Create Date: 2024-03-11 09:36:40.321516

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2621ca26f956'
down_revision: Union[str, None] = '0068408ee64b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('orders', 'totalsum',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('orders', 'totalsum',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
