# readingbitcoin-website
The ReadingBitcoin.org website


## Adding an article

1. Add metadata to the `readingbitcoin/articles.py` file
2. Add images to the `readingbitcoin/static` folder
3. Add the article body to `readingbitcoin/templates/articles`

Articles should start with
<pre>
{% extends "article.html" %}
{% block article %}
</pre>
and end with 
<pre>
{% endblock %}
</pre>
