# Webnovel Retail App
This is a Django web application that allows users to browse and purchase webnovels. It includes CRUD functionality for managing novels and authors, as well as a login system to protect certain areas of the site.

# Requirements

To run this project, you will need to have the following software installed on your system:
```
Python 3
Django 3.2
```
# Installation
* Clone this repository to your local machine.
* Navigate to the project directory.
* Install the required Python packages using pip:
* Run the Django development server:
```
python manage.py runserver
```
Open your web browser and navigate to [localhost](http://localhost:8000/) to view the app.
# Usage
## Authentication
The app includes a login system that allows users to create an account, log in, and log out. Certain areas of the site are protected and can only be accessed by authenticated users.

## WebNovel Management
The app allows authenticated users to create, read, update, and delete novels and their corresponding authors or tags. To manage WebNovels, navigate to the /webnovels URL.

## Author and Tag Management
The app allows authenticated users to create, read, update, and delete authors. To manage authors or tags, go to the corresponding urls to fill the forms and create them.

# Credits
This app was created by Same3000. If you have any questions or feedback, please contact me at samy.yacef@epita.fr

# License
This project is licensed under the MIT License. See the LICENSE file for details.
