# [Black Dashboard Django](https://www.creative-tim.com/product/black-dashboard-django) [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social&logo=twitter)](https://twitter.com/home?status=Material%20Dashboard,%20a%20free%20Material%20Bootstrap%204%20Admin%20Template%20%E2%9D%A4%EF%B8%8F%20https%3A//bit.ly/2Lyat1Y%20%23bootstrap%20%23material%20%23design%20%23developers%20%23freebie%20%20via%20%40CreativeTim)

 ![version](https://img.shields.io/badge/version-1.0.1-blue.svg) [![GitHub issues open](https://img.shields.io/github/issues/creativetimofficial/black-dashboard-django.svg?maxAge=2592000)](https://github.com/creativetimofficial/black-dashboard-django/issues?q=is%3Aopen+is%3Aissue) [![GitHub issues closed](https://img.shields.io/github/issues-closed-raw/creativetimofficial/black-dashboard-django.svg?maxAge=2592000)](https://github.com/creativetimofficial/black-dashboard-django/issues?q=is%3Aissue+is%3Aclosed) [![Join the chat at https://gitter.im/NIT-dgp/General](https://badges.gitter.im/NIT-dgp/General.svg)](https://gitter.im/creative-tim-general/Lobby) [![Chat](https://img.shields.io/badge/chat-on%20discord-7289da.svg)](https://discord.gg/E4aHAQy)

Open-source **[Django Template](https://github.com/nimaprgrmr?tab=repositories)** crafted on top of **Black Dashboard**, a popular Bootstrap 4 design. Start your development with a modern, dark-themed Bootstrap 4 Admin template for Django. It features a huge number of components built to fit together and look fantastic. 

- ✅ `Up-to-date dependencies`
- ✅ Database: `sqlite`
- ✅ UI-Ready app, Django Native ORM
- ✅ `Session-Based authentication`, Forms validation

<br />

[![Black Dashboard Django - Admin Dashboard coded in Django.](https://user-images.githubusercontent.com/51070104/214890715-43a927f1-afea-4f09-9da8-965ba8102b07.png)](https://github.com/nimaprgrmr?tab=repositories)

<br />

## Table of Contents

* [Demo](#demo)
* [Quick Start](#quick-start)
* [Documentation](#documentation)
* [File Structure](#file-structure)
* [Browser Support](#browser-support)
* [Resources](#resources)
* [Reporting Issues](#reporting-issues)
* [Technical Support or Questions](#technical-support-or-questions)
* [Licensing](#licensing)
* [Useful Links](#useful-links)

<br />

## Demo

> To authenticate use the default credentials ***test / ApS12_ZZs8*** or create a new user on the **registration page**.

- **Black Dashboard Django** [Login Page](https://github.com/nimaprgrmr?tab=repositorieso)

<br />

## Quick start

> UNZIP the sources or clone the repository. After getting the code, open a terminal and navigate to the working directory, with product source code.

```bash
$ git clone https://github.com/app-generator/django-black-dashboard.git
$ cd django-black-dashboard
```

<br />

### 👉 Set Up for `Unix`, `MacOS` 

> Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

> Note: To use the app, please access the registration page and create a new user. After authentication, the app will unlock the private pages.

<br />

## Documentation

The documentation for the **Black Dashboard Django** is hosted at our [website](https://github.com/nimaprgrmr?tab=repositories).

<br />

## File Structure
Within the download you'll find the following directories and files:

```bash
< PROJECT ROOT >
   |
   |-- core/                               # Implements app configuration
   |    |-- settings.py                    # Defines Global Settings
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- views.py                  # Serve HTML pages for authenticated users
   |    |    |-- urls.py                   # Define some super simple routes  
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- urls.py                   # Define authentication routes  
   |    |    |-- views.py                  # Handles login and registration  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- layouts/                   # Master pages
   |         |    |-- base-fullscreen.html  # Used by Authentication pages
   |         |    |-- base.html             # Used by common pages
   |         |
   |         |-- accounts/                  # Authentication pages
   |         |    |-- login.html            # Login page
   |         |    |-- register.html         # Register page
   |         |
   |         |-- home/                      # UI Kit Pages
   |              |-- index.html            # Index page
   |              |-- 404-page.html         # 404 page
   |              |-- *.html                # All other pages
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- manage.py                            # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

> The bootstrap flow

- Django bootstrapper `manage.py` uses `core/settings.py` as the main configuration file
- `core/settings.py` loads the app magic from `.env` file
- Redirect the guest users to Login page
- Unlock the pages served by *app* node for authenticated users

<br />

## Resources

- Support: <https://github.com/nimaprgrmr?tab=repositories>
- Issues: [Github Issues Page](https://github.com/nimaprgrmr/black-dashboard-django-master/issues)

<br />

## Reporting Issues

We use GitHub Issues as the official bug tracker for the **Black Dashboard Django**. Here are some advices for our users that want to report an issue:

1. Make sure that you are using the latest version of the **Black Dashboard Django**. Check the CHANGELOG from your dashboard on our [website](https://github.com/nimaprgrmr?tab=repositories).
2. Providing us reproducible steps for the issue will shorten the time it takes for it to be fixed.
3. Some issues may be browser-specific, so specifying in what browser you encountered the issue might help.

<br />

## Technical Support or Questions

If you have questions or need help integrating the product please [contact us](https://github.com/nimaprgrmr?tab=repositories) instead of opening an issue.

<br />

## Licensing

- Copyright 2019 - present [Creative Tim](https://github.com/nimaprgrmr?tab=repositories)

<br />

## Useful Links

- [More products](https://github.com/nimaprgrmr?tab=repositories) from Nima A.t

<br />
