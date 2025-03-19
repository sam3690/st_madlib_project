

def madlib ():
      n1 = input("Enter First noun: ")
      adj1 = input("Enter an adjective: ")
      v1 = input("Enter a verb: ")
      av1 = input("Enter an adverb: ")
      n2 = input("Enter the 2nd noun: ")
      adj2 = input("Enter an adjective: ")

      if n1 and n2 and v1 and av1 and adj1 and adj2:
        story = f"""Once upon a time, there was a {adj1} {n1} who loved to {v1} {av1}.
            One day, while {v1}ing, they found a {adj2} {n2}!
            It was the most extraordinary day of their life."""
        print("Your madlib story")
        print(story)
      else:
          print("Please fill all the blanks")
          

madlib()