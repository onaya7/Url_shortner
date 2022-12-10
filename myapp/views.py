from flask import Blueprint, redirect, render_template, current_app, request
from myapp.models import db, Link

view = Blueprint('view', __name__,  template_folder='template', static_folder='static')

@view.route('/<short_url>')
def redirect_to_url(short_url):
    print(short_url)
    link = Link.query.filter_by(short_url=short_url).first_or_404()
    link.visits = link.visits +1
    db.session.commit()
    return redirect(link.original_url)

@view.route('/')
def index():
    return render_template('home.html')


@view.route('/add_link', methods=['POST'])
def add_link():
    original_url =request.form.get('original_url')
    link = Link(original_url=original_url)
    db.session.add(link)
    db.session.commit()

    return render_template('link_added.html', new_link=link.short_url, original_url=link.original_url)


@view.route('/stats')
def stats():
    link = Link.query.all()
    return render_template('stats.html', link=link)


@view.errorhandler(404)
def page_not_found():
    return ' ', 404
