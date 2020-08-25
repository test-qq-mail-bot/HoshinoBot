import os.path
import peewee as pw

db = pw.SqliteDatabase(
    os.path.join(os.path.dirname(__file__), 'Vortune-data.db')
)

class Vortune(pw.Model):
    qqid = pw.IntegerField(default=0, primary_key = True)
    last_time = pw.TextField()
    vortune_filepath = pw.TextField()
    
    class Meta:
        database = db    

    
def init():
    if not os.path.exists(os.path.join(os.path.dirname(__file__), 'qa.db')):
        db.connect()
        db.create_tables([Vortune])
        db.close()

        
init()