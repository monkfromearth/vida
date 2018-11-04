function Vida(source, target){
	window.vidaClient = this;
	window.sentence = [];
	this.routes = {
	    'api:authorize':'/api/authorize',
	    'api:help#languages':'/api/help/languages',
	    'api:engine#transliterate':'/api/engine/transliterate'
	};
	this.setup = function(){
		NProgress.start();
		$.post(window.vidaClient.routes['api:authorize'], {}, function(ajax){
			if (ajax.status)
				window.csrf_token = ajax.content.csrf_token;
			else {
				console.error("Couldn't authenticate the SDK.");
				return false;
			}
			NProgress.done();
		}).fail(function(e, s, t){
			NProgress.done();
			console.error(e);
			console.error(s);
			console.error(t);
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
	this.setTransliteratedText = function(id, word, replacement){
		console.log(word);
		console.log(replacement);
		var cursorPosition = $(id).prop("selectionStart");
		word = word.split(" ");
		replacement = replacement.split(" ");
		for (var i = 0; i < word.length; i++){
			var text = $(id).val().replace(new RegExp(word[i], 'gi'), replacement[i]);
			$(id).val(text);
		}
		text = text.split(" ");
		window.sentence = text;
		$(id).prop('selectionEnd', cursorPosition + 1);
	};
	this.compareSentence = function(a1, a2) {
	    var a = [], diff = [];
	    for (var i = 0; i < a1.length; i++) a[a1[i]] = true;
	    for (var i = 0; i < a2.length; i++) {
	        if (a[a2[i]]) delete a[a2[i]];
	        else a[a2[i]] = true;
		}
		for (var k in a) diff.push(k);
		return diff;
	};
	this.startEngine = function(id){
		this.setup();
		$(id).keypress(function(e){
			if (e.keyCode == 32){
				var text = $(id).val().split(" ");
				var word = $(text).not(window.sentence).get();
				word = word.join(" ").trim();
				if (word.length == 0) return false;
				$.post(window.vidaClient.routes['api:engine#transliterate'], {
					csrf_token:window.csrf_token,
					source:window.vidaClient.source, 
					target:window.vidaClient.target,
					text:word
				}, function(ajax){
					if (ajax.status) 
						window.vidaClient.setTransliteratedText(id, word, ajax.content.output);
					console.log(ajax);
				}).fail(function(e, s, t){
					console.log(e, s, t)
				});
			};
		});
	};
};