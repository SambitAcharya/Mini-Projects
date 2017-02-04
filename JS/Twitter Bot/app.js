var actions = require('./actions')

actions.retweet.retweet();
setInterval(actions.retweet.retweet, 3000000);

actions.like.like();
setInterval(actions.like.like, 3600000);
