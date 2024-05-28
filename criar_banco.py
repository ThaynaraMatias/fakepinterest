from newpinterest import database, app
from newpinterest.models import Usuario, Foto

with app.app_context():
    database.create_all()