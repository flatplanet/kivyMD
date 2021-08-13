from kivy.lang import Builder
from kivymd.app import MDApp
#import sqlite3
import mysql.connector



class MainApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"

		# Create Database Or Connect To One
		#conn = sqlite3.connect('first_db.db')
		
		# Define DB Stuff
		mydb = mysql.connector.connect(
			host = "localhost", 
			user = "root",
			passwd = "password123",
			database = "second_db",
			)

		# Create A Cursor
		c = mydb.cursor()

		# Create an actual database
		c.execute("CREATE DATABASE IF NOT EXISTS second_db")

		# Check to see if database was created
		#c.execute("SHOW DATABASES")
		#for db in c:
		#	print(db)



		# Create A Table
		c.execute("""CREATE TABLE if not exists customers(
			name VARCHAR(50))
		 """)

		# Check to see if table created
		#c.execute("SELECT * FROM customers")
		#print(c.description)



		# Commit our changes
		mydb.commit()

		# Close our connection
		mydb.close()

		return Builder.load_file('second_db.kv')



	def submit(self):
		# Create Database Or Connect To One
		#conn = sqlite3.connect('first_db.db')
		mydb = mysql.connector.connect(
			host = "localhost", 
			user = "root",
			passwd = "password123",
			database = "second_db",
			)

		# Create A Cursor
		c = mydb.cursor()

		

		# Add A Record
		sql_command = "INSERT INTO customers (name) VALUES (%s)"
		values = (self.root.ids.word_input.text,)
		
		# Execute SQL Command
		c.execute(sql_command, values)	
		

		# Add a little message
		self.root.ids.word_label.text = f'{self.root.ids.word_input.text} Added'

		# Clear the input box
		
		self.root.ids.word_input.text = ''


		# Commit our changes
		mydb.commit()

		# Close our connection
		mydb.close()

		

	def show_records(self):
		# Create Database Or Connect To One
		#conn = sqlite3.connect('first_db.db')
		mydb = mysql.connector.connect(
			host = "localhost", 
			user = "root",
			passwd = "password123",
			database = "second_db",
			)

		# Create A Cursor
		c = mydb.cursor()

		
		# Grab records from database
		c.execute("SELECT * FROM customers")
		records = c.fetchall()

		word = ''
		# Loop thru records
		for record in records:
			word = f'{word}\n{record[0]}'
			self.root.ids.word_label.text = f'{word}'

		# Commit our changes
		mydb.commit()

		# Close our connection
		mydb.close()



MainApp().run()
