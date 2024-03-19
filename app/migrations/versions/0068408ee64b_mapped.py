"""mapped

Revision ID: 0068408ee64b
Revises: 7337f19c4677
Create Date: 2024-03-10 18:54:36.876304

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0068408ee64b'
down_revision: Union[str, None] = '7337f19c4677'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('order_items', 'product',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('order_items', 'quantity',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('order_items', 'order_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('orders', 'owner_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('orders', 'address',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=False)
    op.drop_constraint('orders_owner_id_fkey', 'orders', type_='foreignkey')
    op.create_foreign_key(None, 'orders', 'users', ['owner_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'orders', type_='foreignkey')
    op.create_foreign_key('orders_owner_id_fkey', 'orders', 'users', ['owner_id'], ['id'])
    op.alter_column('orders', 'address',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.alter_column('orders', 'owner_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('order_items', 'order_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('order_items', 'quantity',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('order_items', 'product',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###