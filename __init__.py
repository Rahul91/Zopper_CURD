from admin import admin # the Blueprint instance that we created
app.register_blueprint(admin, url_prefix='/admin')