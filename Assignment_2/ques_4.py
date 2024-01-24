x=['apple', 'issue', 'beach', 'coral', 'money', 'avoid', 'fable', 'aware', 'happy', 'giant','hairy', 'acute', 'goofy', 'humid', 'alcon', 'there', 'agent', 'knife', 'dress', 'large','model', 'alive', 'lucid', 'lumpy', 'smash', 'mauve', 'basis', 'entry', 'arise', 'onion','birth', 'admit', 'petal', 'begin', 'error', 'plump', 'brave', 'proud', 'while', 'faith','event', 'blood', 'queen', 'reign', 'rugby', 'north', 'print', 'shape', 'until', 'since','skill', 'swamp', 'sweep', 'swirl', 'tempt', 'torch', 'trash', 'tulip', 'vivid', 'which']
import random
def generate1():
    index=random.randint(0,49)
    return index
index1=generate1()
def is_word_in_dictionary(word, app_id, app_key):
    import requests
    language = 'en-us'
    word_id = word.lower()
    url="https://od-api.oxforddictionaries.com/api/v2/" + "entries" + "/" + language + "/" + word_id
    r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
    if r.status_code == 200:
        return True
    elif r.status_code == 404:
       return False
    else:
        print(f'Error {r.status_code}: {r.text}')
        return False
word1=x[index1]
for i in range(7):
    if i==6:
        print("you have exhausted the number of tries available")
        print("the word was",word1)
        print("BETTER LUCK NEXT TIME!!!")
        print('-'*5,"game terminated",'-'*5)
        break
    x=input("guess the five letter word \n")
    if is_word_in_dictionary(x,"5ad13507","f38ea2962ab8410188d8fb270b174eff")==True and len(x)==5:
        if x==word1:
            print("your guess is correct !!!!")
            print("-"*5,"WOHOOO!!!","-"*5)
            print('-'*5,"game terminated",'-'*5)
            break
        else :
            s1,s2='',''
            for i in x :
                if word1[x.index(i)]==i:
                    s1+=i
                elif i in word1:
                    if i not in s2:
                        s2+=i
                else:
                    s1+='-'
            print("the actual word is of the format \n",s1)
            print("other characters present except displyed:",s2)
            print('*'*40)
    else:
        print("MESSAGE : enter a valid english word of appropriate lenght")
        print('-'*5,"game continues",'-'*5)
        



    
