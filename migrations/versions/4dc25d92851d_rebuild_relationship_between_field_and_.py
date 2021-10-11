"""rebuild relationship between field and seed tables

Revision ID: 4dc25d92851d
Revises: ce645d2f4d89
Create Date: 2021-10-10 06:41:35.573366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4dc25d92851d'
down_revision = 'ce645d2f4d89'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('seed', sa.Column('field_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'seed', 'field', ['field_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'seed', type_='foreignkey')
    op.drop_column('seed', 'field_id')
    # ### end Alembic commands ###