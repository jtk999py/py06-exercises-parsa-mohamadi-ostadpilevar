# tamrin haye adv3
'''3--> yek listi darim be in nam , tedade afradi k esmeshon ba a shoro mishe ro bedast bairid --> for
my_users=['ali','vahid','hamid',...]'''

my_users = ['mana','parsa','amir','arsalan','adele','ana','arron']
tedad = 0
for i in my_users:
    if i[0]=='a' or i[0]=='A':
        tedad=tedad+1
        
print(tedad)