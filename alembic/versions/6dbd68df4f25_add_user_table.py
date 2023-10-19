"""add user table

Revision ID: 6dbd68df4f25
Revises: de9df40dda1f
Create Date: 2023-10-19 08:34:56.911543

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6dbd68df4f25'
down_revision: Union[str, None] = 'de9df40dda1f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users', 
                    sa.Column('id', sa.Integer(), nullable= False),
                    sa.Column('email', sa.String(), nullable= False),
                    sa.Column('password', sa.String(), nullable= False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable= False, server_default= sa.text('now()')),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
