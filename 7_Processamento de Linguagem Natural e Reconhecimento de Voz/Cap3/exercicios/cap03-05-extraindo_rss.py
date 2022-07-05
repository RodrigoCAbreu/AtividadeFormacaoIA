# Extraindo Texto de RSS

# pip install feedparser
import feedparser

myFeed = feedparser.parse("http://feeds.mashable.com/Mashable")
print('Título do Feed Title :', myFeed['feed']['title'])
print('Número de Posts :', len(myFeed.entries))
post = myFeed.entries[0]
print('Título do Post :',post.title)
content = post.content[0].value
print('Conteúdo :\n', content)