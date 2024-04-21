from langchain_community.utilities import SQLDatabase
import os
from dotenv import load_dotenv

load_dotenv()

db = SQLDatabase.from_uri(f'mysql://root:@127.0.0.1:3309/{os.environ['DB_NAME']}')
print(db.dialect)
print(db.get_usable_table_names())
print(db.run("SELECT * FROM products LIMIT 10;"))