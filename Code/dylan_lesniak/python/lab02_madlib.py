#variables
adj = []
adv = []
noun = []
verb = []
#working code
# def madden():



def get_adjs():
    adj = []
    while len(adj) != 4:
        print("To start, please enter 4 adjectives, separated by a comma and a space.")
        adjs = input("> ")
        adj = adjs.split(", ")
    return adj

def get_advs():
    adv = []
    while len(adv) != 2:
        print("Please enter 2 adverbs, separated by a comma and a space.")
        advs = input("> ")
        adv = advs.split(", ")
    return adv

def get_nouns():
    noun = []
    while len(noun) != 3:
        print("Please enter 3 nouns, separated by a comma and a space.")
        nouns = input("> ")
        noun = nouns.split(", ")
    return noun


def get_verbs():
    verb = []
    while len(verb) != 3:
        print("Please enter a past tense verb, a present tense one, and a past tense on separated by a comma and a space.")
        verbs = input("> ")
        verb = verbs.split(", ")
    return verb

def start():
    print("Hello! Welcome to the Magically Monotonous Mad Lib!")
    print()
    adj = get_adjs()
    adv = get_advs()
    noun = get_nouns()
    verb = get_verbs()
    print ( f'''Today I went to the zoo. I saw a(n)
{adj[0]}(adjective)
{noun[0]}(Noun) jumping up and down in its tree.
He {verb[0]}(verb, past tense) {adv[0]}(adverb)
through the large tunnel that led to its {adj[1]}(adjective)
{noun[1]}(noun). I got some peanuts and passed
them through the cage to a gigantic gray {noun[2]}(noun)
towering above my head. Feeding that animal made
me hungry. I went to get a {adj[2]}(adjective) scoop
of ice cream. It filled my stomach. Afterwards I had to
{verb[1]}(verb) {adv[1]} (adverb) to catch our bus.
When I got home I {verb[2]}(verb, past tense) my
mom for a {adj[3]}(adjective) day at the zoo. ''')

start()