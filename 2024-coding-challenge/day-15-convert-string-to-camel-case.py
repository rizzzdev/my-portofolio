'''

https://www.codewars.com/kata/517abf86da9663f1d2000003

DESCRIPTION:
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"

'''

# Solution
def to_camel_case(text):
    dash_underscore_remover = ''.join([i if i not in ['-', '_'] else ' ' for i in text ])
    splitter = dash_underscore_remover.split(' ')
    return ''.join([i.title() if splitter.index(i) > 0 else i for i in splitter ])

# Testing
print(to_camel_case("the_stealth-warrior"))