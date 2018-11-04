function Vida(source, target){
	window.vidaClient = this;
	window.sentence = [];
	this.host = "https://vidacorp.ml";
	this.routes = {
	    'api:authorize':'/api/authorize',
	    'api:help#languages':'/api/help/languages',
	    'api:engine#transliterate':'/api/engine/transliterate'
	};
	this.setup = function(){
		NProgress.start();
		$.post(window.vidaClient.host + window.vidaClient.routes['api:authorize'], {}, function(ajax){
			if (ajax.status)
				window.csrf_token = ajax.content.csrf_token;
			else {
				console.error("Couldn't authenticate the SDK.");
				return false;
			}
			NProgress.done();
		}).fail(function(e, s, t){
			NProgress.done();
			console.error(e, s, t);
		});
		if ($.inArray(this.source, Object.keys(this.codes)) == -1){
			console.error("Please specify the correct code for the source langauge;");
			return false;
		}
		if ($.inArray(this.target, Object.keys(this.codes)) == -1){
			console.error("Please specify the correct code for the target langauge;");
			return false;
		}
	};
	this.codes = languages = {
		"hin": "Hindi",
		"ben": "Bengali",
		"guj": "Gujarati",
		"pun": "Punjabi",
		"mal": "Malayalam",
		"kan": "Kannada",
		"tam": "Tamil",
		"tel": "Telugu",
		"ori": "Oriya",
		"mar": "Marathi",
		"ass": "Assamese",
		"kon": "Konkani",
		"bod": "Bodo",
		"nep": "Nepali",
		"urd": "Urdu",
		"eng": "English"
	};
	this.source = source;
	this.target = target;
	this.text = null;
	this.config = function(name, value){
		if (name == 'source')
			this.source = value;
		if (name == 'target')
			this.target = value;
	};
	this.options = {
		valueBasedInputs:[
			'TEXTAREA',
			'INPUT',
			'SELECT'
		]
	};
	this.setTransliteratedText = function(id, word, replacement){
		var text;
		word = word.split(" ");
		replacement = replacement.split(" ");
		for (var i = 0; i < word.length; i++){
			replacement[i] = replacement[i].replace(/[?=]/g, "");
			if ($.inArray($(id)[0].tagName, window.vidaClient.options.valueBasedInputs) != -1){
				text = $(id).val().replace(new RegExp(word[i], 'gi'), replacement[i]);
				$(id).val(text);
			} else {
				text = $(id).text().replace(new RegExp(word[i], 'gi'), replacement[i]);
				$(id).text(text);
				window.vidaClient.setCaretPosition(id, text.length);
			}
		}
		text = text.split(" ");
		window.sentence = text;
	};
	this.setCaretPosition = function(id, pos){
		var content  = document.getElementById(id.slice(1));
		content.focus();
	    var sel; // character at which to place caret
		if (document.selection) {
		  sel = document.selection.createRange();
		  sel.moveStart('character', pos);
		  sel.select();
		}
		else {
		   sel = window.getSelection();
		   sel.collapse(content.firstChild, pos);
		}
	};
	this.startEngine = function(id){
		this.setup();
		$(id).keypress(function(e){
			if (e.keyCode == 32){
				var text, word;
				if ($.inArray($(id)[0].tagName, window.vidaClient.options.valueBasedInputs) != -1)
					text = $(id).val().split(" ");
				else
					text = $(id).text().split(" ");
				word = $(text).not(window.sentence).get();
				word = word.join(" ").trim();
				if (word.length == 0) return false;
				$.post(window.vidaClient.host + window.vidaClient.routes['api:engine#transliterate'], {
					csrf_token:window.csrf_token,
					source:window.vidaClient.source, 
					target:window.vidaClient.target,
					text:word
				}, function(ajax){
					if (ajax.status) 
						window.vidaClient.setTransliteratedText(id, word, ajax.content.output);
				}).fail(function(e, s, t){
					console.log(e, s, t)
				});
			};
		});
	};
};