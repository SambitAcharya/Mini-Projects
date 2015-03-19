import newspaper

cnn_paper = newspaper.build('http://cnn.com')

art = []
cat = []

for article in cnn_paper.articles:
    art.append(article.url)

for category in cnn_paper.category_urls():
    cat.append(category)

print len(art)
print len(cat)
