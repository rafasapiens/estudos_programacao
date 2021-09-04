# coding: utf-8


# Todas as perguntas são referentes ao arquivo `data.csv`

# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.

import csv


global data


with open("data.csv") as fobj:

    reader = csv.DictReader(fobj)

    data = [r for r in reader]


# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?

# 

def q_1():

    global data


    nationalities = []

    for i in data:

        nationalities.append(i["nationality"])

    return int(len(set(nationalities)))


    pass


# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?

def q_2():

    global data


    clubs = []

    for i in data:

        clubs.append(i["club"])

    return int(len(set(clubs)))


    pass


# **Q3.** Liste o nome completo dos 20 primeiros jogadores de acordo com a coluna `full_name`.

def q_3():

    global data


    names = []

    try:

        for i in range(20):

            names.append(data[i]["full_name"])

    except IndexError:

        for i in data:

            names.append(i["full_name"])


    return names


    pass


# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?

def q_4():

    global data


    money = []

    for i in data:

        money.append(i["eur_wage"])

    money.sort(reverse=True)

    del money[10:]


    rich = []

    count = 0

    

    for j in money:

        for i in data:

            if i["eur_wage"] is j:

                rich.append(i["full_name"])

                count+=1

    return rich


    pass


# **Q5.** Quem são os 10 jogadores mais velhos?

def q_5():

    global data


    age = []

    for i in data:

        age.append(i["age"])

    age.sort(reverse=True)

    del age[10:]


    old = []

    count = 0

    

    for j in age:

        for i in data:

            if i["age"] is j:

                old.append(i["full_name"])

                count+=1

    return old


    pass


# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.

def q_6():

    global data


    diff_ages = {}

    for i in data:

        if i["age"] in diff_ages.keys():

            diff_ages[i["age"]] += 1

        else:

            diff_ages[i["age"]] = 1


    return diff_ages


    pass