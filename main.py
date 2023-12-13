import numerology
import bot
import openai

openai.api_key = "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"


#name = input("your name \n")
#year = int(input("your birth year \n"))
#month = int(input("your birth month \n"))
#day = int(input("just your birth day \n"))
#year_looking = int(input("what year are you looking for \n"))


def main(day, month, year, name, year_looking):

    x = numerology.lifepath(day, month, year)
    y = numerology.personal_number(day)
    z = numerology.namevalue(name)
    w = numerology.cnc(x, year_looking)

    a = numerology.personal_number_results(day)
    b = numerology.lifepath_results(day, month, year)
    c = numerology.namevalue_results(name)

    d = numerology.cnc_results(w)

    prompt1 = f"""I want to write an article about someone. 
    Follow the outline below

    - Introduction ourselves shortly and thank  them for using our service ( we are davinX team. We develop this web application that can forecast someone's future on top of research data) 

    - in this part describe the details of the person who is predicting the future. In this section, we will provide you with 3 list 

    List 1 = This list contains the person's Skills: This number indicates your natural abilities and talents that you can use to achieve your goals and fulfill your destiny.
    Likes and dislikes: This number shows your preferences and tastes in various aspects of life, such as hobbies, interests, colors, foods, etc.
    Best fitting careers: This number suggests the types of professions or occupations that suit your personality and potential the most.
    Challenges: This number reveals the obstacles and difficulties that you may face in your life and how to overcome them.

    List 2 = This list contains the person's Lucky numbers: These are the numbers that resonate with your life path and bring you positive energy, opportunities, and success.
    Born talents: These are the innate gifts and qualities that you possess and that make you unique and special.
    Fortune and misfortune: These are the events and situations that affect your life positively or negatively, depending on your choices and actions.
    Purpose: This is the ultimate goal or mission of your life that you are meant to accomplish and that gives you fulfillment and happiness.
    Lessons: These are the experiences and learnings that you gain from your life journey and that help you grow and evolve.
    career: the best career presented by nature 

    List 3 = This list contains the person's How they interact with society: This number reflects your social skills and behavior, how you communicate and relate to others, and how you influence and are influenced by the world around you.
    About their friends: This number shows the kind of people that you attract and are attracted to, who support you who challenge you, and who are compatible and incompatible with you.
    Opportunities and open doors: These are the chances and possibilities that you encounter in your life that can help you achieve your goals and dreams.
    Hidden potential: This is the part of yourself that you may not be aware of or that you may not express fully, but that can enhance your abilities and talents.
    Karmic lessons and challenges: These are the issues and problems that you have to face and resolve in your life, that are related to your past lives or actions, and that can affect your present and future.

    Writer a full description. About this man describe his Likes and dislikes, Best fitting careers, Challenges, Lucky numbers, Born talents, Fortune and misfortune, Purpose, Lessons, career, How they interact with society, About their friends, Opportunities and open doors, Hidden potential, Karmic lessons and challenges  according to the list I have provided below
    """

    prompt2 = f"""each of these lists contains a variety of aspects of that person's life. That description of this man must written as a combination of these lists.

    - in this paragraph, we are focusing on how will be next year. To write a paragraph. I will provide another list of things. It will be list 4. You have to simply extract everything from that list and write a paragraph about how his next year will be. Use the given data to write that paragraph. 
    """

    prompt3 = f""" at the end say again thanks for using our service (davinX) and don't forget to tell them to be kind enough to leave your feedback. stop the article with our slogan. 

    our slogan is " happy life destination "

    # There is a very important thing you have to keep in mind while writing the whole article. It uses simple language throughout the whole article that can be easily understood by grade 5 students. the length of the article must be between 400 to 400 words.
    # and also don't show lists and list numbers and other thechnical details like titels for pharagraphs, word counts and so on.
    #deliver the output in very freandly tone
    #don't use point form in the article and describe everthing things in detail"""

    prompt = prompt1 +"\n"+" list 1 = "+ a +"\n"+" list 2 = "+ b +"\n"+" list 3 = "+ c +"\n"+ prompt2+"\n"+" list 4 = " + d +"\n"+ prompt3

    e = bot.bot(prompt)
    #e = bot.bot("rewrite this paragrap to be more clear. and interesting way.discribe this persons life.personality, social and financial status and future career. don't include the lists. write in 400 words" + d)


    #print("life path",str(x))
    #print("personal number",str(y))
    #print("name value",str(z))

    #print("your life path results are :", str(b),"\n \n \n")
    #print("your name value results are :", str(c),"\n \n \n")
    #print("your next year will be :", str(d),"\n \n \n")

    print(e,)

    #completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt }])
    #print(completion.choices[0].message.content)

    #print("\n"+e)

    #def pedictor (e):
    return e

