from pystardict import Dictionary
import os
import sys
import re
reload(sys)
sys.setdefaultencoding('utf8')

dicts_dir = os.path.join(os.path.dirname(__file__))
# pierwszy arg to katalog, drugi to nazwa pliku bez rozszerzenia 
pl_ru = Dictionary(os.path.join(dicts_dir, 'pl_ru', 'pl_ru_slovnik'))
ru_pl = Dictionary(os.path.join(dicts_dir, 'ru_pl', 'ru_pl_slovnik'))
synonyms = Dictionary(os.path.join(dicts_dir, 'Soule_Synonyms', 'Soule'))
ru_en = Dictionary(os.path.join(dicts_dir, 'stardict-rus_eng_full-2.4.2', 'rus_eng_full'))
wordnet = Dictionary(os.path.join(dicts_dir, 'WordNet', 'WordNet'))
wordnet = Dictionary(os.path.join(dicts_dir, 'WordNet', 'WordNet'))
#collins = Dictionary(os.path.join(dicts_dir, 'Collins', 'Collins Thesaurus'))
phonohack = Dictionary(os.path.join(dicts_dir, 'transcription', 'trans'))
pl_en  = Dictionary(os.path.join(dicts_dir, 'dic', 'pl-en'))
pl_syn = Dictionary(os.path.join(dicts_dir, 'dic', 'pl-syn'))
kosciuszko = Dictionary(os.path.join(dicts_dir, 'dic', '00kosciuszkoa'))
kosciuszko2 = Dictionary(os.path.join(dicts_dir, 'dic', '00kosciuszkop'))
frazes = Dictionary(os.path.join(dicts_dir, 'dic', 'frazes'))
thesaurus = Dictionary(os.path.join(dicts_dir, 'dic', 'thesaurus-ee'))
#obcy = Dictionary(os.path.join(dicts_dir, 'dic', 'obcy'))
#polski = Dictionary(os.path.join(dicts_dir, 'dic', 'polski'))
chambers = Dictionary(os.path.join(dicts_dir, 'Chambers_Thesaurus', 'chambers'))
collins = Dictionary(os.path.join(dicts_dir, 'Collins', 'collins'))
#longman = Dictionary(os.path.join(dicts_dir, 'Longman', 'Longman'))
#macmillan = Dictionary(os.path.join(dicts_dir, 'macmillan_thesaurus', 'macmillan'))
#oxford = Dictionary(os.path.join(dicts_dir, 'Oxford_English', 'oxford1'))
#webster = Dictionary(os.path.join(dicts_dir, 'Webster_Unabridged', 'webster'))
roget2 = Dictionary(os.path.join(dicts_dir, 'rogetII', 'Roget'))
advanced = Dictionary(os.path.join(dicts_dir, 'Oxford_Advanced_Learner', 'advanced'))

def hyperonym(zmienna):
  ontos = wordnet[zmienna]
  kstring = re.findall(ur'Hypernyms.*</co>', ontos)
  przedszkole_krefka = re.findall(r'<kref>\w+\s\w+</kref>', str(kstring))
  if len(przedszkole_krefka) == 0:
    przedszkole_krefka = re.findall(r'<kref>\w+</kref>', str(kstring))
  shyper = re.sub("</?kref>","", str(przedszkole_krefka))
  redhyp =  re.sub("(\[|\]|')","", shyper)
  manipro = redhyp.split(",")

#  1 = re.sub("\[","", shyper)
#  2 = re.sub("\]","", 1)
#  3 = re.sub("'","", 2)
#  print 2
#  splist = lhyper.split(",")
#  print splist
#  splist = list(splist)
  return manipro


# rex2 = "theos"
# regex2 = re.compile('({}|{})'.format(rex1, rex2))
# test_rex1 ="anthropos"
# regex2.findall(test_rex1)

# to find oud and fully acquire other classes 
def hyponym(zmienna):
  ontos = wordnet[zmienna]
  kstring = re.findall(ur'Hyponyms.*</co>', ontos)
  przedszkole_krefka = re.findall(r'<kref>\w+\s\w+</kref>', str(kstring))
  if len(przedszkole_krefka) == 0:
    przedszkole_krefka = re.findall(r'<kref>\w+</kref>', str(kstring))
  shyper = re.sub("</?kref>","", str(przedszkole_krefka))
  redhyp =  re.sub("(\[|\]|')","", shyper)
  manipro = redhyp.split(",")
  return manipro








if __name__ == '__main__':
  hyperonym(zmienna)
  hyponym(zmienna)
