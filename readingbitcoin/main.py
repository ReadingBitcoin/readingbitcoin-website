from flask import Flask, render_template

from readingbitcoin.articles import articles_data
from readingbitcoin.constants import language_map

app = Flask(__name__)


@app.route('/', defaults={'language': None})
@app.route('/<language>/')
def index(language=None):
    if language is None:
        language_code = None
    else:
        language_code = language_map[language]
    return render_template('index.html',
                           language_code=language_code)


@app.route('/fonts/<font_name>')
def fonts(font_name):
    return ''


@app.route('/articles/', defaults={'language': None})
@app.route('/articles/<language>/')
def articles(language=None):
    if language is None:
        language_code = None
    else:
        language_code = language_map[language]
    return render_template('articles.html',
                           articles_data=articles_data,
                           language_code=language_code)


@app.route('/articles/<year>/<month>/<file_name>/', defaults={'language': None})
@app.route('/articles/<year>/<month>/<file_name>/<language>/')
def article(year, month, file_name, language=None):
    article_data = [a for a in articles_data if a['file_name'] == file_name][0]
    template_name = 'articles/{file_name}.html'.format(file_name=file_name)
    if language is None:
        language_code = None
    else:
        language_code = language_map[language]
    return render_template(template_name,
                           article_data=article_data,
                           language_code=language_code)


@app.route('/about/', defaults={'language': None})
@app.route('/about/<language>/')
def about(language=None):
    if language is None:
        language_code = None
    else:
        language_code = language_map[language]
    return render_template('about.html',
                           language_code=language_code)


if __name__ == '__main__':
    app.run(debug=True, port=7808)
