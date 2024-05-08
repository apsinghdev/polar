"""org and user blocking

Revision ID: 22b6469a1294
Revises: 5b96b5f08ddc
Create Date: 2024-05-14 13:24:45.231403

"""

import sqlalchemy as sa
from alembic import op

# Polar Custom Imports
from polar.kit.extensions.sqlalchemy import PostgresUUID

# revision identifiers, used by Alembic.
revision = "22b6469a1294"
down_revision = "5b96b5f08ddc"
branch_labels: tuple[str] | None = None
depends_on: tuple[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "organizations",
        sa.Column("blocked_at", sa.TIMESTAMP(timezone=True), nullable=True),
    )
    op.add_column(
        "users", sa.Column("blocked_at", sa.TIMESTAMP(timezone=True), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "blocked_at")
    op.drop_column("organizations", "blocked_at")
    # ### end Alembic commands ###