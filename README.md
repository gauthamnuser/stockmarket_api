# stockmarket_api

# Database settings

DB_DATABASE=stockmarket\
DB_USERNAME=root\
DB_PASSWORD=

run the command below to create appropriate tables for the application

```
python manage.py migrate
```

# Details
Framework: Django\
Database:  MySQL

# API Provider
Financial Modeling Prep

 
# Application
1:Home Page

url: '/'

2:Top Gainers

url: '/topgainers'

3:Top Losers

url: '/toplosers

4:Company Details

url: '/companydetails/{company_symbol}'

