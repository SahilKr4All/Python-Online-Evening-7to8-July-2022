from nltk.corpus import stopwords
data1 = '''Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.'''
data2 = '''Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[31]
Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[32][33]
Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[34] Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.[35]'''

#Step1 :Tokenization
data1 = data1.split()
data2 = data2.split()

#remove the stopwords
sw=stopwords.words('english')


for word in sw:
    for i in data1:
        if word == i:
            data1.remove(word)

    for j in data2:
        if word == j:
            data2.remove(word)
#change to set
data1 = set(data1)
data2 = set(data2)
#Find the simmilarity
common=data1.intersection(data2)
total =data1.union(data2)
perc  = (len(common)/len(total))*100
print(f"Simmilarity = {perc}%")
