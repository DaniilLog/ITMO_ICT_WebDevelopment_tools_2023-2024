"""salary legal status added

Revision ID: af732e7fae6f
Revises: 
Create Date: 2024-09-07 15:39:16.485577

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'af732e7fae6f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('salary', 'legal')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('salary', sa.Column('legal', sa.BOOLEAN(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
