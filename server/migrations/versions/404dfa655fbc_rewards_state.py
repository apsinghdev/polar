"""rewards state

Revision ID: 404dfa655fbc
Revises: 489ecfd46540
Create Date: 2023-03-01 13:35:18.097859

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "404dfa655fbc"
down_revision = "489ecfd46540"
branch_labels: tuple[str] | None = None
depends_on: tuple[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "rewards",
        sa.Column("state", sa.String(), nullable=False, server_default="created"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("rewards", "state")
    # ### end Alembic commands ###
