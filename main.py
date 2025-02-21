def avoiding_duplicates(list_of_words: list) -> list:
    new_list=[]
    for word in list_of_words:
          if word not in new_list:
                new_list.append(word)
    return new_list

def words_list() -> list:
    list_of_words=[]
    word=input("Enter a word (or a blank line to quit): ")
    while word!="":
            list_of_words.append(word)
            word=input("Enter a word (or a blank line to quit): ")
    return list_of_words

def main():
    list_of_words=words_list()
    list_without_duplicates=avoiding_duplicates(list_of_words)

    print(f"Original list: {list_of_words}\nList without duplicates: {list_without_duplicates}")

if __name__=="__main__":
    main()