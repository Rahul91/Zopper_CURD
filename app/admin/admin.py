from flask import Blueprint, request, g, redirect, url_for, abort, \
                  render_template



from flask.views import MethodView


from .models import Table

admin = Blueprint('admin', __name__, template_folder='templates')

class CRUDView(MethodView):
	# default template that we will use to display a list
    # of all items in a model
    list_template = 'admin/list_view.html'

    def __init__(self, model, endpoint, list_template=None):
        self.model = model
        self.endpoint = endpoint

        self.path = url_for('.%s' % self.endpoint)
        if list_template:
            self.list_template = list_template


    # all GET methods will link to this function
    def get():
        obj = self.model.query.all()
        return render_template(list_template, obj=obj, path=self.path)
	


view = CRUDView.as_view('Table')


admin.add_url_rule('/Table/', view_func=view, methods=['GET', 'POST'])
