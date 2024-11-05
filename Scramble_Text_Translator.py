
import string
import math

def load_dictionary(file_name):
     with open(file_name, 'r') as file:
        words = file.read().splitlines()
        return words

def binary_search(sorted_words, targeted_words):
    low, high = 0, len(sorted_words) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_words[mid] == targeted_words:
            return mid
        elif sorted_words[mid] < targeted_words:
            low = mid + 1
        else:
            high = mid - 1
    return None

def clean_up_words(word_list, text):
    word_array = text.split()
    corrected_text = []

    for scrambled_text in word_array:
        punctuation = ''

        if scrambled_text[-1] in string.punctuation:
            punctuation = scrambled_text[-1]
            scrambled_text = scrambled_text[:-1]

        word_lowercase = scrambled_text.lower()

        if len(word_lowercase) > 3:
            target = word_lowercase[0] + ''.join(sorted(word_lowercase[1:-1])) + word_lowercase[-1]
        else:
            target = word_lowercase

        for word in word_list:
            if len(word) == len(scrambled_text) and target == (word[0] + ''.join(sorted(word[1:-1])) + word[-1]):
                if scrambled_text.istitle():
                    corrected_text.append(word.capitalize() + punctuation)
                else:
                    corrected_text.append(word + punctuation)
                break
        else:
            corrected_text.append(scrambled_text + punctuation)

    return text, ' '.join(corrected_text)


def main( ) :

   passage1 = '''\
Aoccdrnig to rsceareh at an Elingsh uinervtisy, it deosnt \
mttaer in waht oredr the ltteers in a wrod are, the olny iprmoatnt \
tihng is taht the frist and lsat ltteer is at the rghit pclae. The \
rset can be a toatl mses and you can sitll raed it wouthit a \
porbelm. Tihs is bcuseae hmuan biegns do not raed ervey lteter by itslef \
but the wrod as a wlohe! Nxet \
To! Etu? Brute? A! to! etu? brute? a! Aslo'''

   passage2 = '''\
I cnat blveiee taht I can aulaclty uesdnatnrd tihs! The \
phaonmneel pweor of the hmuan mnid is qiute remarkable. I awlyas thought taht \
slpeling was ipmorantt too, but apparnelty tihs is not so. Hevower \
wihle it is rieealtvly esay to raed sroht wrods, it is not so esay wehn ridaneg \
legonr wdros. Aslo, msot wdros in Esinglh are sveen leertts lnog or leognr, and \
the mroe leretts terhe are in a wrod, the mroe dulcifift it bmeecos to cletrorcy \
infietdy them wehn the ltrtees are ragnearerd. Mroe cmoomn wrdos lkie blal \
and baer raimen mltsoy ungnchead and esay to rizocenge, whereas, lgneor and less \
cmoomn wdros, like pltuonuim and soulamitunes caghne saillbattunsy scuh taht \
rnciooitegn is srclceay pbsslioe. This atiibly smtes form a garet deal \
of enpicerexe rindaeg cretolcry slelepd wdros and only plopee who can \
adrealy raed pelictroinfy can do this tsak. Tihs tirck does not reeavl \
mcuh aoubt the pscroes of lnnreaig to raed, it only ietaindcs that hhligy \
slielkd rrdeaes can omoercve moinr informieepcts wehn dnriiveg mnnaeig!'''

   book = load_dictionary("dictionary.txt")

   mixed,good = clean_up_words(book, passage1)

   print("\n=SCRAMBLED=============================================================================")
   print("original:")
   wc = 1
   for w in mixed.split(' ') :
      if wc % 9 == 0 :
         print( )
      print(w, end=" ")
      wc += 1

   print("\n=CLEANED===============================================================================")
   print("cleaned:")
   wc = 1
   for w in good.split(' ') :
      if wc % 9 == 0 :
         print( )
      print(w, end =" ")
      wc += 1

   mixed,good = clean_up_words(book, passage2)

   print("\n=SCRAMBLED=============================================================================")
   print("original:")
   wc = 1
   for w in mixed.split(' ') :
      if wc % 9 == 0 :
         print( )
      print(w, end=" ")
      wc += 1

   print("\n=CLEANED===============================================================================")
   print("cleaned:")
   wc = 1
   for w in good.split(' ') :
      if wc % 9 == 0 :
         print( )
      print(w, end =" ")
      wc += 1
   print( )

if __name__ == "__main__" :
   main( )