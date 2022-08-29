# Image retrive in the database
# Import the required modules
import mysql.connector
import base64
from PIL import Image
import io

# For security reasons, never expose your password
#password = open('password','r').readline()

# Create a connection
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="12345678",
	database="database" # Name of the database
)

# Create a cursor object
cursor = mydb.cursor()

# Prepare the query
query = 'SELECT PICTURE FROM PROFILE WHERE ID=103'

# Execute the query to get the file
cursor.execute(query)

data = cursor.fetchall()

# The returned data will be a list of list
image = data[0][0]

# Decode the string
binary_data = base64.b64decode(image)

# Convert the bytes into a PIL image
image = Image.open(io.BytesIO(binary_data))

# Display the image
image.show()
