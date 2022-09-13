"""empty message

Revision ID: 4360cc29b3c7
Revises: cbcce28b06dd
Create Date: 2022-08-21 00:06:41.782370

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4360cc29b3c7'
down_revision = 'cbcce28b06dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('Show_artist_id_fkey', 'Show', type_='foreignkey')
    op.drop_constraint('Show_venue_id_fkey', 'Show', type_='foreignkey')
    op.create_foreign_key(None, 'Show', 'Venue', ['venue_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'Show', 'Artist', ['artist_id'], ['id'], ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.create_foreign_key('Show_venue_id_fkey', 'Show', 'Venue', ['venue_id'], ['id'])
    op.create_foreign_key('Show_artist_id_fkey', 'Show', 'Artist', ['artist_id'], ['id'])
    # ### end Alembic commands ###