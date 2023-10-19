"""add content column to posts table

Revision ID: de9df40dda1f
Revises: 0382b85d481a
Create Date: 2023-10-19 08:30:30.357953

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de9df40dda1f'
down_revision: Union[str, None] = '0382b85d481a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable= False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
