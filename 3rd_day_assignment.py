# -*- coding: utf-8 -*-
"""3rd Day Assignment

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qV6YJvHIaOju_ffKMwKNwT-e5KKYeUtP
"""

def remove_vowels(string):
  vowels = "aeiouAEIOU"
  new_string = ""
  for char in string:
    if char not in vowels:
      new_string += char
  return new_string

def main():
  string = "String with vowels"
  print(remove_vowels(string))

if __name__ == "__main__":
  main()