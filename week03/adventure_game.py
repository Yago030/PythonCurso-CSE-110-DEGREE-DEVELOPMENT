"""
Author: Santiago Bergerat  S
Purpose: W03 Adventure game 
}
This program was tested by two friends who played through the different scenarios. 
Their feedback helped me refine the prompts and improve the narrative.
"""




print(f"{'WELCOME TO ADVENTURE GAME':^50}")
print('-' * 50, '\n')

print(f"{'Story: My First Exploration Tour':^50}\n")
print(f"It's the weekend, and you decide to go on a vacation surrounded by forests. "
      f"As a city person, you've never visited a forest before. "
      f"You have two options for starting this adventure:\n")

while True:
    print("You must choose between TOUR or ALONE.")
    choice = input("What is your choice? ").lower()
    if choice in ["tour", "alone"]:
        break
    print("Invalid choice. Please select one of the provided options.\n")

if choice == "tour":
    print(f'\nYou decide to join a guided tour. '
          f'You pack your backpack with everything necessary based on the recommendations: flashlight, lighter, canned food, warm clothes, ropes, among other items. '
          f'You arrive at the meeting point and meet the group.\n')

    print(f'The first activity is a climb up a narrow mountain trail. '
          f'The guide recommends using ropes to tie everyone together for safety, although it’s not mandatory.\n')

    while True:
        print("You must choose between TIE or DON'T TIE.")
        choice = input("What is your choice? ").lower()
        if choice in ["tie", "don't tie"]:
            break
        print("Invalid choice. Please select one of the provided options.\n")

    if choice == "tie":
        print(f'You choose safety and tie yourself to the rest of the group. '
              f'During the climb, your legs weaken and you fall, but the rope keeps you safe. '
              f'With the support of your companions, you recover your energy and reach the top of the mountain. '
              f'There, you camp and share stories by the campfire.\n')

        while True:
            print("You must choose between SODA or COOKIES.")
            choice = input("What is your choice? ").lower()
            if choice in ["soda", "cookies"]:
                break
            print("Invalid choice. Please select one of the provided options.\n")

        if choice == "soda":
            print(f'You share it with your companions, creating new bonds and friends for future adventures.')
        else:
            print(f'You share the cookies while listening to stories and planning new excursions.')

    else: 
        print(f'\nYou trust your instincts and decide not to use the rope. '
              f'After 40 minutes of walking, your legs weaken and you fall, rolling down the slope. '
              f'Luckily, a companion catches you before you fall into the void. '
              f'They treat your wounds, and this time, you are tied to the group. Despite the pain, you reach the top. '
              f'There, the group camps and lights a campfire.\n')

        while True:
            print("You must choose between CHICKEN or PICKLED MEAT.")
            choice = input("What is your choice? ").lower()
            if choice in ["chicken", "pickled meat"]:
                break
            print("Invalid choice. Please select one of the provided options.\n")

        if choice == "chicken":
            print(f'You eat near the campfire while contemplating the moon. You reflect on your experience and enjoy the moment.')
        else:
            print(f'You reflect on what could have happened if your companion hadn’t saved you. '
                  f'You learn the importance of being better prepared in the future.')

elif choice == "alone":
    print(f'\nYou choose to go alone. '
          f'You go to a nearby store and buy chips, soda, and some snacks. '
          f'You reach the foot of a mountain, park your car, and venture into the forest while enjoying your chips.\n')

    print(f'After a few hours of walking, you realize you’re lost. '
          f'The forest begins to darken, and you don’t recognize the trail.\n')

    while True:
        print("You must choose between BACKTRACK or BACKPACK.")
        choice = input("What is your choice? ").lower()
        if choice in ["backtrack", "backpack"]:
            break
        print("Invalid choice. Please select one of the provided options.\n")

    if choice == "backtrack":
        print(f'You decide to backtrack and start walking quickly in a desperate attempt to find your way back. '
              f'In the dark, you trip and fall, severely injuring your leg. The pain is intense, and it’s hard to move.\n')

        while True:
            print("You must choose between WAIT or USE BRANCHES.")
            choice = input("What is your choice? ").lower()
            if choice in ["wait", "use branches"]:
                break
            print("Invalid choice. Please select one of the provided options.\n")

        if choice == "wait":
            print(f'You spend the night cold and scared by the sounds of animals. The next day, a search team finds you. '
                  f'Although you’re safe, the fear and experience deeply mark you. '
                  f'You promise never to venture into nature without company and preparation.')
        else:
            print(f'With determination, you use branches as crutches and walk for hours until you find a road. '
                  f'There, someone helps you. You reflect on the importance of preparation and promise never to explore again without being well-equipped.')

    else: 
        print(f'You check your backpack and find a map. You use it to orient yourself and find a trail that leads to an abandoned cabin. '
              f'You decide to spend the night there. While eating your provisions, you enjoy the tranquility and plan to explore with more preparation in the future.')
