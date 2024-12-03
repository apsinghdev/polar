"""Remove Invite

Revision ID: 39ce508b936c
Revises: 2daaffbdf32e
Create Date: 2024-12-03 09:21:23.927870

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# Polar Custom Imports

# revision identifiers, used by Alembic.
revision = "39ce508b936c"
down_revision = "2daaffbdf32e"
branch_labels: tuple[str] | None = None
depends_on: tuple[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("ix_invites_code", table_name="invites")
    op.drop_index("ix_invites_created_at", table_name="invites")
    op.drop_index("ix_invites_deleted_at", table_name="invites")
    op.drop_index("ix_invites_modified_at", table_name="invites")
    op.drop_table("invites")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "invites",
        sa.Column("created_by", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column("claimed_by", sa.UUID(), autoincrement=False, nullable=True),
        sa.Column("code", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("note", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("id", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "modified_at",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column(
            "deleted_at",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["claimed_by"], ["users.id"], name="invites_claimed_by_fkey"
        ),
        sa.ForeignKeyConstraint(
            ["created_by"], ["users.id"], name="invites_created_by_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="invites_pkey"),
    )
    op.create_index("ix_invites_modified_at", "invites", ["modified_at"], unique=False)
    op.create_index("ix_invites_deleted_at", "invites", ["deleted_at"], unique=False)
    op.create_index("ix_invites_created_at", "invites", ["created_at"], unique=False)
    op.create_index("ix_invites_code", "invites", ["code"], unique=True)
    # ### end Alembic commands ###
