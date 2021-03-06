"""add test_field to user

Revision ID: e7cd98b0da4d
Revises: 25914e647ca8
Create Date: 2020-10-25 18:10:43.368224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7cd98b0da4d'
down_revision = '25914e647ca8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('test_field', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'test_field')
    # ### end Alembic commands ###
