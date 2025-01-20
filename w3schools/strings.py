if __name__ == "__main__":
    print("Hello")
    
    ### Quotes inside quotes
    print("I'm selling bridges! You should buy... all of them.")
    print("You cannot find 'better' bridges anywhere!")
    print('Nor can ya find "better" bridges anywhere!')

    ### string variables
    greeting = "Hello"
    print(greeting)
    long_greeting = """To whom it may concern,
with all that it may concern,
and all concerning which could be with concern:"""
    print(long_greeting)
    another_long_greeting = '''With
    all
    but
    the
    best,'''
    print(another_long_greeting)

    ### Strings are arrays
    hello = "Have a silly story!"
    print(hello[0], hello[3], hello[9], hello[10], hello[15])
    # there is no character data type; just strings of length 1

    ### Looping through a string
    for letter in "String":
        print(letter)
    
    ### String length
    print(len("string"))

    ### Check string
    text = "According to all known laws of aviation..."
    if "cord" in text:
        print("Wires")
    if "bees" not in text:
        print("Wrong movie?")

    ### Slicing
    fruit = "pineapple"
    print(fruit[4:7])
    print(fruit[:4])
    print(fruit[4:])
    print(fruit[-5:-2])
    if fruit[-5:] == "apple":
        print(fruit, "is definitely a type of apple")
    
    ### Upper case
    upper = "upper"
    print(upper.upper())

    ### Lower case
    lower = "LOWER"
    print(lower.lower())

    ### Remove whitespace
    tabs = "    Tabulation    "
    print(tabs.strip()) # removes leading and trailing whitespace

    ### Replace string
    formal_email_signoff = "Love, Bailey"
    print(formal_email_signoff.replace("Love", "Sincerely"))

    ### Split string
    words = "How many words are in this string? Or rather, how many tokens?"
    tokens = words.split(" ")
    print(tokens)
    print(len(tokens))

    ### String concatenation
    s1 = "String"
    s2 = "Concatenation"
    s3 = s1 + s2
    s4 = s1 + " " + s2
    print(s3)
    print(s4)

    ### F-Strings
    insert = "nonsense"
    fstring = f"I'm just gonna talk about some {insert}"
    print(fstring)
    
    price = 4.994
    fstringfloat = f"And all it's gonna cost you is ${price:.2f}!"
    print(fstringfloat)
    
    bulk_price = 17.666
    fstringbulk = f"Or you can order 5 {insert}'s for the low low special of ${bulk_price:.2f}!"
    print(fstringbulk)

    fstringdiscount = f"And if you order right now, you'll get your first {insert} 90% off for a total of {price*0.1:.2f}!"
    print(fstringdiscount)

    # Escape character
    air_quotes = "Ah, yes, the \"package\" included in the \"module\". Of course!"
    print(air_quotes)

    illegals = """Here are some things you cannot print in Python:
\tQuotes: \' \"
\tBackslashes: \\\\
\tNew Line: \n\\n This is on a separate line.
\tCarriage Return: \r\\r Hi!
\tTab: \t\\t
\tBackspace: \b\\b
\tForm Feed: \f\\f This is technically the \"Next Page\"
\tOctal Value: \003 \\ooo
\tHex value: \x03 \\xhh"""
    print(illegals)

    ### String methods

    ## capitalize()
    print("the capital".capitalize())

    ## casefold()
    compare_this = "The character: ß"
    print(f"How does Python handle {compare_this} with .lower() and .casefold()?")
    print(f".lower() produces: {compare_this.lower()}")
    print(f".casefold() produces: {compare_this.casefold()}")
    print(f".lower() == .casefold() produces: {compare_this.lower() == compare_this.casefold}")
    print(".lower() should be used for simple display")    
    print(".casefold() should be used for strong caseless comparison")

    ## center()
    print("A string centered with in a space of length 75 with character '-'.".center(75, "-"))
    print("A string centered with in a space of length 100 with character '='.".center(100, "="))

    ## count()
    likeness = "So like I like when to like the store, y'know? And like there were like so many like shoppers there it was CRAZY."
    print(f"Counting 'likes' in: \"{likeness}\"")
    print("likes:", likeness.count("like"))

    ## encode()
    for_elise = "Beethoven? You mean the guy who wrote Für Elise?"
    print(for_elise.encode(encoding="ascii",errors="namereplace"))

    ## endswith()
    statement = "This is a question, I'm sure."
    question = "Well, is this a valid question?"
    loud_question = "How about this!?"
    question_loud = "Even this?!"
    questions = (statement, question, loud_question, question_loud)
    for q in questions:
        print(f"Evaluating whether following is question: {q}")
        print(q.endswith(("?","!?","?!")))

    ## expandtabs()
    balloon = "b\ta\tl\tl\to\to\tn"
    print("I am now going to inflate this {balloon}")
    inflation_level = 5
    for n in range(inflation_level):
        if n**2 != 8:
            print(balloon.expandtabs(n**2))
        else:
            print(balloon.expandtabs())
    print("Pop!".center(97,"*"))

    ## find()
    search_space = "There is a word hidden inside of this string."
    valuable = "ring"
    print(f"A {valuable} has been stolen. Where is it? ({search_space})")
    for n in (0, 1, 5):
        print(search_space.find(valuable, n, len(search_space) - n))

    
    ## strip()
    for q in questions:
        print(f"Evaluating whether following ends with 'this' or 'question': {q}")
        print(q.strip("!?.").casefold().endswith(("this", "question")))
