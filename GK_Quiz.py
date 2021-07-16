score = 0

start = input('Are you ready to play(yes/no): ')
if start.lower() == 'yes':
    print(' _______')
    print('|       |')
    print('|       |')
    print('|_______|')
    print('Welcome to the GK Quiz!')
    one = input("1.Which is the capital of Australia: ")
    if one.lower() == 'sydney':
        print("correct!")
        score += 1
    else:
        print('Incorrect!')
        print("The correct answer is Sydney")
    two = input("2.Who invented Playing cube: ")
    if two.lower() == 'erno rubik':
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("The correct answer is Erno Rubik")
    three = input("3.Which is called  'The Oxford of SouthIndia': ")
    if three.lower() == 'tirunelveli':
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("The correct answer is Tirunelveli")
    four = input("4.How many colours are in a Rainbow: ")
    if four.lower() == '7':
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("The correct answer is Seven")
    five = input("5.Who is the author of Thirukkural: ")
    if five.lower() == 'thiruvalluvar':
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("The correct answer is Thiruvalluvar")
    six = input("6.Who is the first Prime Minister of India: ")
    if six.lower() == 'jawaharlal nehru':
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("The correct answer is Jawaharlal Nehru")
    seven = input("7.Who is called  'Iron man of India': ")
    if seven.lower() == 'sardar vallabhai patel':
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("The correct answer is Sardar Vallabhai Patel")
    eight = input("8.Who is called  'Missile man of India': ")
    if eight.lower() == 'a.p.j.abdul kalam':
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("The correct answer is A.P.J.Abdul Kalam")
    nine = input("9.Which city is called 'Pink city of India': ")
    if nine.lower() == 'jaipur':
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("The correct answer is Jaipur")
    ten = input("10.Which is the Temple city of South India: ")
    if ten.lower() == 'kumbakonam':
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print('The correct answer is Kumbakonam ')
    print('Your mark is '+ str(score) +' out of 10')  
    print('      ___               || ')
    print('     | __} |  /  ____   ||       ')
    print('     |___}  |/  | ___]  ||       ')
    print('           _/   {_____  --       ')
    print("See you later in another Quiz")
if start.lower() == 'no':
    print('Get ready for the Quiz soon!,See you later!')
else:
    print("You have typed wrong!")
