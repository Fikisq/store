"""Add parent_id to categories

Revision ID: 5e302476cf7c
Revises: bdf1206a0b67
Create Date: 2026-11-16 16:18:15.558460

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e302476cf7c'
down_revision: Union[str, Sequence[str], None] = 'bdf1206a0b67'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    with op.batch_alter_table('categories') as batch:
        batch.add_column(sa.Column('parent_id', sa.Integer(), nullable=True))
        batch.create_foreign_key(
            'fk_categories_parent_id', 'categories', ['parent_id'], ['id']
        )


def downgrade() -> None:
    """Downgrade schema."""
    with op.batch_alter_table('categories') as batch:
        batch.drop_constraint('fk_categories_parent_id', type_='foreignkey')
        batch.drop_column('parent_id')
