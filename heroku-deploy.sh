heroku container:login
heroku container:push web --app vnnews-scrapper
heroku container:release web --app vnnews-scrapper
heroku container:release web --app vnnews-scrapper