# Importing data from database using SQLite3
# A good practice is to save/commit your transactions using the commit() function
# even if you are only reading the data.

import pandas as pd
import sqlite3

# open engine connection
con=sqlite3.connect('./files/sample_test.db')

# create a cursor object
cur = con.cursor()

# Perform query: rs
rs = cur.execute('select * from TEST')

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())

# Close connection
con.commit()

# Print head of DataFrame df
df.head()
