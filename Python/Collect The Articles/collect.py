import newspaper

cnn_paper = newspaper.build('http://cnn.com')

art = []
cat = []

# for article in cnn_paper.articles:
#     art.append(article.url)
#
# for category in cnn_paper.category_urls():
#     cat.append(category)

article = cnn_paper.articles[0]
article.download()
article.parse()
# html = article.html
text = article.text
authors = article.authors
# print html
print authors
print text
