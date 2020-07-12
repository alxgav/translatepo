from googletrans import Translator
import pprint


translator = Translator()

sourceFile = 'source/tutor-uk.po'
outFile = 'out/tutor-uk.po'

resLanguage = []
id = 1
tFile = open(outFile, 'w')
with open(sourceFile, 'r') as file:
    # resLanguage = file.readlines()
    for i in file:
        if 'msgstr' not in i:
            tFile.write(i)
        if "msgid" in i:
            if i !='""':
                t = translator.translate(i, dest='uk').text
                print(t, id)
                id +=1
            tFile.write(f'{t}\n')


        


# pprint.pprint(resLanguage)
# result = translator.translate('%1$s - There is a newer version of WordPress available (%2$s)', dest='uk')

# print (result.text)