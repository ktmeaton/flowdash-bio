"""no database

Revision ID: e2bc6261f314
Revises: 
Create Date: 2020-10-24 15:50:06.667346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2bc6261f314'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('remember_me', sa.Boolean(), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('workflow',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('system', sa.String(length=64), nullable=True),
    sa.Column('node', sa.String(length=64), nullable=True),
    sa.Column('status', sa.String(length=64), nullable=True),
    sa.Column('progress', sa.Integer(), nullable=True),
    sa.Column('total_jobs', sa.Integer(), nullable=True),
    sa.Column('completed_jobs', sa.Integer(), nullable=True),
    sa.Column('running_jobs', sa.Integer(), nullable=True),
    sa.Column('failed_jobs', sa.Integer(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_workflow_start_date'), 'workflow', ['start_date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_workflow_start_date'), table_name='workflow')
    op.drop_table('workflow')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
