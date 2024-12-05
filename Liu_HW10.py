# -*- coding: utf-8 -*-
"""HW 10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FxC6EmmrUUXpMDnXs944FJEHbH-jaoia
"""

#Student Name:Zhizhong Liu
#Assignment:HW 10
#Last Modify Date:12/05/2024

import sqlite3
import pandas as pd

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    publication_year INTEGER NOT NULL
)
""")

conn.commit()
books_data = [
    ("Dream of the Red Chamber", "Cao Xueqin", 1791),
    ("Journey to the West", "Wu Cheng'en", 1592),
    ("The Three-Body Problem", "Liu Cixin", 2008),
    ("Ordinary World", "Lu Yao", 1986),
    ("Fortress Besieged", "Qian Zhongshu", 1947)
]

cursor.executemany("INSERT INTO books (title, author, publication_year) VALUES (?, ?, ?)", books_data)
conn.commit()

#Search books publish after year 2000
cursor.execute("SELECT * FROM books WHERE publication_year > 2000")
records_after_2000 = cursor.fetchall()
print("Books published after 2000:")
for record in records_after_2000:
    print(record)

#update
cursor.execute("UPDATE books SET author = 'Liu Cixin (Updated)' WHERE title = 'The Three-Body Problem'")
conn.commit()

#delete
cursor.execute("DELETE FROM books WHERE title = 'Fortress Besieged'")
conn.commit()

#transfer data to pandas dataframe
df = pd.read_sql_query("SELECT * FROM books", conn)
print("\nBooks table as DataFrame:")
print(df)

#add books type
genres = ["Fiction", "Adventure", "Science Fiction", "Realism"]
df["genre"] = genres * (len(df) // len(genres)) + genres[:len(df) % len(genres)]

#update and add gener
df.to_sql("books", conn, if_exists="replace", index=False)

#look through update
updated_df = pd.read_sql_query("SELECT * FROM books", conn)
print("\nUpdated books table with genres:")
print(updated_df)

#close database
conn.close()