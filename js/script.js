function rand(min,max){
	return Math.floor(Math.random()*(max-min+1))+min;
}

(function(document, undefined){
	
var winner_box = document.querySelector('#winner span'),
	choose_btn = document.getElementById('choose-winner'),
	add_btn = document.getElementById('add'),
	players = document.getElementById('players'),
	last_winner;

choose_btn.addEventListener('click', function() {
	
	var li = players.getElementsByTagName("li");
	var names_array = [];
	for(var i=0; i<li.length; i++){
		
		var liChildren = li.item(i).childNodes;
		
		for(var j=0; j<liChildren.length; j++)
			if(liChildren.item(j).nodeType == liChildren.item(j).TEXT_NODE)
				names_array.push( liChildren.item(j).nodeValue );
		
	}

	get_winner(names_array.filter(function(name){
	 	return name !== "";
	}));
	
}, false);

add_btn.addEventListener('click', function() {
		var textInput = document.getElementById("newPlayers");
		var playerName = textInput.value;
		var li= document.createElement("li");
		li.innerHTML=playerName;
		players.appendChild(li);
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
