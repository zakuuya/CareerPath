
import random

def greetings():
  print("Hi, I am Emaje -- your career guide. \n\nI offer insight into selecting a career path, and the skills needed to reach your goal. \nPlease understand that I can only offer guidance into careers that I have personally researched.\n\nPLEASE READ:\nTo return to previous question, type 'back' ")

#Different path types

user_type = ['highschool', 'college', 'postdoc','professional']

#The lists

science_list = ['environmental', 'hydrology', 'physics', 'electrochemistry',]
sci_skills_list = ['remote_sensing', 'gis',]
sci_cert_list = ['gis', 'leed', 'osha', 'optics', 'accelerator_physics', 'faa_part_107']

engineering_list = ['uas', 'mechanical',]
eng_skills_list = ['autocad', 'nx_siemens', 'fmea_analysis', 'repairing', 'rebuilding',]
eng_cert_list = ['nx_siemens', 'private_pilot', 'faa_part_107',]

#Personality
affirmation = ['Good idea', 'Smart', 'Interesting', 'OK cool', 'Sweet']
random_aff = random.choice(affirmation)

#Highschool science
#Some programs, projects, skills, or internships may be interchangeable
#Try not to overcreate functions, design for reuse if possible
def hs_env():
  print("\nEncouraging words for hs students. As a highschool student, there are many programs to participate in, projects to work on and skills to learn.\nHere are some programs that you can get into now.\nHere are some projects to work on.\nThese are the skills you can learn.\nGlobal comparison notes: EU students can become 'dr's' at age 24. Some colleges in the EU are free such as:")
def hs_phys():
  print("Here are some programs that you can get into now. These are the skills you need.")
def hs_hydro():
  print("Here are some programs that you can get into now. These are the skills you need.")
def hs_electrochem():
  print("Here are some programs that you can get into now. These are the skills you need.")
#college science
def uni_env_programs():
  print("Program 1:\nProgram 2:\n\n")
def uni_env_projects():
  print("Project 1:\nProject 2:\n\n")
def uni_env_skills():
  print("Skill 1:\nSkill 2:\n\n")
def uni_env_internships():
  print("Internship 1:\nInternship 2:\n\n")
def uni_env():
  print("\nEncouraging words for uni students. Here are some programs that you can get into now.\nHere are some projects to work on:\nThese are the skills you need:\nThese are the internships available to you:")
  ask_more = str(input("Would you like to learn more? Y or N\n"))
  if ask_more == "Y":
    more_uni_env = input("What would you like to learn more about? 'programs', 'projects', 'skills', or 'internships'?\n")
    if more_uni_env == "programs":
      uni_env_programs()
      print("OK, let's take a step back")
      uni_env()
    elif more_uni_env == "projects":
      uni_env_projects()
      print("OK, let's take a step back")
      uni_env()
    elif more_uni_env == "skills":
      uni_env_skills()
      print("OK, let's take a step back")
      uni_env()
    elif more_uni_env == "internships":
      uni_env_internships()
      print("OK, let's take a step back")
      uni_env()
    else:
      uni_env()
  else:
    environmental()
def uni_phys():
  print("Here are some programs that you can get into now. These are the skills you need.")
def uni_hydro():
  print("Here are some programs that you can get into now. These are the skills you need.")
def uni_electrochem():
  print("Here are some programs that you can get into now. These are the skills you need.")
#postdoc science
def pd_env():
  print("Here are some programs that you can get into now. These are the skills you need.")
def pd_phys():
  print("Here are some programs that you can get into now. These are the skills you need.")
def pd_hydro():
  print("Here are some programs that you can get into now. These are the skills you need.")
def pd_electrochem():
  print("Here are some programs that you can get into now. These are the skills you need.")
#professional science
def pro_env():
  print("Here are some programs that you can get into now. These are the skills you need.")
def pro_phys():
  print("Here are some programs that you can get into now. These are the skills you need.")
def pro_hydro():
  print("Here are some programs that you can get into now. These are the skills you need.")
def pro_electrochem():
  print("Here are some programs that you can get into now. These are the skills you need.")


#Science paths
def science_choice():
  science_type = str(input(f"What type of science are you interested in? {science_list}\n\n")).lower()
  if science_type == "back":
    main_menu()
  elif science_type == "environmental":
    environmental()
  elif science_type == "hydrology":
    hydrology()
  elif science_type == "physics":
    physics()
  elif science_type == "electrochemistry":
    electrochemistry()
  else:
    print("Sorry. I do not understand your response.\n\n")
    science_choice()

def environmental():
    #Insert background info.
    #Ask if user wants to learn more?
    #If user says no, return to main menu
    print(f"{random_aff}. We need people like you\n\n")
    print("About Environmental Science:(what they do, work-life balance)\nJob Roles + Salary + Duties:\nSalary Survey:\nCareer Growth and Outlook:\nCareer Paths:(environmental planner I > Environmental Planner IV > Project Manager\nQualifications:\nJob Sites:\nCompanies to work for:")
    ask_more = input("Would you like to learn more? Y or N\n")
    if ask_more == "Y":
      user_type_input = str(input(f"What is your professional status?\n\nType{user_type}\n\n")).lower()
      if user_type_input == "highschool":
        hs_env()
      elif user_type_input == "college":
        uni_env()
      elif user_type_input == "postdoc":
        pd_env()
      elif user_type_input == "professional":
        pro_env()
      elif user_type_input == "N" or user_type_input == "back":
        environmental()
      else:
        print("Sorry, I do no understand that answer.\n")
        environmental()
    elif ask_more == "N" or ask_more == "back":
      science_choice()
    else:
      print("Sorry. I do not understand your response. Please type Y or N\n\n")
      environmental()

