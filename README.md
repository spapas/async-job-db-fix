# async-job-db-fix

A companion project to the https://spapas.github.io/2019/02/25/django-fix-async-db/ article. Helps you understand why you see problems when you use your database with async jobs and how to fix it.

Should work fine on windows: Install and run redis (using WSL) and then run win_rqworker.bat to start the async worker and rs.bat to start the server (of course you need a venv with the requirements installed: https://spapas.github.io/2017/12/20/python-2-3-windows/)
