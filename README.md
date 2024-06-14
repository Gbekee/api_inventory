
  <h1>Online Store Inventory and Supplier Management API
</h1>
<h2>Background</h2>
<p>The system is developed to handle the following aspects efficiently:</p>
1) Managing inventory items<br>
2) Managing supplier information<br>
3) Establishing relationships between inventory items and supplier<br>
4) Performing CRUD functionalities for items and suppliers<br>
<h2>Prerequisites:</h2>
<p> 
  1) Python 3.12,<br>
  2) djangorestframework 3.15.1<br>
  3) django 5.0.6<br>
</p>
<h2>Project Setup</h2>
CLone my repository using: <a href='https://github.com/Gbekee/api_inventory.git'> clone repo</a><br>
cd project
<h3>Setup virtual environment</h3>
python -m venv venv<br>
cd venv/Scripts<br>
activate<br>
cd..<br>
cd..<br>
<h3>Install dependencies</h3>
pip install -r requirements.txt<br>
<h3>Set up database</h3>
python manage.py makemigrations<br>
python manage.py migrate
<h3>Run development server</h3>
python manage.py runsever<br>
Development server will be running on  http://127.0.0.1:8000 <br>
<h2>Performing operations on the API</h2><br>
<b>URL Patterns</b>:<br><br>
  1) /items: Retrieve list of items or create a new item.<br><br>
  2) /suppliers: Retrieve list of suppliers or create a new supplier.<br><br>
  3) /items/<str:pk>: Retrieve, update, or delete a specific item.<br><br>
  4) /suppliers/<str:pk>: Retrieve or update a specific supplier.<br><br>
<h3>Testing the API<br></h3>
    
1) GET /items: Retrieve all items

2) POST /items: Create a new item

3) GET /items/str:pk: Retrieve a specific item

4) PUT /items/str:pk: Update a specific item

5) DELETE /items/str:pk: Delete a specific item

6) GET /suppliers: Retrieve all suppliers

7) POST /suppliers: Create a new supplier

8) GET /suppliers/str:pk: Retrieve a specific supplier

9) PUT /suppliesr/str:pk: Update a specific supplier
<hr>
<br>
<b>This documentation provides a comprehensive guide for setting up, using, and understanding the Online Store Inventory and Supplier Management API. For further details or assistance, please refer to the source code and comments within the code.</b>
<br>