def hydrology():
    #Insert background info.
    #Ask if user wants to learn more?
    #If user says no, return to main menu
    print(f"{random_aff}. We need people like you\n")
    ask_more = input("Would you like to learn more? Y or N\n")
    if ask_more == "Y":
      user_type_input = str(input(f"What is your professional status?\n\nType{user_type}")).lower()
    elif ask_more == "N" or ask_more == "back":
      science_choice()
    else:
      print("Sorry. I do not understand your response. Please type Y or N\n\n")
      hydrology()

def physics():
    #Insert background info.
    #Ask if user wants to learn more?
    #If user says no, return to main menu
    print(f"{random_aff}. We need people like you\n")
    ask_more = input("Would you like to learn more? Y or N\n")
    if ask_more == "Y":
      user_type_input = str(input(f"What is your professional status?\n\nType{user_type}"))
    elif ask_more == "N" or ask_more == "back":
      science_choice()
    else:
      print("Sorry. I do not understand your response. Please type Y or N\n\n")
      physics()

def electrochemistry():
    #Insert background info.
    #Ask if user wants to learn more?
    #If user says no, return to main menu
    print(f"{random_aff}. We need people like you\n")
    ask_more = input("Would you like to learn more? Y or N\n")
    if ask_more == "Y":
      user_type_input = str(input(f"What is your professional status?\n\nType{user_type}"))
    elif ask_more == "N" or ask_more == "back":
      science_choice()
    else:
      print("Sorry. I do not understand your response. Please type Y or N\n\n")
      electrochemistry()

#Highschool engineering
def hs_engineering():
  print("As a highschool student, there are many programs to participate in, projects to work on and skills to learn. Here are some programs that you can get into now. Here are some projects to work on. These are the skills you can learn.")
#college engineering
def uni_engineering():
  print("As a university student, there are many programs to participate in, projects to work on and skills to learn. Here are some programs that you can get into now. Here are some projects to work on. These are the skills you can learn.")
#postdoc engineering
def pd_engineering():
  print("As a postdoc, there are many programs to participate in, projects to work on and skills to learn. Here are some programs that you can get into now. Here are some projects to work on. These are the skills you can learn.")
#professional engineering
def pro_engineering():
  print("As a professional, there are many programs to participate in, projects to work on and skills to learn. Here are some programs that you can get into now. Here are some projects to work on. These are the skills you can learn.")


#Engineering Paths
def engineering_choice():
  eng_type = str(input(f"What type of engineering are you interested in? {engineering_list}\n\n"))
  if eng_type == "back":
    main_menu()
  elif eng_type == "uas":
    uas()
  elif eng_type == "mechanical":
    mechanical()
  else:
    print("Sorry. I do not understand your response.\n\n")
    engineering_choice()

def uas():
    #Insert background info.
    #Ask if user wants to learn more?
    #If user says no, return to main menu
    print(f"{random_aff}. Your future is bright\n")
    ask_more = input("Would you like to learn more? Y or N\n")
    if ask_more == "Y":
      user_type_input = str(input(f"What is your professional status?\n\nType{user_type}"))
    elif ask_more == "N" or ask_more == "back":
      engineering_choice()
    else:
      print("Sorry. I do not understand your response. Please type Y or N\n\n")
      uas()

def mechanical():
    #Insert background info.
    #Ask if user wants to learn more?
    #If user says no, return to main menu
    print(f"{random_aff}. We need people like you\n")
    ask_more = input("Would you like to learn more? Y or N\n")
    if ask_more == "Y":
      user_type_input = str(input(f"What is your professional status?\n\nType{user_type}"))
    elif ask_more == "N" or ask_more == "back":
      engineering_choice()
    else:
      print("Sorry. I do not understand your response. Please type Y or N\n\n")
      mechanical()

#Main menu
def main_menu():
  if user_type_ask == "Y":
      choice = str(input("What career path do you want to pursue? Type Science or Engineering\n")).lower()

      if choice == "science":
        science_choice()
        end_1st_path = True

      elif choice == "engineering":
        engineering_choice()
        end_1st_path = True
        
      else:
         print("Please type 'science' or 'engineering'\n")

  elif user_type_ask == "N":
      print("Sorry, this generator has not yet been updated for global guidance. Check back again later for an update.\n")

  else:
      print("Error. Please type 'Y' or 'N' to continue.\n")


#Code starts running here
greetings()


end_1st_path = False

while not end_1st_path:
  user_type_ask = str(input("Are you currently living in the United States? Type 'Y' for yes or 'N' for no.\n\n"))
  main_menu()


print("You have reached the end")


#Ask to learn more about the eng_skills_list
#Ask to learn more about programs
#Ask to learn more about internships
#Ask to learn more about benefits
#Include project examples
#Add salary data
#Add REAL required job qualifications such as yearly experience, status, credentials
#Add job sites and job boards
#Add encouraging text that prove anyone can learn anything
#If user inputs wrong answer, then return a sorry, then ask same question
#Give user an option to go back for every question
#Show user their career path through tree model-like ascII career_type
#Give user option to type a shortcut to a position in career path utilizing a search bar
#Optimize to gather data: figure out how to record input data in a structured way for future data analysis
