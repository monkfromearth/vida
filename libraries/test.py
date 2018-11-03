from vida import Vida

source = raw_input()
target = raw_input()
text = raw_input()

vidacorp = Vida(text, source, target)

print vidacorp.run()