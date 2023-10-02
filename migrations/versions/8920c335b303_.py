"""empty message

Revision ID: 8920c335b303
Revises: 648a13a649a4
Create Date: 2023-09-25 21:59:10.951886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8920c335b303'
down_revision = '648a13a649a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
