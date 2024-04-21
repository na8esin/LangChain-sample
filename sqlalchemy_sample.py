from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

e = create_engine(f'mysql://root:@127.0.0.1:3309/{os.environ['DB_NAME']}', echo=True)
with e.connect() as conn:
  print(conn.execute(text("select * from products")).all())
