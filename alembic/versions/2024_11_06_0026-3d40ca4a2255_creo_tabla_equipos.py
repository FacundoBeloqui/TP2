"""Creo tabla equipos

Revision ID: 3d40ca4a2255
Revises: fb180cfd34fa
Create Date: 2024-11-06 00:26:43.581684

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d40ca4a2255'
down_revision: Union[str, None] = 'fb180cfd34fa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "equipo",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("nombre", sa.Text, nullable=False),
        sa.Column("generacion", sa.Integer, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("equipo")