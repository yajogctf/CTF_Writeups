# shattered-memories - 0 pts

Difficulty :  :star:  

## Statement

> I swear I knew what the flag was but I can't seem to remember it anymore... can you dig it out from my inner psyche?  

> Dowloads : [fichier](./shattered-memories)  

**Hint** : The flag for this challenge is of the form `lactf[TEXTE_HERE]`.

![Copie d'écran](./shattered-memories.png)  

## Discovery - Analysis
We have a file to analyze. We'll probably have to use reverse-engering tools to find the flag.  

## Soluce
To start with, I'm using the free version of `IDA` (not the pro version).  

Using `IDA`, I open the `shattered-memories` file and start browsing it to see what functions it offers:  

![Liste des fonctions](./IDA_fonctions.png)  

I'll take a closer look at the `main` function and take a look at the rest:  

![Fonction Main1](./IDA_fonctionMain1.png)  

![Fonction Main1](./IDA_fonctionMain2.png)  

![Fonction Main1](./IDA_fonctionMain3.png)  

My gaze lingers on a section containing the characters `lactf{no` :  

![Début du flag](./IDA_lactfno.png)  

All that remains is to look above and below to retrieve the pieces of the flag found: `t_what_f`; `t_means}`; `nd_forge`; `lactf{no`; `orgive_a`.  

All that remains is to put everything back in order to obtain the flag: `lactf{not_what_forgive_and_forget_means}`.
