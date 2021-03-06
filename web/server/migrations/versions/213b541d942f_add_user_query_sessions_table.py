"""Add user query session table

Revision ID: 213b541d942f
Revises: 853e0e8aa6a0
Create Date: 2019-08-23 17:05:30.862737
Revised 2019-09-30

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '213b541d942f'
down_revision = '853e0e8aa6a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'user_query_session',
        sa.Column('query_uuid', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('query_blob', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='valid_user'),
        sa.PrimaryKeyConstraint('query_uuid'),
    )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_query_session')
    # ### end Alembic commands ###
