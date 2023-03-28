print("Hi")
print("Enter a sentence to get how many word did you use")

sentence = input("Enter the sentence or article : ")

number_of_words = len(sentence.split())

print("This sentence/article has ",number_of_words," words.")