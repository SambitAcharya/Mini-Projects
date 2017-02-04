var twit = require('twit');
var config = require('../config.js');

var Twitter = new twit(config);
// function to select a random tweet from an array of tweets
function getRandomTweet (arr) {
  var index = Math.floor(Math.random()*arr.length);
  return arr[index];
};

module.exports = {
    like : function(){
    var params = {
        q: '#nodejs, #Nodejs',
        result_type: 'recent',
        lang: 'en'
    }
    Twitter.get('search/tweets', params, function(err,data){

      var tweet = data.statuses;
      var randomTweet = getRandomTweet(tweet);   // pick a random tweet

      if(typeof randomTweet != 'undefined'){
        Twitter.post('favorites/create', {id: randomTweet.id_str}, function(err, response){
          if(err){
            console.log('A tweet couldn\'t be liked');
          }
          else{
            console.log('A tweet has been successfully liked');
          }
        });
      }
    });
  }
}
