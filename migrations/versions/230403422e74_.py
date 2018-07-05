"""empty message

Revision ID: 230403422e74
Revises: 88b286b63f1a
Create Date: 2018-06-08 17:46:16.036051

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '230403422e74'
down_revision = '88b286b63f1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('t_user', sa.Column('role_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 't_user', 'role', ['role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 't_user', type_='foreignkey')
    op.drop_column('t_user', 'role_id')
    # ### end Alembic commands ###
