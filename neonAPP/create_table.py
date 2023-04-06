import psycopg2
import sys

def main():

	conn_string = "postgres://crispin.carlos:9dFUIXwRn5ut@ep-throbbing-voice-463758.us-east-2.aws.neon.tech/neondb"

	#Creating table as per requirement
	sql ='''CREATE TABLE EMPLOYEE(
   		FIRST_NAME CHAR(20) NOT NULL,
   		LAST_NAME CHAR(20),
   		AGE INT
	)'''

	try:
		conn = psycopg2.connect(conn_string)

	except:
		print("I am unable to connect to the database") 

	else:
		cursor = conn.cursor()
		print("Connected!\n")

		cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
		cursor.execute(sql)
		print("Table created successfully........")
		conn.commit()

		conn.close()
		cursor.close()
	

if __name__ == "__main__":
	main()


#postgres://crispin.carlos:9dFUIXwRn5ut@ep-throbbing-voice-463758.us-east-2.aws.neon.tech/neondb