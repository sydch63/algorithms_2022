from memory_profiler import memory_usage
from pympler import asizeof
from numpy import array

dct_eng_rus = {"one":"один","two":"два","three":"три","four":"четыре","five":"пять","six":"шесть","seven":"семь","eight":"восемь","nine":"девять","ten":"десять"}

def num_translate(word):
    word = word.lower()
    dct_eng_rus.get(word)
    if word in dct_eng_rus.keys():
        return dct_eng_rus.get(word)
    else:
        return dct_eng_rus.get(word)

print(num_translate("one"))
print(num_translate("Five"))
print(asizeof.asizeof(dct_eng_rus))#1784

tpl_eng_rus = ("один","два","три","четыре","пять","шесть","семь","восемь","девять","десять")

def num_translate(number):
    if number in range(len(tpl_eng_rus)):
        return tpl_eng_rus[number-1]
    else:
        return f'no number'

print(num_translate(1))
print(num_translate(5))
print(asizeof.asizeof(tpl_eng_rus))#1784
