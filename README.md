# HRMS
> This is a project to deal with the HRM where:
1. GM = General Manager
2. RGM = Regional General Manager
3. AGM = Area General Manager
4. DM = Distributor Manager
   
# The commission scheme:

* If GM sales a certain unit then:
1. GM gets 25 % commission self
2. RGM gets 15 % commission
3. AGM gets 10 % commission
4. DM gets 5 % commission
   
* If RGM sales a certain unit then:
1. AGM gets 15 % commission
2. DM gets 10 % commission

* If AGM sales a certain unit then:
1. DM gets 15 % commission


## How to run the app: 
* install all the dependencies with `pip install -r requirements.txt`
* Navigae to project root and run django server `python manage.py runserver`
* Now server is up and goto 127.0.0.1:8000
> Username and Password for super user is mani

# Technologies Used:
* Django
* Bootstrap
* SQLite