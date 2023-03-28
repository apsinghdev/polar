"""issues_references_synced_at

Revision ID: dc19b85fe8a6
Revises: 7f3d2182a4fb
Create Date: 2023-03-22 08:53:07.202973

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# Polar Custom Imports

# revision identifiers, used by Alembic.
revision = "dc19b85fe8a6"
down_revision = "7f3d2182a4fb"
branch_labels: tuple[str] | None = None
depends_on: tuple[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "repositories",
        sa.Column(
            "issues_references_synced_at", sa.TIMESTAMP(timezone=True), nullable=True
        ),
    )
    op.drop_column("repositories", "repository_issues_references_synced_at")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "repositories",
        sa.Column(
            "repository_issues_references_synced_at",
            postgresql.TIMESTAMP(timezone=True),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.drop_column("repositories", "issues_references_synced_at")
    # ### end Alembic commands ###
