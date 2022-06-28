from translate import Translator
import pdb

translator = Translator(to_lang='zh')

with open('eng.txt') as file_in:
    with open('cn.txt', mode='w') as file_out:
        for line in file_in:
            text = translator.translate(line)
            file_out.write(text + '\n')

print('Done!')
