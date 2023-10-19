"""add last few columns to posts table

Revision ID: f945fff88c10
Revises: 53d3dc72a0a0
Create Date: 2023-10-19 08:50:44.335191

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f945fff88c10'
down_revision: Union[str, None] = '53d3dc72a0a0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable= False, server_default= 'TRUE'))
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable= False, server_default= sa.text('NOW()')
    ))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
