"""drop table

Revision ID: d4d14480b650
Revises: 25d814bc83ed
Create Date: 2024-12-17 22:16:10.438782

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd4d14480b650'
down_revision: Union[str, None] = '25d814bc83ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
