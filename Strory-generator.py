import random
when =[ 'Awhile ago', 'Yesterday','Last nighht', 'Two weeks back','On 3rd March']
who = ['a hen','Mr paul', 'a cat','a croccodile','a mad man']
name = ['Ali','Mirim', 'Martin','lius', 'Agnes']
residence = ['Kampala','Kyaliwagala','Mbale','Kabojja','Gulu']
went = ['Club','Museum','School','Hospital','Cinema']
happened = ['made alot of friends', 'fell in love','found a lost friend','danced all night','got treated']
print(random.choice(when)+', '+random.choice(who)+'that lived in '+ random.choice(residence) + ',went to the '+ random.choice(went)+' and '+ random.choice(happened))