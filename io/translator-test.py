from translate import Translator

translator = Translator(to_lang='ja')

try:
    with open('eng.txt', mode='r') as file_in:
        text = file_in.read()
        translation = translator.translate(text)

        with open('ja.txt', mode='w') as file_out:
            file_out.write(translation)
except FileNotFoundError as err:
    print('check whether your file exists')

print('Done!')
