"""remove is_admin from user

Revision ID: 25914e647ca8
Revises: 2885461cffba
Create Date: 2020-10-25 17:58:42.172853

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25914e647ca8'
down_revision = '2885461cffba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_admin')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_admin', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
