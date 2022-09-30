heroku container:login
heroku container:push web --app $APPNAME
heroku container:release web --app $APPNAME
heroku container:release web --app $APPNAME