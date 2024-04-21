from modules.expansion import emagoedivExpansion

expansion = emagoedivExpansion()

text = 'a handsome man'

for i in range(64):
    print(expansion(text, seed=i))
