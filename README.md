# List Management Application

<a name="readme-top"></a>

<br />

  <h3 align="center">SDEV220 Final Project</h3>

  <p align="center">
    A List Management Web Application built with Flask.
    <br />
    <a href="#about-the-project"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://example.com">View Demo</a>
    ·
    <a href="https://github.com/Ivytechstephen/IvyTech-SDEV220-Final-Project/issues">Report Bug</a>
    ·
    <a href="https://github.com/Ivytechstephen/IvyTech-SDEV220-Final-Project/issues">Request Feature</a>
  </p>
</div>



<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



## About The Project

#### Video Demo:  [![List App Video][YouTube.com]][YouTube-url]


![Dashboard Screen Shot][product-screenshot]



The goal of this project is to provide a seamless way to manage daily tasks, shopping lists, and job requirements.
* **Create & Organize:** Easily create new lists for any purpose.
* **Templating System:** Save frequently used lists as templates to save time.
* **Track Progress:** Mark items as completed and manage quantities dynamically.
* **Secure:** User authentication ensures your data remains private.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

These are the frameworks, libraries, and software used to bring this project to life.

* [![Python][Python.com]][Python-url]
* [![Flask][Flask.com]][Flask-url]
* [![Jinja][Jinja.com]][Jinja-url]
* [![SQLAlchemy][SQLAlchemy.com]][SQLAlchemy-url]
* [![SQLite][SQLite.com]][SQLite-url]
* [![HTML][HTML.com]][HTML-url]
* [![CSS][CSS.com]][CSS-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![Javascript][Javascript.com]][Javascript-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Getting Started
To get the server up and running follow these steps.

* Start by cloning the repository
    ```sh
    git clone https://github.com/Ivytechstephen/IvyTech-SDEV220-Final-Project.git
    ```
* Navigate into the project directory
    ```sh
    cd IvyTech-SDEV220-Final-Project
    ```
* Set up python virtual environment
    ```sh
    python3 -m venv venv
    ```
* Activate python virtual environment
    ```sh
    # On Linux use:
    source venv/bin/activate
    # On Windows use: 
    source venv\Scripts\activate
    ```
* Install dependencies
    ```sh
    pip install -r requirements.txt
    ```
* Run the Application
    ```sh
    python app.py
    ```
* Open your browser and enter this local address
    ```sh
    http://127.0.0.1:5000/
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Dependencies

This is a list of Dependencies needed to run the Server.

* Flask
    ```sh
    pip install flask
    ```
* SQLAlchemy
    ```sh
    pip install flask_sqlalchemy
    ```
* Flask Session
    ```sh
    pip install flask_session
    ```
* Werkzeug
    ```sh
    pip install werkzeug
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Usage

First, register an account to access the secure dashboard.
From the dashboard, you can start a fresh list or load a pre-saved template.
Use the "Save as Template" feature to backup lists you use frequently.


![List View Screen Shot][product-screenshot2]

*Above: The List View showing items, quantities, and the editing.*

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Roadmap

- [x] Core CRUD Functionality
- [x] User Authentication (Register/Login)
- [x] Item Quantity Management (Increase/Decrease)
- [x] Template System (Save/Load/Preview/Edit/Delete)
- [x] Delete Confirmation
- [ ] Automatically Login after Registration
- [ ] Add Quanity Editing to Templates
- [ ] Add List Output to Email 
- [ ] Add reordering
- [ ] Add Dark Mode Toggle

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Contact

Your Name - [My LinkedIn](https://www.linkedin.com/in/stephen-littman/) - [My GitHub](https://github.com/anarchking)

Project Link - [List-Management-App-Repo](https://github.com/Ivytechstephen/IvyTech-SDEV220-Final-Project/issues)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Acknowledgments

This is a list of some useful tools and resources used in the study of this project.

* [Flask Documentation](https://flask.palletsprojects.com/)
* [Bootstrap 5](https://getbootstrap.com/)
* [SQLAlchemy Documentation](https://www.sqlalchemy.org/)
* [Jinja2](https://jinja.palletsprojects.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



[product-screenshot]: static/images/dashboard_screenshot.gif
[product-screenshot2]: static/images/list_view_screenshot.gif

[YouTube.com]: https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white
[YouTube-url]: https://youtu.be/s52GovBQQmk

[Python.com]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/

[Flask.com]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/

[Jinja.com]: https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black
[Jinja-url]: https://jinja.palletsprojects.com/

[SQLAlchemy.com]: https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white
[SQLAlchemy-url]: https://www.sqlalchemy.org/

[SQLite.com]: https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white
[SQLite-url]: https://sqlite.org/

[HTML.com]: https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white
[HTML-url]: https://www.w3.org/html/

[CSS.com]: https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white
[CSS-url]: https://www.w3.org/Style/CSS/Overview.en.html

[Javascript.com]: https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E
[Javascript-url]: https://www.javascript.com/

[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
