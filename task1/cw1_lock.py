#!/usr/bin/env python3
key=str(input("Wprowadz szyfr: "))
check=str(input("Wprowadz szyfr ponownie: "))

if key==check:
    print("Oba szyfry sa zgodne!")
    input()
else:
    print("Podna szyfry sa rozne!")
    input()
