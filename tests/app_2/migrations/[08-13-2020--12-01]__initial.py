"""initial

Revision ID: 3b5bf36e6cdf
Revises: 965629534192
Create Date: 2020-08-13 12:01:47.205264

"""
from alembic import op
import sqlalchemy as sa
import enumtables


# revision identifiers, used by Alembic.
revision = "3b5bf36e6cdf"
down_revision = "965629534192"
branch_labels = None
depends_on = "51dfa20071b0"


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "app_2_base_user",
        sa.Column("sex", sa.String(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("username", sa.String(), nullable=True),
        sa.Column("hashed_password", sa.String(), nullable=False),
        sa.Column("date_joined", sa.DateTime(), nullable=True),
        sa.Column("first_name", sa.String(), nullable=True),
        sa.Column("last_name", sa.String(), nullable=True),
        sa.Column("is_staff", sa.Boolean(), nullable=False),
        sa.Column("permission_group", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["permission_group"], ["auth_group.id"],),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("username"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("app_2_base_user")
    # ### end Alembic commands ###
