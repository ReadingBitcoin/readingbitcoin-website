from flask import Flask, render_template

from readingbitcoin.articles import articles_data

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fonts/<font_name>')
def fonts(font_name):
    return ''


@app.route('/articles/')
def articles():
    return render_template('articles.html', articles_data=articles_data)


@app.route('/articles/<file_name>/')
def article(file_name):
    article_data = [a for a in articles_data if a['file_name'] == file_name][0]
    return render_template(
        'articles/{file_name}.html'.format(file_name=file_name),
        article_data=article_data)


if __name__ == '__main__':
    app.run(debug=True, port=7808)
