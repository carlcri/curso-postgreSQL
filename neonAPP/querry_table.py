import psycopg2
import os, pprint
from dotenv import load_dotenv

def main():

	# Load config from .env file
	load_dotenv()
	NEON_URI = os.environ["NEON_URI"]

#	conn_string = "postgres://crispin.carlos:9dFUIXwRn5ut@ep-throbbing-voice-463758.us-east-2.aws.neon.tech/neondb"

	#Creating table as per requirement
	sql ='''SELECT * FROM employee'''

	try:
		conn = psycopg2.connect(NEON_URI)

	except:
		print("I am unable to connect to the database") 

	else:
		cursor = conn.cursor()
		print("Connected!\n")

		cursor.execute(sql)
		record = cursor.fetchall()

		pprint.pprint(record)
		print(type(record))

		conn.close()
		cursor.close()
	

if __name__ == "__main__":
	main()


#postgres://crispin.carlos:9dFUIXwRn5ut@ep-throbbing-voice-463758.us-east-2.aws.neon.tech/neondb