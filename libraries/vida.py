from repo import Repo
from indictrans import Transliterator
import enchant


class Vida:
	"""
	Only focused on English to 15 Indic Language Transliteration
	Hindi (hin)
	Bengali (ben)
	Gujarati (guj)
	Punjabi (pun)
	Malayalam (mal)
	Kannada (kan)
	Tamil (tam)
	Telugu (tel)
	Oriya (ori)
	Marathi (mar)
	Assamese (ass)
	Konkani (kon)
	Bodo (bod)
	Nepali (nep)
	Urdu (urd)
	English (eng)
	"""

	languages = {
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
	}

	codes = languages.keys()

	@staticmethod
	def is_ascii(s): return all(ord(c) < 128 for c in s)

	def __init__(self, text, source, target):
		self.text = text
		self.source = source
		self.target = target
		self.isEngSource = (self.source == 'eng')
		if self.isEngSource:
			self.usdictionary = enchant.Dict("en_US")
			self.gbdictionary = enchant.Dict("en_GB")
		self.validated = self.source in self.codes and self.target in self.codes
		if self.validated:
			self.engine = Transliterator(source=self.source, target=self.target)
		
	def run(self):
		status = False; message = "Couldn't transliterate the text."; content = {}
		output = []
		if not self.validated:
			message = "Please provide languages and their code."
			output = self.text
		else:
			text = self.text.split()
			try:
				for index in xrange(len(text)):
					word = text[index]
					if not self.isEngSource:
						word = word.decode('utf-8')
						output.insert(index, self.engine.transform(word).encode('utf-8'))
					else:
						if not Vida.is_ascii(word): word = word.decode('utf-8')
						if not self.usdictionary.check(word) and not self.gbdictionary.check(word):
							output.insert(index, self.engine.transform(word).encode('utf-8'))
						else: 
							output.insert(index, word)
				status = True
				message = "Succesfully transliterated the code."
			except UnicodeDecodeError, e:
				Repo.exception(e)
				message = "Couldn't decode the language properly."
			except IndexError, e:
				Repo.exception(e)
				message = "Couldn't properly frame the sentence."
			output = ' '.join(output)
		output = output.decode('utf-8')
		content['output'] = output
		return Repo.api('libraries:vida#run', status, message, content)