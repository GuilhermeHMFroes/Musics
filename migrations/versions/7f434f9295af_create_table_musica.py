"""create table Musica

Revision ID: 7f434f9295af
Revises: 
Create Date: 2023-04-02 01:34:37.509520

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f434f9295af'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('music',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.String(length=80), nullable=False),
    sa.Column('artista', sa.String(length=80), nullable=False),
    sa.Column('video', sa.String(length=800), nullable=False),
    sa.Column('link', sa.String(length=800), nullable=False),
    sa.Column('genero', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('music')
    # ### end Alembic commands ###