var twit = require('twit');
var config = require('../config.js');

var Twitter = new twit(config);

module.exports = {

    retweet : function() {
      var params = {
          q: '#nodejs, #Nodejs',  // REQUIRED
          result_type: 'recent',
          lang: 'en'
      }

      Twitter.get('search/tweets', params, function(err, data) {
          if (!err) {

              var retweetId = data.statuses[0].id_str;
              Twitter.post('statuses/retweet/:id', {
                  id: retweetId
              }, function(err, response) {
                  if (response) {
                      console.log('Retweeted!!!');
                  }
                  if (err) {
                      console.log('Something went wrong while retweeting');
                  }
              });
          }
          else {
            console.log('Something went wrong while searching');
          }
      });
  }
}
