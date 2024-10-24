"""Make PersonalAccessToken.expires_at nullable

Revision ID: ace3b0ceefc3
Revises: a2f8da11b9ce
Create Date: 2024-10-24 15:32:22.517737

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# Polar Custom Imports

# revision identifiers, used by Alembic.
revision = "ace3b0ceefc3"
down_revision = "a2f8da11b9ce"
branch_labels: tuple[str] | None = None
depends_on: tuple[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "personal_access_tokens",
        "expires_at",
        existing_type=postgresql.TIMESTAMP(timezone=True),
        nullable=True,
    )
    op.create_index(
        op.f("ix_personal_access_tokens_expires_at"),
        "personal_access_tokens",
        ["expires_at"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_personal_access_tokens_expires_at"),
        table_name="personal_access_tokens",
    )
    op.alter_column(
        "personal_access_tokens",
        "expires_at",
        existing_type=postgresql.TIMESTAMP(timezone=True),
        nullable=False,
    )
    # ### end Alembic commands ###