function rand(min,max){
	return Math.floor(Math.random()*(max-min+1))+min;
}

(function(document, undefined){
	
var winner_box = document.querySelector('#winner span'),
	choose_btn = document.getElementById('choose-winner'),
	players = document.getElementById('players'),
	last_winner;

choose_btn.addEventListener('click', function() {
	get_winner(players.value.split(",").filter(function(name){
		return name !== "";
	}));
}, false);

function get_winner(names){
	
	var index = -1, looper;

	(function __cycle(){	
		
		var name =  names[++index % names.length];
		winner_box.textContent = name;
		looper = setTimeout(__cycle, 70);
			
	})();

	setTimeout(function(){
		var name;
		clearTimeout(looper);

		do{
			name = names[rand(0, names.length - 1)];
		}while(name == last_winner);
		last_winner = name;
		winner_box.textContent = name;

	}, rand(350, 700));
 }

})(document);
