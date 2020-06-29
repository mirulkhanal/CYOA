import os


def start():
    start_text = '''
                    Welcome to PRANKING DAD, A Choose your own adventure.
    '''
    print(start_text)
    return starter_func()


def starter_func():
    name = input("Enter Your Full Name: ")
    age = input("Enter Your Age: ")
    first_name, last_name = name.split(" ")
    return part_one(first_name, last_name, age)


def part_one(fname, lname, age):
    os.system('cls')
    start_text = '''    -------------------------------------------------------------------------------------
                                    Dad's Sorrow
    -------------------------------------------------------------------------------------'''
    print(start_text)
    story = '''
    I am extremely scared of my dad, I like to think he is a decent person but whenever he
    gets mad,he goes crazy. He never understands how much it affects us. Give him a bottle
    of whisky and he will weaponize that shit like a nuclear missile and give us a decent
    beating. I remember that day as it was yesterday although some memories are vague.

    I heard him beating my mom, I reckon she might've done something to make him mad. It's
    not right to get him mad. She should've held back whatever it was.

    I thought to myself I might have to help mom now or he might actually kill her. So I
    decided to .....

    1) Scream at dad, "Hey Leave her the fuck alone"
    2) Sit there and watch, because I was a pussy and as dad often said, I wouldn't ever amount
       to anything.
    '''
    print(story)
    choice = int(input("Choice: "))
    if choice == 1:
        return dad_action(fname, lname, age)
    elif choice == 2:
        return do_nothing()
    else:
        print('Invalid Code')


def dad_action(fname, lname, age):
    os.system('cls')

    start_text = '''    -------------------------------------------------------------------------------------
                            Hey Dad! Leave her the fuck alone. Or else...
    -------------------------------------------------------------------------------------'''
    print(start_text)
    story = '''
    "Or what? you little shit?"
    oh fuck!!! Dad is more mad now, he stopped hitting mom and rolled the belt around his
    palm. He looks terrifying. I shouldn't speak now.
    "I will show you what talking up to me gets you sonny"

    He beat me with an inch of my life, it was messy. My mum took me to a nearby hospital
    where they treated me. My father had told them I had fallen down the fourth floor of
    our apartment while playing. They obviously had no reason not to believe him, and the
    tears, he could get an oscars for those tears.

    I had been there for about 28 hours when I finally regained conciousness. I felt like
    I had died and come to heaven, then I saw my dad sitting there by my side. I could see
    it in his eyes that he was sorry this time, he had gone too far, and most of all he
    suspects that the doctors have notified the authorities and he might've to answer them.

    "I am so sorry baby, I was so drunk and lost control, I never meant to hurt you son."

    I could say nothing but umms and uhhhs like he was talking rocket science.

    "Baby, they want to take you away from me, they wanna ask some questions about this
    incident and I told them that you fell off of the fourth floor while playing. Do this
    one thing for daddy will you?"

    "Ok dad" I said with a lot of hesitation in my tone.

    ***Police are here to take my report***

    '''
    print(story)
    print(f'\nOfficer: "So {fname} was it?"')

    print('\nMe: "Yes"')

    print('\nOfficer: "For the record, could you please state your full name?"')

    print(f'\nMe: "Yes officer! I am {fname} {lname}"')

    print(f'\nOfficer: "How old are you again?"')

    print(f'\nMe: "I am 4 days away from being {age} "')

    print('''
          "Wow, you're a grownup already.
          If you dont mind me asking, how did you hurt yourself?"
          
          1. I Told him everything about how when dad gets drunk he likes to hit mom and me
          2. I Lied because I knew dad loves us even though he makes mistakes sometime
          ''')
    choice = int(input('Choice: '))
    if choice == 1:
        return dad_action(fname, lname, age)
    elif choice == 2:
        return do_nothing()
    else:
        print('Invalid Code')


def do_nothing():
    pass


start()
