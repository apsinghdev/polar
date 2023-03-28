"""tweak issues and prs

Revision ID: 3c9a26ad7774
Revises: 404dfa655fbc
Create Date: 2023-03-02 12:04:48.081654

"""
import sqlalchemy as sa
from alembic import op

# Polar Custom Imports

# revision identifiers, used by Alembic.
revision = "3c9a26ad7774"
down_revision = "404dfa655fbc"
branch_labels: tuple[str] | None = None
depends_on: tuple[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        "issues_organization_name_repository_name_number_key",
        "issues",
        type_="unique",
    )
    op.drop_constraint("issues_token_key", "issues", type_="unique")
    op.create_unique_constraint(
        None,
        "issues",
        ["organization_id", "repository_id", "number"],
    )
    op.drop_column("issues", "organization_name")
    op.drop_column("issues", "repository_name")
    op.drop_column("issues", "lock_reason")
    op.drop_column("issues", "is_locked")
    op.drop_column("issues", "token")
    op.alter_column(
        "pull_requests", "is_draft", existing_type=sa.BOOLEAN(), nullable=True
    )
    op.drop_constraint(
        "pull_requests_organization_name_repository_name_number_key",
        "pull_requests",
        type_="unique",
    )
    op.create_unique_constraint(
        None,
        "pull_requests",
        ["organization_id", "repository_id", "number"],
    )
    op.drop_column("pull_requests", "organization_name")
    op.drop_column("pull_requests", "lock_reason")
    op.drop_column("pull_requests", "is_locked")
    op.drop_column("pull_requests", "repository_name")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "pull_requests",
        sa.Column(
            "repository_name",
            sa.VARCHAR(),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.add_column(
        "pull_requests",
        sa.Column(
            "is_locked",
            sa.BOOLEAN(),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.add_column(
        "pull_requests",
        sa.Column(
            "lock_reason",
            sa.VARCHAR(),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.add_column(
        "pull_requests",
        sa.Column(
            "organization_name",
            sa.VARCHAR(),
            autoincrement=False,
            nullable=False,
        ),
    )
    # Known issue that we resolved in later Alembic version to set our index
    # naming convention and thereby resolve autogeneration of None values.
    op.drop_constraint(None, "pull_requests", type_="unique")  # type: ignore
    op.create_unique_constraint(
        "pull_requests_organization_name_repository_name_number_key",
        "pull_requests",
        ["organization_name", "repository_name", "number"],
    )
    op.alter_column(
        "pull_requests",
        "is_draft",
        existing_type=sa.BOOLEAN(),
        nullable=False,
    )
    op.add_column(
        "issues",
        sa.Column(
            "token",
            sa.VARCHAR(),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.add_column(
        "issues",
        sa.Column(
            "is_locked",
            sa.BOOLEAN(),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.add_column(
        "issues",
        sa.Column(
            "lock_reason",
            sa.VARCHAR(),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.add_column(
        "issues",
        sa.Column(
            "repository_name",
            sa.VARCHAR(),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.add_column(
        "issues",
        sa.Column(
            "organization_name",
            sa.VARCHAR(),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.drop_constraint(None, "issues", type_="unique")  # type: ignore
    op.create_unique_constraint("issues_token_key", "issues", ["token"])
    op.create_unique_constraint(
        "issues_organization_name_repository_name_number_key",
        "issues",
        ["organization_name", "repository_name", "number"],
    )
    # ### end Alembic commands ###
