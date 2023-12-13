# calculate personal number
def personal_number(day):
    if day == 1 or day == 10 or day == 19 or day == 28:
        personal_number = 1

    elif day == 2 or day == 11 or day == 20:
        personal_number = 2

    elif day == 3 or day == 12 or day == 21 or day == 30:
        personal_number = 3

    elif day == 4 or day == 13 or day == 22 or day == 31:
        personal_number = 4

    elif day == 5 or day == 14 or day == 23:
        personal_number = 5

    elif day == 6 or day == 15 or day == 24:
        personal_number = 6

    elif day == 7 or day == 16 or day == 25:
        personal_number = 7

    elif day == 8 or day == 17 or day == 26:
        personal_number = 8

    elif day == 9 or day == 18 or day == 27:
        personal_number = 9

    else:
        personal_number = 11

    return personal_number




# calculate life path 
def lifepath(day, month, year):
    day_value = personal_number(day)

    month_value = 0
    if month == 1 or month == 10:
        month_value = 1
    elif month == 2 or month == 11:
        month_value = 2
    elif month == 3 or month == 12:
        month_value = 3
    elif month == 4:
        month_value = 4
    elif month == 5:
        month_value = 5
    elif month == 6:
        month_value = 6
    elif month == 7:
        month_value = 7
    elif month == 8:
        month_value = 8
    else:
        month_value = 9

    year_array = [int(digit) for digit in str(year)]

    total_of_year = sum(year_array)

    lifepath_value = day_value + month_value + total_of_year

    if lifepath_value == 1 or lifepath_value == 10 or lifepath_value == 19 or lifepath_value == 28 or lifepath_value == 37 or lifepath_value == 46:
        lifepath_number = 1
    elif lifepath_value == 2 or lifepath_value == 20:
        lifepath_number = 2
    elif lifepath_value == 3 or lifepath_value == 12 or lifepath_value == 21 or lifepath_value == 30 or lifepath_value == 39 or lifepath_value == 48:
        lifepath_number = 3
    elif lifepath_value == 4 or lifepath_value == 13 or lifepath_value == 31 or lifepath_value == 40 or lifepath_value == 49:
        lifepath_number = 4
    elif lifepath_value == 5 or lifepath_value == 14 or lifepath_value == 23 or lifepath_value == 32 or lifepath_value == 41 or lifepath_value == 50:
        lifepath_number = 5
    elif lifepath_value == 6 or lifepath_value == 15 or lifepath_value == 24 or lifepath_value == 33 or lifepath_value == 42 or lifepath_value == 51:
        lifepath_number = 6
    elif lifepath_value == 7 or lifepath_value == 16 or lifepath_value == 25 or lifepath_value == 34 or lifepath_value == 43 or lifepath_value == 52:
        lifepath_number = 7
    elif lifepath_value == 8 or lifepath_value == 17 or lifepath_value == 26 or lifepath_value == 35 or lifepath_value == 44 or lifepath_value == 53:
        lifepath_number = 8
    elif lifepath_value == 9 or lifepath_value == 18 or lifepath_value == 27 or lifepath_value == 36 or lifepath_value == 45 or lifepath_value == 54:
        lifepath_number = 9
    elif lifepath_value == 11 or lifepath_value == 29 or lifepath_value == 38 or lifepath_value == 47:
        lifepath_number = 11
    elif lifepath_value == 22:
        lifepath_number = 22
    else:
        lifepath_number = 33

    return lifepath_number


# letter value
def letter_value(letter):
    if letter == "A" or letter == "I" or letter == "J" or letter == "Q" or letter == "Y":
        letter = 1

    elif letter == "B" or letter == "K" or letter == "R":
        letter = 2

    elif letter == "C" or letter == "G" or letter == "L" or letter == "S":
        letter = 3

    elif letter == "D" or letter == "M" or letter == "T":
        letter = 4

    elif letter == "E" or letter == "H" or letter == "N" or letter == "X":
        letter = 5

    elif letter == "U" or letter == "V" or letter == "W":
        letter = 6

    elif letter == "O" or letter == "Z":
        letter = 7

    elif letter == "F" or letter == "P":
        letter = 8

    return letter

# calculate namevalue
def namevalue(name):
    name = name.upper()
    name_array = []
    total = 0

    for letter in name:
        name_array.append(letter)

    A = 1
    I = 1
    J = 1
    Q = 1
    Y = 1
    B = 2
    K = 2
    R = 2
    C = 3
    G = 3
    L = 3
    S = 3
    D = 4
    M = 4
    T = 4
    E = 5
    H = 5
    N = 5
    X = 5
    U = 6
    V = 6
    W = 6
    O = 7
    Z = 7
    F = 8
    P = 8

    for i in name_array:
        let = letter_value(i)
        total = total + let

    if total == 1 or total == 10 or total == 19 or total == 28 or total == 37 or total == 46:
        name_value = 1
    elif total == 2 or total == 20:
        name_value = 2
    elif total == 3 or total == 12 or total == 21 or total == 30 or total == 39 or total == 48:
        name_value = 3
    elif total == 4 or total == 13 or total == 31 or total == 40 or total == 49:
        name_value = 4
    elif total == 5 or total == 14 or total == 23 or total == 32 or total == 41 or total == 50:
        name_value = 5
    elif total == 6 or total == 15 or total == 24 or total == 33 or total == 42 or total == 51:
        name_value = 6
    elif total == 7 or total == 16 or total == 25 or total == 34 or total == 43 or total == 52:
        name_value = 7
    elif total == 8 or total == 17 or total == 26 or total == 35 or total == 44 or total == 53:
        name_value = 8
    elif total == 9 or total == 18 or total == 27 or total == 36 or total == 45 or total == 54:
        name_value = 9
    elif total == 11 or total == 29 or total == 38 or total == 47:
        name_value = 11
    elif total == 22:
        name_value = 22
    else:
        name_value = 33

    return name_value


# calculate current numerologycal cercul ( cnc )
def cnc(lifepath, year_looking):
    year_array = [int(digit) for digit in str(year_looking)]

    universal_year = sum(year_array)
    cnc = lifepath + universal_year

    return cnc


# results for personal number
def personal_number_results(day):
    personal_number_results = personal_number(day)

    if personal_number_results == 1:
        personal_number_results = f"""  leadership, originality, and confidence. It is a time to initiate, create, and achieve. It is also a time to be independent, courageous, and ambitious. You may face challenges with arrogance, selfishness, or loneliness.
        Skills: You may have a natural ability for innovation, invention, or entrepreneurship. You may also have a talent for authority, management, or politics.
        Likes and dislikes: You may like things that are new, unique, or challenging. You may also like things that are competitive, dynamic, or powerful. You may dislike things that are old, common, or easy.
        Best fitting careers: You may excel in fields that require leadership, originality, or confidence. You may also succeed in fields that require innovation, invention, or entrepreneurship. Some examples are: leader, inventor, entrepreneur, manager, or politician.
        Challenges: You may face obstacles and difficulties that test your will, courage, and determination. You may also face issues and problems that require you to cooperate, compromise, or share. """
    elif personal_number_results == 2:
        personal_number_results = f"""  intuition, inspiration, and illumination. It is a time to trust your inner guidance, express your original ideas, and shine your light to the world. It is also a time to be cooperative, diplomatic, and adaptable. You may face challenges with nervousness, anxiety, or self-doubt.
        Skills: You may have a natural ability for psychic, spiritual, or artistic pursuits. You may also have a talent for leadership, innovation, or communication.
        Likes and dislikes: You may like things that are mystical, visionary, or creative. You may also like things that are harmonious, peaceful, or cooperative. You may dislike things that are mundane, conventional, or rigid.
        Best fitting careers: You may excel in fields that require intuition, inspiration, or illumination. You may also succeed in fields that require cooperation, diplomacy, or adaptability. Some examples are: psychic, healer, teacher, inventor, writer, speaker, mediator, or counselor.
        Challenges: You may face obstacles and difficulties that test your faith, confidence, and courage. You may also face issues and problems that require you to balance your individuality and your partnership. """
    elif personal_number_results == 3:
        personal_number_results = f""" creativity, joy, and communication. It is a time to express yourself, share your ideas, and have fun. It is also a time to be optimistic, enthusiastic, and sociable. You may face challenges with self-discipline, responsibility, or ego.
        Skills: You may have a natural ability for creativity, innovation, or entertainment. You may also have a talent for speaking, writing, or teaching.
        Likes and dislikes: You may like things that are artistic, visionary, or humorous. You may also like things that are harmonious, peaceful, or cooperative. You may dislike things that are mundane, conventional, or rigid.
        Best fitting careers: You may excel in fields that require creativity, joy, or communication. You may also succeed in fields that require innovation, entertainment, or education. Some examples are: artist, writer, speaker, comedian, or teacher. """

    elif personal_number_results == 4:
        personal_number_results = f""" mastery, power, and achievement. It is a time to build, organize, and work hard. It is also a time to be realistic, reliable, and diligent. You may face challenges with materialism, domination, or greed.
        Skills: You may have a natural ability for structure, discipline, or management. You may also have a talent for engineering, science, or mathematics.
        Likes and dislikes: You may like things that are practical, logical, or rational. You may also like things that are stable, secure, or orderly. You may dislike things that are chaotic, unpredictable, or irrational.
        Best fitting careers: You may excel in fields that require mastery, power, or achievement. You may also succeed in fields that require structure, discipline, or management. Some examples are: builder, organizer, leader, engineer, scientist, or politician. """

    elif personal_number_results == 5:
        personal_number_results = f""" change, freedom, and adventure. It is a time to explore, experiment, and experience new things. It is also a time to be flexible, versatile, and curious. You may face challenges with impulsiveness, restlessness, or instability.
        Skills: You may have a natural ability for variety, excitement, or travel. You may also have a talent for sales, marketing, or media.
        Likes and dislikes: You may like things that are different, novel, or surprising. You may also like things that are flexible, adaptable, or spontaneous. You may dislike things that are boring, routine, or predictable.
        Best fitting careers: You may excel in fields that require change, freedom, or adventure. You may also succeed in fields that require variety, excitement, or travel. Some examples are: explorer, adventurer, traveler, salesperson, marketer, or journalist. """

    elif personal_number_results == 6:
        personal_number_results = f"""  love, service, and responsibility. It is a time to care, help, and support others. It is also a time to be loyal, compassionate, and generous. You may face challenges with sacrifice, interference, or perfectionism.
        Skills: You may have a natural ability for care, healing, or education. You may also have a talent for arts, music, or beauty.
        Likes and dislikes: You may like things that are loving, caring, or supportive. You may also like things that are harmonious, peaceful, or cooperative. You may dislike things that are hateful, selfish, or destructive.
        Best fitting careers: You may excel in fields that require love, service, or responsibility. You may also succeed in fields that require care, healing, or education. Some examples are: nurse, doctor, teacher, artist, musician, or beautician. """

    elif personal_number_results == 7:
        personal_number_results = f""" wisdom, spirituality, and introspection. It is a time to learn, analyze, and understand yourself and the world. It is also a time to be calm, reflective, and meditative. You may face challenges with isolation, skepticism, or cynicism.
        Skills: You may have a natural ability for research, analysis, or knowledge. You may also have a talent for science, philosophy, or spirituality.
        Likes and dislikes: You may like things that are mysterious, profound, or enlightening. You may also like things that are peaceful, serene, or meditative. You may dislike things that are superficial, trivial, or distracting.
        Best fitting careers: You may excel in fields that require wisdom, spirituality, or introspection. You may also succeed in fields that require research, analysis, or knowledge. Some examples are: researcher, analyst, scientist, philosopher, or spiritualist. """

    elif personal_number_results == 8:
        personal_number_results = f""" power, success, and abundance. It is a time to achieve, lead, and prosper. It is also a time to be confident, ambitious, and authoritative. You may face challenges with materialism, domination, or greed.
        Skills: You may have a natural ability for leadership, management, or business. You may also have a talent for finance, law, or politics.
        Likes and dislikes: You may like things that are practical, logical, or rational. You may also like things that are stable, secure, or orderly. You may dislike things that are chaotic, unpredictable, or irrational.
        Best fitting careers: You may excel in fields that require power, success, or abundance. You may also succeed in fields that require leadership, management, or business. Some examples are: leader, manager, entrepreneur, financier, lawyer, or politician. """

    elif personal_number_results == 9:
        personal_number_results = f""" completion, humanitarianism, and transformation. It is a time to finish, release, and let go of what no longer serves you. It is also a time to be compassionate, altruistic, and visionary. You may face challenges with attachment, loss, or resentment.
        Skills: You may have a natural ability for service, healing, or education. You may also have a talent for arts, music, or spirituality.
        Likes and dislikes: You may like things that are loving, caring, or supportive. You may also like things that are harmonious, peaceful, or cooperative. You may dislike things that are hateful, selfish, or destructive.
        Best fitting careers: You may excel in fields that require completion, humanitarianism, or transformation. You may also succeed in fields that require service, healing, or education. Some examples are: nurse, doctor, teacher, artist, musician, or humanitarian. """

    else:   
        personal_number_results = f""" intuition, inspiration, and illumination. It is a time to trust your inner guidance, express your original ideas, and shine your light to the world. It is also a time to be cooperative, diplomatic, and adaptable. You may face challenges with nervousness, anxiety, or self-doubt.
        Skills: You may have a natural ability for psychic, spiritual, or artistic pursuits. You may also have a talent for leadership, innovation, or communication.
        Likes and dislikes: You may like things that are mystical, visionary, or creative. You may also like things that are harmonious, peaceful, or cooperative. You may dislike things that are mundane, conventional, or rigid.
        Best fitting careers: You may excel in fields that require intuition, inspiration, or illumination. You may also succeed in fields that require cooperation, diplomacy, or adaptability. Some examples are: psychic, healer, teacher, inventor, writer, speaker, mediator, or counselor.
        Challenges: You may face obstacles and difficulties that test your faith, confidence, and courage. You may also face issues and problems that require you to balance your individuality and your partnership.
        Compatibility: You may get along well with others who are intuitive, inspirational, or illuminating. You may also get along well with others who are cooperative, diplomatic, or adaptable. Some compatible numbers are: 2, 3, 6, and 9.

        This is a number of intuition, inspiration, and illumination. It is a time to trust your inner guidance, express your original ideas, and shine your light to the world. It is also a time to be cooperative, diplomatic, and adaptable. You may face challenges with nervousness, anxiety, or self-doubt. This number is considered to be very unfortunate and stressful, as it indicates a person who has great difficulties to contend against and who lives in a fool’s paradise. """

    return personal_number_results
    


# results for life parth
def lifepath_results(day, month, year):
    lifepath_results = lifepath(day, month, year)

    if lifepath_results == 1:
        lifepath_results = f"""  leadership, originality, and confidence. It is a time to initiate, create, and achieve. It is also a time to be independent, courageous, and ambitious. You may face challenges with arrogance, selfishness, or loneliness.
        Lucky numbers: Your lucky numbers are 1, 10, 19, and 28. These numbers can bring you success, recognition, and fame.
        Born talents: You may have a natural ability for innovation, invention, or entrepreneurship. You may also have a talent for authority, management, or politics.
        Fortune and misfortune: You may experience fortune in your life when you follow your own path, trust your instincts, and take action. You may experience misfortune in your life when you ignore your inner voice, depend on others, or procrastinate.
        Purpose: Your purpose is to be a leader, an innovator, and a pioneer. You are meant to create something new, original, and valuable for yourself and others.
        Lessons: Your lessons are to learn humility, cooperation, and compassion. You need to balance your individuality and your partnership, your confidence and your sensitivity, and your ambition and your generosity.
         """
    
    elif lifepath_results == 2:
        lifepath_results = f""" partnership, cooperation, and diplomacy. It is a time to seek harmony, balance, and peace in your relationships and situations. It is also a time to be receptive, intuitive, and adaptable. You may face challenges with indecision, sensitivity, or dependence.
        Lucky numbers: Your lucky numbers are 2, 11, 20, and 29. These numbers can bring you harmony, friendship, and love.
        Born talents: You may have a natural ability for psychic, spiritual, or artistic pursuits. You may also have a talent for teamwork, negotiation, or counseling.
        Fortune and misfortune: You may experience fortune in your life when you listen to your intuition, cooperate with others, and be flexible. You may experience misfortune in your life when you doubt yourself, conflict with others, or be rigid.
        Purpose: Your purpose is to be a partner, a mediator, and a peacemaker. You are meant to create harmony, balance, and peace for yourself and others.
        Lessons: Your lessons are to learn assertiveness, confidence, and independence. You need to balance your receptivity and your expression, your sensitivity and your strength, and your adaptability and your stability.
         """

    elif lifepath_results == 3:
        lifepath_results = f""" creativity, joy, and communication. It is a time to express yourself, share your ideas, and have fun. It is also a time to be optimistic, enthusiastic, and sociable. You may face challenges with self-discipline, responsibility, or ego.
        Lucky numbers: Your lucky numbers are 3, 12, 21, and 30. These numbers can bring you creativity, happiness, and popularity.
        Born talents: You may have a natural ability for creativity, innovation, or entertainment. You may also have a talent for speaking, writing, or teaching.
        Fortune and misfortune: You may experience fortune in your life when you express yourself, communicate with others, and enjoy life. You may experience misfortune in your life when you suppress yourself, isolate yourself, or take life too seriously.
        Purpose: Your purpose is to be a creator, an entertainer, and a communicator. You are meant to create something beautiful, joyful, and meaningful for yourself and others.
        Lessons: Your lessons are to learn discipline, focus, and humility. You need to balance your creativity and your productivity, your enthusiasm and your realism, and your sociability and your solitude.

         """
    
    elif lifepath_results == 4:
        lifepath_results = f""" stability, order, and practicality. It is a time to build, organize, and work hard. It is also a time to be realistic, reliable, and diligent. You may face challenges with rigidity, limitation, or boredom.
        Lucky numbers: Your lucky numbers are 4, 13, 22, and 31. These numbers can bring you stability, security, and success.
        Born talents: You may have a natural ability for structure, discipline, or management. You may also have a talent for engineering, science, or mathematics.
        Fortune and misfortune: You may experience fortune in your life when you plan, execute, and achieve your goals. You may experience misfortune in your life when you procrastinate, avoid, or give up on your goals.
        Purpose: Your purpose is to be a builder, an organizer, and a worker. You are meant to create something solid, reliable, and useful for yourself and others.
        Lessons: Your lessons are to learn flexibility, innovation, and openness. You need to balance your structure and your spontaneity, your discipline and your freedom, and your order and your chaos.
         """

    elif lifepath_results == 5:
        lifepath_results = f""" change, freedom, and adventure. It is a time to explore, experiment, and experience new things. It is also a time to be flexible, versatile, and curious. You may face challenges with impulsiveness, restlessness, or instability.
        Lucky numbers: Your lucky numbers are 5, 14, 23, and 32. These numbers can bring you change, excitement, and opportunity.
        Born talents: You may have a natural ability for variety, excitement, or travel. You may also have a talent for sales, marketing, or media.
        Fortune and misfortune: You may experience fortune in your life when you embrace change, seek adventure, and learn new things. You may experience misfortune in your life when you resist change, fear adventure, or stagnate in old things.
        Purpose: Your purpose is to be an explorer, an adventurer, and a learner. You are meant to experience different things, expand your horizons, and discover yourself.
        Lessons: Your lessons are to learn consistency, commitment, and focus. You need to balance your variety and your routine, your excitement and your calm, and your curiosity and your concentration.
        """

    elif lifepath_results == 6:
        lifepath_results = f"""  love, service, and responsibility. It is a time to care, help, and support others. It is also a time to be loyal, compassionate, and generous. You may face challenges with sacrifice, interference, or perfectionism.
        Lucky numbers: Your lucky numbers are 6, 15, 24, and 33. These numbers can bring you love, happiness, and peace.
        Born talents: You may have a natural ability for care, healing, or education. You may also have a talent for arts, music, or beauty.
        Fortune and misfortune: You may experience fortune in your life when you love yourself, serve others, and take responsibility. You may experience misfortune in your life when you neglect yourself, interfere with others, or take blame.
        Purpose: Your purpose is to be a lover, a healer, and a teacher. You are meant to love yourself and others, heal yourself and others, and teach yourself and others.
        Lessons: Your lessons are to learn boundaries, expression, and acceptance. You need to balance your service and your self-care, your compassion and your assertiveness, and your responsibility and your forgiveness.
         """

    elif lifepath_results == 7:
        lifepath_results = f""" wisdom, spirituality, and introspection. It is a time to learn, analyze, and understand yourself and the world. It is also a time to be calm, reflective, and meditative. You may face challenges with isolation, skepticism, or cynicism.
        Lucky numbers: Your lucky numbers are 7, 16, 25, and 34. These numbers can bring you wisdom, insight, and enlightenment.
        Born talents: You may have a natural ability for research, analysis, or knowledge. You may also have a talent for science, philosophy, or spirituality.
        Fortune and misfortune: You may experience fortune in your life when you seek knowledge, trust your intuition, and follow your path. You may experience misfortune in your life when you ignore knowledge, doubt your intuition, or lose your direction.
        Purpose: Your purpose is to be a seeker, a thinker, and a mystic. You are meant to seek knowledge, think deeply, and connect with the divine.
        Lessons: Your lessons are to learn connection, trust, and emotion. You need to balance your introspection and your interaction, your analysis and your intuition, and your logic and your feeling.
         """

    elif lifepath_results == 8:
        lifepath_results = f""" power, success, and abundance. It is a time to achieve, lead, and prosper. It is also a time to be confident, ambitious, and authoritative. You may face challenges with materialism, domination, or greed.
        Lucky numbers: Your lucky numbers are 8, 17, 26, and 35. These numbers can bring you power, wealth, and influence.
        Born talents: You may have a natural ability for leadership, management, or business. You may also have a talent for finance, law, or politics.
        Fortune and misfortune: You may experience fortune in your life when you use your power wisely, lead by example, and prosper with integrity. You may experience misfortune in your life when you abuse your power, lead by force, or prosper with dishonesty.
        Purpose: Your purpose is to be a leader, a manager, and a entrepreneur. You are meant to use your power, authority, and influence for the greater good of yourself and others.
        Lessons: Your lessons are to learn ethics, compassion, and balance. You need to balance your material and spiritual goals, your ambition and generosity, and your confidence and humility.
         """

    elif lifepath_results == 9:
        lifepath_results = f""" completion, humanitarianism, and transformation. It is a time to finish, release, and let go of what no longer serves you. It is also a time to be compassionate, altruistic, and visionary. You may face challenges with attachment, loss, or resentment.
        Lucky numbers: Your lucky numbers are 9, 18, 27, and 36. These numbers can bring you completion, fulfillment, and peace.
        Born talents: You may have a natural ability for service, healing, or education. You may also have a talent for arts, music, or spirituality.
        Fortune and misfortune: You may experience fortune in your life when you love yourself, serve others, and take responsibility. You may experience misfortune in your life when you neglect yourself, interfere with others, or take blame.
        Purpose: Your purpose is to be a humanitarian, a healer, and a teacher. You are meant to love yourself and others, heal yourself and others, and teach yourself and others.
        Lessons: Your lessons are to learn detachment, forgiveness, and acceptance. You need to let go of what no longer serves you, forgive yourself and others, and accept yourself and others.
         """

    elif lifepath_results == 11:
        lifepath_results = f""" partnership, cooperation, and diplomacy. It is a time to seek harmony, balance, and peace in your relationships and situations. It is also a time to be receptive, intuitive, and adaptable. You may face challenges with indecision, sensitivity, or dependence.
        Lucky numbers: Your lucky numbers are 2, 11, 20, and 29. These numbers can bring you harmony, friendship, and love.
        Born talents: You may have a natural ability for psychic, spiritual, or artistic pursuits. You may also have a talent for teamwork, negotiation, or counseling.
        Fortune and misfortune: You may experience fortune in your life when you listen to your intuition, cooperate with others, and be flexible. You may experience misfortune in your life when you doubt yourself, conflict with others, or be rigid.
        Purpose: Your purpose is to be a partner, a mediator, and a peacemaker. You are meant to create harmony, balance, and peace for yourself and others.
        Lessons: Your lessons are to learn assertiveness, confidence, and independence. You need to balance your receptivity and your expression, your sensitivity and your strength, and your adaptability and your stability.

        This is a number of intuition, inspiration, and illumination. It is a time to trust your inner guidance, express your original ideas, and shine your light to the world. It is also a time to be cooperative, diplomatic, and adaptable. You may face challenges with nervousness, anxiety, or self-doubt. This number is considered to be very unfortunate and stressful, as it indicates a person who has great difficulties to contend against and who lives in a fool’s paradise.
         """

    elif lifepath_results == 22:
        lifepath_results = f""" stability, order, and practicality. It is a time to build, organize, and work hard. It is also a time to be realistic, reliable, and diligent. You may face challenges with rigidity, limitation, or boredom.
        Lucky numbers: Your lucky numbers are 4, 13, 22, and 31. These numbers can bring you stability, security, and success.
        Born talents: You may have a natural ability for structure, discipline, or management. You may also have a talent for engineering, science, or mathematics.
        Fortune and misfortune: You may experience fortune in your life when you plan, execute, and achieve your goals. You may experience misfortune in your life when you procrastinate, avoid, or give up on your goals.
        Purpose: Your purpose is to be a builder, an organizer, and a worker. You are meant to create something solid, reliable, and useful for yourself and others.
        Lessons: Your lessons are to learn flexibility, innovation, and openness. You need to balance your structure and your spontaneity, your discipline and your freedom, and your order and your chaos.

        This is a number of mastery, power, and achievement. It is a time to build, organize, and work hard. It is also a time to be realistic, reliable, and diligent. You may face challenges with materialism, domination, or greed. This number is also considered to be very unfortunate and naive, as it indicates a person who is blinded by the folly of others and who is constantly ripped off by bad people.
         """

    elif lifepath_results == 33:
        lifepath_results = f"""  love, service, and responsibility. It is a time to care, help, and support others. It is also a time to be loyal, compassionate, and generous. You may face challenges with sacrifice, interference, or perfectionism.
        Lucky numbers: Your lucky numbers are 6, 15, 24, and 33. These numbers can bring you love, happiness, and peace.
        Born talents: You may have a natural ability for care, healing, or education. You may also have a talent for arts, music, or beauty.
        Fortune and misfortune: You may experience fortune in your life when you love yourself, serve others, and take responsibility. You may experience misfortune in your life when you neglect yourself, interfere with others, or take blame.
        Purpose: Your purpose is to be a lover, a healer, and a teacher. You are meant to love yourself and others, heal yourself and others, and teach yourself and others.
        Lessons: Your lessons are to learn boundaries, expression, and acceptance. You need to balance your service and your self-care, your compassion and your assertiveness, and your responsibility and your forgiveness.

        This is a number of love, service, and responsibility. It is a time to care, help, and support others. It is also a time to be loyal, compassionate, and generous. You may face challenges with sacrifice, interference, or perfectionism. This number is considered to be very fortunate and beneficial, as it indicates a person who has the assistance and association of those of rank and position and who gains through love and the opposite sex. """

    return lifepath_results

# results for namevalues
def namevalue_results(name):
    namevalue_results = namevalue(name)

    if namevalue_results == 1:
        namevalue_results = f"""  leadership, originality, and confidence. It is a time to initiate, create, and achieve. It is also a time to be independent, courageous, and ambitious. You may face challenges with arrogance, selfishness, or loneliness.
        Lucky numbers: Your lucky numbers are 1, 10, 19, and 28. These numbers can bring you success, recognition, and fame.
        How they interact with society: You may have a strong and assertive personality, that can make you a leader, an innovator, or a pioneer. You may also have a confident and decisive communication style, that can help you express your ideas and opinions. You may influence and be influenced by the world around you through your originality, creativity, and leadership.
        About their friends: You may attract and be attracted to people who are innovative, inventive, or entrepreneurial. You may also have friends who are competitive, dynamic, or powerful. You may support and challenge each other to achieve your goals and dreams. You may be compatible with people who share your vision and passion, and incompatible with people who oppose your ideas and actions.
        Opportunities and open doors: You may encounter chances and possibilities that allow you to express your originality, creativity, and leadership. You may also find opportunities and open doors that help you to achieve success, recognition, and fame. You may benefit from being proactive, confident, and decisive.
        Purpose: Your purpose is to be a leader, an innovator, and a pioneer. You are meant to create something new, original, and valuable for yourself and others.
        Hidden potential: You may have a hidden potential for innovation, invention, or entrepreneurship. You may also have a latent talent for authority, management, or politics. You may enhance your abilities and talents by trusting your instincts, following your path, and taking action.
        Lessons: Your lessons are to learn humility, cooperation, and compassion. You need to balance your individuality and your partnership, your confidence and your sensitivity, and your ambition and your generosity.
        Karmic lessons and challenges: You may have to face and resolve issues and problems that are related to your ego, pride, or independence. You may also have to deal with karmic consequences of your past lives or actions, such as being too arrogant, selfish, or lonely. You may overcome your challenges by learning humility, cooperation, and compassion.
         """
    
    elif namevalue_results == 2:
        namevalue_results = f""" partnership, cooperation, and diplomacy. It is a time to seek harmony, balance, and peace in your relationships and situations. It is also a time to be receptive, intuitive, and adaptable. You may face challenges with indecision, sensitivity, or dependence.
        Lucky numbers: Your lucky numbers are 2, 11, 20, and 29. These numbers can bring you harmony, friendship, and love.
        How they interact with society: You may have a gentle and cooperative personality, that can make you a partner, a mediator, or a peacemaker. You may also have a receptive and diplomatic communication style, that can help you listen and relate to others. You may influence and be influenced by the world around you through your harmony, balance, and peace.
        About their friends: You may attract and be attracted to people who are psychic, spiritual, or artistic. You may also have friends who are harmonious, peaceful, or cooperative. You may support and challenge each other to grow and heal. You may be compatible with people who understand and appreciate you, and incompatible with people who hurt or ignore you.
        Opportunities and open doors: You may encounter chances and possibilities that allow you to listen to your intuition, cooperate with others, and be flexible. You may also find opportunities and open doors that help you to find harmony, friendship, and love. You may benefit from being receptive, diplomatic, and adaptable.
        Purpose: Your purpose is to be a partner, a mediator, and a peacemaker. You are meant to create harmony, balance, and peace for yourself and others.
        Hidden potential: You may have a hidden potential for psychic, spiritual, or artistic pursuits. You may also have a latent talent for teamwork, negotiation, or counseling. You may enhance your abilities and talents by trusting your intuition, cooperating with others, and being flexible.
        Lessons: Your lessons are to learn assertiveness, confidence, and independence. You need to balance your receptivity and your expression, your sensitivity and your strength, and your adaptability and your stability.
        Karmic lessons and challenges: You may have to face and resolve issues and problems that are related to your self-esteem, confidence, or independence. You may also have to deal with karmic consequences of your past lives or actions, such as being too indecisive, sensitive, or dependent. You may overcome your challenges by learning assertiveness, confidence, and independence.
         """

    elif namevalue_results == 3:
        namevalue_results = f""" creativity, joy, and communication. It is a time to express yourself, share your ideas, and have fun. It is also a time to be optimistic, enthusiastic, and sociable. You may face challenges with self-discipline, responsibility, or ego.
        Lucky numbers: Your lucky numbers are 3, 12, 21, and 30. These numbers can bring you creativity, happiness, and popularity.
        How they interact with society: You may have a creative and joyful personality, that can make you a creator, an entertainer, or a communicator. You may also have a optimistic and enthusiastic communication style, that can help you share your ideas and opinions. You may influence and be influenced by the world around you through your creativity, joy, and communication.
        About their friends: You may attract and be attracted to people who are artistic, visionary, or humorous. You may also have friends who are harmonious, peaceful, or cooperative. You may support and challenge each other to express and enjoy yourselves. You may be compatible with people who inspire and appreciate you, and incompatible with people who bore or criticize you.
        Opportunities and open doors: You may encounter chances and possibilities that allow you to express yourself, communicate with others, and enjoy life. You may also find opportunities and open doors that help you to create something beautiful, joyful, and meaningful for yourself and others. You may benefit from being optimistic, enthusiastic, and sociable.
        Purpose: Your purpose is to be a creator, an entertainer, and a communicator. You are meant to create something beautiful, joyful, and meaningful for yourself and others.
        Hidden potential: You may have a hidden potential for creativity, innovation, or entertainment. You may also have a latent talent for speaking, writing, or teaching. You may enhance your abilities and talents by expressing yourself, communicating with others, and enjoying life.
        Lessons: Your lessons are to learn discipline, focus, and humility. You need to balance your creativity and your productivity, your enthusiasm and your realism, and your sociability and your solitude.
        Karmic lessons and challenges: You may have to face and resolve issues and problems that are related to your self-discipline, responsibility, or ego. You may also have to deal with karmic consequences of your past lives or actions, such as being too irresponsible, careless, or vain. You may overcome your challenges by learning discipline, focus, and humility.
         """
    
    elif namevalue_results == 4:
        namevalue_results = f""" stability, order, and practicality. It is a time to build, organize, and work hard. It is also a time to be realistic, reliable, and diligent. You may face challenges with rigidity, limitation, or boredom.
        Lucky numbers: Your lucky numbers are 4, 13, 22, and 31. These numbers can bring you stability, security, and success.
        How they interact with society: You may have a stable and orderly personality, that can make you a builder, an organizer, or a worker. You may also have a realistic and reliable communication style, that can help you plan and execute your goals. You may influence and be influenced by the world around you through your stability, order, and practicality.
        About their friends: You may attract and be attracted to people who are practical, logical, or rational. You may also have friends who are stable, secure, or orderly. You may support and challenge each other to build and achieve your goals. You may be compatible with people who share your values and standards, and incompatible with people who violate your rules and expectations.
        Opportunities and open doors: You may encounter chances and possibilities that allow you to build, organize, and work hard. You may also find opportunities and open doors that help you to achieve stability, security, and success. You may benefit from being realistic, reliable, and diligent.
        Purpose: Your purpose is to be a builder, an organizer, and a worker. You are meant to create something solid, reliable, and useful for yourself and others.
        Hidden potential: You may have a hidden potential for structure, discipline, or management. You may also have a latent talent for engineering, science, or mathematics. You may enhance your abilities and talents by planning, executing, and achieving your goals.
        Lessons: Your lessons are to learn flexibility, innovation, and openness. You need to balance your structure and your spontaneity, your discipline and your freedom, and your order and your chaos.
        Karmic lessons and challenges: you lack these qualities in your life and you need to develop them. You may have been irresponsible, self-indulgent, or disorganized in your previous life, and now you have to face the consequences. You may have trouble finding your direction, establishing your foundation, or achieving your goals. You may also have to deal with karmic consequences of your past lives or actions, such as being too rigid, limited, or bored.To overcome these challenges, you need to learn discipline, focus, and humility. You need to balance your structure and your spontaneity, your discipline and your freedom, and your order and your chaos. You need to plan, execute, and achieve your goals with realism, reliability, and diligence. You need to create something solid, reliable, and useful for yourself and others.
         """


    elif namevalue_results == 5:
        namevalue_results = f""" change, freedom, and adventure. It is a time to explore, experiment, and experience new things. It is also a time to be flexible, versatile, and curious. You may face challenges with impulsiveness, restlessness, or instability.
        Lucky numbers: Your lucky numbers are 5, 14, 23, and 32. These numbers can bring you change, excitement, and opportunity.
        How they interact with society: You may have a adventurous and curious personality, that can make you an explorer, an adventurer, or a learner. You may also have a flexible and versatile communication style, that can help you adapt and improvise in different situations. You may influence and be influenced by the world around you through your change, freedom, and adventure.
        About their friends: You may attract and be attracted to people who are different, novel, or surprising. You may also have friends who are flexible, adaptable, or spontaneous. You may support and challenge each other to explore and experience new things. You may be compatible with people who stimulate and appreciate you, and incompatible with people who bore or restrict you.
        Opportunities and open doors: You may encounter chances and possibilities that allow you to explore, experiment, and experience new things. You may also find opportunities and open doors that help you to expand your horizons, discover yourself, and learn new things. You may benefit from being flexible, versatile, and curious.
        Purpose: Your purpose is to be an explorer, an adventurer, and a learner. You are meant to experience different things, expand your horizons, and discover yourself.
        Hidden potential: You may have a hidden potential for variety, excitement, or travel. You may also have a latent talent for sales, marketing, or media. You may enhance your abilities and talents by embracing change, seeking adventure, and learning new things.
        Lessons: Your lessons are to learn consistency, commitment, and focus. You need to balance your variety and your routine, your excitement and your calm, and your curiosity and your concentration.
        Karmic lessons and challenges: You may have to face and resolve issues and problems that are related to your impulsiveness, restlessness, or instability. You may also have to deal with karmic consequences of your past lives or actions, such as being too reckless, irresponsible, or unfaithful. You may overcome your challenges by learning consistency, commitment, and focus.
         """


    elif namevalue_results == 6:
        namevalue_results = f""" love, service, and responsibility. It is a time to care, help, and support others. It is also a time to be loyal, compassionate, and generous. You may face challenges with sacrifice, interference, or perfectionism.
        Lucky numbers: Your lucky numbers are 6, 15, 24, and 33. These numbers can bring you love, happiness, and peace.
        How they interact with society: You may have a loving and caring personality, that can make you a lover, a healer, or a teacher. You may also have a loyal and compassionate communication style, that can help you listen and relate to others. You may influence and be influenced by the world around you through your love, service, and responsibility.
        About their friends: You may attract and be attracted to people who are loving, caring, or supportive. You may also have friends who are harmonious, peaceful, or cooperative. You may support and challenge each other to love and heal yourselves and others. You may be compatible with people who understand and appreciate you, and incompatible with people who hurt or ignore you.
        Opportunities and open doors: You may encounter chances and possibilities that allow you to love yourself, serve others, and take responsibility. You may also find opportunities and open doors that help you to find love, happiness, and peace. You may benefit from being loyal, compassionate, and generous.
        Purpose: Your purpose is to be a lover, a healer, and a teacher. You are meant to love yourself and others, heal yourself and others, and teach yourself and others.
        Hidden potential: You may have a hidden potential for care, healing, or education. You may also have a latent talent for arts, music, or beauty. You may enhance your abilities and talents by loving yourself, serving others, and taking responsibility.
        Lessons: Your lessons are to learn boundaries, expression, and acceptance. You need to balance your service and your self-care, your compassion and your assertiveness, and your responsibility and your forgiveness.
        Karmic lessons and challenges: You may have to face and resolve issues and problems that are related to your sacrifice, interference, or perfectionism. You may also have to deal with karmic consequences of your past lives or actions, such as being too sacrificing, interfering, or demanding. You may overcome your challenges by learning boundaries, expression, and acceptance.
         """

    elif namevalue_results == 7:
        namevalue_results = f""" wisdom, spirituality, and introspection. It is a time to learn, analyze, and understand yourself and the world. It is also a time to be calm, reflective, and meditative. You may face challenges with isolation, skepticism, or cynicism.
        Lucky numbers: Your lucky numbers are 7, 16, 25, and 34. These numbers can bring you wisdom, insight, and enlightenment.
        How they interact with society: You may have a wise and introspective personality, that can make you a seeker, a thinker, or a mystic. You may also have a calm and reflective communication style, that can help you learn and understand yourself and others. You may influence and be influenced by the world around you through your wisdom, spirituality, and introspection.
        About their friends: You may attract and be attracted to people who are mysterious, profound, or enlightening. You may also have friends who are peaceful, serene, or meditative. You may support and challenge each other to seek knowledge, trust intuition, and follow your path. You may be compatible with people who respect and appreciate you, and incompatible with people who distract or deceive you.
        Opportunities and open doors: You may encounter chances and possibilities that allow you to learn, analyze, and understand yourself and the world. You may also find opportunities and open doors that help you to connect with the divine, find your purpose, and transform yourself. You may benefit from being calm, reflective, and meditative.
        Purpose: Your purpose is to be a seeker, a thinker, and a mystic. You are meant to seek knowledge, think deeply, and connect with the divine.
        Hidden potential: You may have a hidden potential for research, analysis, or knowledge. You may also have a latent talent for science, philosophy, or spirituality. You may enhance your abilities and talents by learning, analyzing, and understanding yourself and the world.
        Lessons: Your lessons are to learn connection, trust, and emotion. You need to balance your introspection and your interaction, your analysis and your intuition, and your logic and your feeling.
        Karmic lessons and challenges: You may have to face and resolve issues and problems that are related to your isolation, skepticism, or cynicism. You may also have to deal with karmic consequences of your past lives or actions, such as being too isolated, skeptical, or cynical. You may overcome your challenges by learning connection, trust, and emotion.
         """

    elif namevalue_results == 8:
        namevalue_results = f""" power, success, and abundance. It is a time to achieve, lead, and prosper. It is also a time to be confident, ambitious, and authoritative. You may face challenges with materialism, domination, or greed.
        Lucky numbers: Your lucky numbers are 8, 17, 26, and 35. These numbers can bring you power, wealth, and influence.
        How they interact with society: You may have a powerful and ambitious personality, that can make you a leader, a manager, or a entrepreneur. You may also have a confident and authoritative communication style, that can help you influence and inspire others. You may influence and be influenced by the world around you through your power, success, and abundance.
        About their friends: You may attract and be attracted to people who are practical, logical, or rational. You may also have friends who are stable, secure, or orderly. You may support and challenge each other to achieve and prosper. You may be compatible with people who share your goals and standards, and incompatible with people who oppose your plans and actions.
        Opportunities and open doors: You may encounter chances and possibilities that allow you to achieve, lead, and prosper. You may also find opportunities and open doors that help you to attain power, wealth, and influence. You may benefit from being confident, ambitious, and authoritative.
        Purpose: Your purpose is to be a leader, a manager, and a entrepreneur. You are meant to use your power, authority, and influence for the greater good of yourself and others.
        Hidden potential: You may have a hidden potential for leadership, management, or business. You may also have a latent talent for finance, law, or politics. You may enhance your abilities and talents by using your power wisely, leading by example, and prospering with integrity.
        Lessons: Your lessons are to learn ethics, compassion, and balance. You need to balance your material and spiritual goals, your ambition and generosity, and your confidence and humility.
        Karmic lessons and challenges: You may have to face and resolve issues and problems that are related to your materialism, domination, or greed. You may also have to deal with karmic consequences of your past lives or actions, such as abusing your power, leading by force, or prospering with dishonesty. You may overcome your challenges by learning ethics, compassion, and balance.
         """


    elif namevalue_results == 9:
        namevalue_results = f""" completion, humanitarianism, and transformation. It is a time to finish, release, and let go of what no longer serves you. It is also a time to be compassionate, altruistic, and visionary. You may face challenges with attachment, loss, or resentment.
        Lucky numbers: Your lucky numbers are 9, 18, 27, and 36. These numbers can bring you completion, fulfillment, and peace.
        How they interact with society: You may have a compassionate and visionary personality, that can make you a humanitarian, a healer, or a teacher. You may also have a altruistic and inspirational communication style, that can help you serve and uplift others. You may influence and be influenced by the world around you through your completion, humanitarianism, and transformation.
        About their friends: You may attract and be attracted to people who are loving, caring, or supportive. You may also have friends who are harmonious, peaceful, or cooperative. You may support and challenge each other to love and heal yourselves and others. You may be compatible with people who understand and appreciate you, and incompatible with people who hurt or ignore you.
        Opportunities and open doors: You may encounter chances and possibilities that allow you to finish, release, and let go of what no longer serves you. You may also find opportunities and open doors that help you to connect with the divine, find your purpose, and transform yourself. You may benefit from being compassionate, altruistic, and visionary.
        Purpose: Your purpose is to be a humanitarian, a healer, and a teacher. You are meant to love yourself and others, heal yourself and others, and teach yourself and others.
        Hidden potential: You may have a hidden potential for service, healing, or education. You may also have a latent talent for arts, music, or spirituality. You may enhance your abilities and talents by loving yourself, serving others, and taking responsibility.
        Lessons: Your lessons are to learn detachment, forgiveness, and acceptance. You need to let go of what no longer serves you, forgive yourself and others, and accept yourself and others.
        Karmic lessons and challenges: You may have to face and resolve issues and problems that are related to your attachment, loss, or resentment. You may also have to deal with karmic consequences of your past lives or actions, such as being too sacrificing, interfering, or demanding. You may overcome your challenges by learning detachment, forgiveness, and acceptance.
         """


    elif namevalue_results == 11:
        namevalue_results = f""" completion, humanitarianism, and transformation. It is a time to finish, release, and let go of what no longer serves you. It is also a time to be compassionate, altruistic, and visionary. You may face challenges with attachment, loss, or resentment.
        Lucky numbers: Your lucky numbers are 9, 18, 27, and 36. These numbers can bring you completion, fulfillment, and peace.
        How they interact with society: You may have a compassionate and visionary personality, that can make you a humanitarian, a healer, or a teacher. You may also have a altruistic and inspirational communication style, that can help you serve and uplift others. You may influence and be influenced by the world around you through your completion, humanitarianism, and transformation.
        About their friends: You may attract and be attracted to people who are loving, caring, or supportive. You may also have friends who are harmonious, peaceful, or cooperative. You may support and challenge each other to love and heal yourselves and others. You may be compatible with people who understand and appreciate you, and incompatible with people who hurt or ignore you.
        Opportunities and open doors: You may encounter chances and possibilities that allow you to finish, release, and let go of what no longer serves you. You may also find opportunities and open doors that help you to connect with the divine, find your purpose, and transform yourself. You may benefit from being compassionate, altruistic, and visionary.
        Purpose: Your purpose is to be a humanitarian, a healer, and a teacher. You are meant to love yourself and others, heal yourself and others, and teach yourself and others.
        Hidden potential: You may have a hidden potential for service, healing, or education. You may also have a latent talent for arts, music, or spirituality. You may enhance your abilities and talents by loving yourself, serving others, and taking responsibility.
        Lessons: Your lessons are to learn detachment, forgiveness, and acceptance. You need to let go of what no longer serves you, forgive yourself and others, and accept yourself and others.
        Karmic lessons and challenges: You may have to face and resolve issues and problems that are related to your attachment, loss, or resentment. You may also have to deal with karmic consequences of your past lives or actions, such as being too sacrificing, interfering, or demanding. You may overcome your challenges by learning detachment, forgiveness, and acceptance.
         """


    elif namevalue_results == 22:
        namevalue_results = f"""  mastery, power, and achievement. It is a time to build, organize, and work hard. It is also a time to be realistic, reliable, and diligent. You may face challenges with materialism, domination, or greed. This number is also considered to be very unfortunate and naive, as it indicates a person who is blinded by the folly of others and who is constantly ripped off by bad people.
        Lucky numbers: Your lucky numbers are 22, 31, 40, and 49. These numbers can bring you mastery, power, and achievement.
        How they interact with society: You may have a powerful and ambitious personality, that can make you a master, a builder, or a achiever. You may also have a realistic and reliable communication style, that can help you plan and execute your goals. You may influence and be influenced by the world around you through your mastery, power, and achievement.
        About their friends: You may attract and be attracted to people who are practical, logical, or rational. You may also have friends who are stable, secure, or orderly. You may support and challenge each other to build and achieve your goals. You may be compatible with people who share your goals and standards, and incompatible with people who oppose your plans and actions.
        Opportunities and open doors: You may encounter chances and possibilities that allow you to build, organize, and work hard. You may also find opportunities and open doors that help you to attain mastery, power, and achievement. You may benefit from being realistic, reliable, and diligent.
        Purpose: Your purpose is to be a master, a builder, and a achiever. You are meant to use your mastery, power, and achievement for the greater good of yourself and others.
        Hidden potential: You may have a hidden potential for structure, discipline, or management. You may also have a latent talent for engineering, science, or mathematics. You may enhance your abilities and talents by planning, executing, and achieving your goals.
        Lessons: Your lessons are to learn ethics, compassion, and balance. You need to balance your material and spiritual goals, your ambition and generosity, and your confidence and humility.
        Karmic lessons and challenges: You may have to face and resolve issues and problems that are related to your materialism, domination, or greed. You may also have to deal with karmic consequences of your past lives or actions, such as abusing your power, leading by force, or prospering with dishonesty. You may overcome your challenges by learning ethics, compassion, and balance.
         """

    elif namevalue_results == 33:
        namevalue_results = f""" love, service, and responsibility. It is a time to care, help, and support others. It is also a time to be loyal, compassionate, and generous. You may face challenges with sacrifice, interference, or perfectionism. This number is considered to be very fortunate and beneficial, as it indicates a person who has the assistance and association of those of rank and position and who gains through love and the opposite sex.
        Lucky numbers: Your lucky numbers are 33, 42, 51, and 60. These numbers can bring you love, happiness, and peace.
        How they interact with society: You may have a loving and caring personality, that can make you a humanitarian, a healer, or a teacher. You may also have a loyal and compassionate communication style, that can help you listen and relate to others. You may influence and be influenced by the world around you through your love, service, and responsibility.
        About their friends: You may attract and be attracted to people who are loving, caring, or supportive. You may also have friends who are harmonious, peaceful, or cooperative. You may support and challenge each other to love and heal yourselves and others. You may be compatible with people who understand and appreciate you, and incompatible with people who hurt or ignore you.
        Opportunities and open doors: You may encounter chances and possibilities that allow you to love yourself, serve others, and take responsibility. You may also find opportunities and open doors that help you to find love, happiness, and peace. You may benefit from being loyal, compassionate, and generous.
        Purpose: Your purpose is to be a humanitarian, a healer, and a teacher. You are meant to love yourself and others, heal yourself and others, and teach yourself and others.
        Hidden potential: You may have a hidden potential for care, healing, or education. You may also have a latent talent for arts, music, or beauty. You may enhance your abilities and talents by loving yourself, serving others, and taking responsibility.
        Lessons: Your lessons are to learn boundaries, expression, and acceptance. You need to balance your service and your self-care, your compassion and your assertiveness, and your responsibility and your forgiveness.
        Karmic lessons and challenges: You may have to face and resolve issues and problems that are related to your sacrifice, interference, or perfectionism. You may also have to deal with karmic consequences of your past lives or actions, such as being too sacrificing, interfering, or demanding. You may overcome your challenges by learning boundaries, expression, and acceptance. """

    return namevalue_results


# results for cnc
def cnc_results (cnc):
    if cnc == 2 or cnc == 11:
        cnc_results = f""" partnership, cooperation, and diplomacy. It is a time to seek harmony, balance, and peace in your relationships and situations. It is also a time to be receptive, intuitive, and adaptable. You may face challenges with indecision, sensitivity, or dependence.
        Career: You may work well with others, especially in fields that require teamwork, negotiation, or counseling. You may also have a talent for arts, music, or writing. You may need to be more assertive and confident in your abilities and decisions.
        Marriage and relationship: You may be a loving, loyal, and supportive partner, who values harmony and intimacy. You may also be very sensitive and empathetic to your partner’s needs and emotions. You may need to avoid being too dependent, passive, or submissive in your relationship.
        Financial life: You may have a moderate and balanced approach to money, neither too extravagant nor too frugal. You may also be generous and charitable, willing to share your resources with others. You may need to avoid being too indecisive, insecure, or influenced by others in your financial matters.
        Social life: You may be a friendly, sociable, and diplomatic person, who gets along well with most people. You may also be a good listener, mediator, and peacemaker, who can resolve conflicts and create harmony. You may need to avoid being too shy, timid, or influenced by others in your social interactions.
        Spiritual life: You may have a strong intuition, psychic ability, or connection to the spiritual realm. You may also be interested in learning about different religions, philosophies, or cultures. You may need to avoid being too doubtful, fearful, or confused in your spiritual path.
        Luck and challenges: You may be lucky in finding good partners, friends, or mentors, who can help you in your life. You may also be lucky in having a peaceful and harmonious environment. You may face challenges with making choices, expressing yourself, or standing up for yourself."""
    
    elif cnc == 3 or cnc == 12:
        cnc_results = f""" creativity, joy, and communication. It is a time to express yourself, share your ideas, and have fun. It is also a time to be optimistic, enthusiastic, and sociable. You may face challenges with self-discipline, responsibility, or ego.
        Career: You may excel in fields that require creativity, innovation, or entertainment. You may also have a talent for speaking, writing, or teaching. You may need to be more organized, focused, and committed in your work.
        Marriage and relationship: You may be a fun, lively, and adventurous partner, who enjoys romance and excitement. You may also be a good communicator, who can express your feelings and thoughts clearly. You may need to avoid being too superficial, restless, or unfaithful in your relationship.
        Financial life: You may have a good sense of humor, optimism, and abundance, which can attract money and opportunities. You may also like to spend money on things that make you happy, such as travel, entertainment, or education. You may need to avoid being too careless, wasteful, or extravagant in your financial matters.
        Social life: You may be a popular, outgoing, and charismatic person, who can make friends easily and charm anyone. You may also be a good storyteller, comedian, or performer, who can entertain and inspire others. You may need to avoid being too boastful, arrogant, or insensitive in your social interactions.
        Spiritual life: You may have a joyful, playful, and curious attitude towards spirituality, which can make you explore different paths and possibilities. You may also have a creative, expressive, and inspirational gift, which can help you manifest your dreams and visions. You may need to avoid being too scattered, distracted, or egotistical in your spiritual path.
        Luck and challenges: You may be lucky in finding opportunities, resources, or people that can help you express your creativity and potential. You may also be lucky in having a positive and cheerful outlook on life. You may face challenges with being responsible, disciplined, or humble.
         """

    elif cnc == 4 or cnc == 13:
        cnc_results = f""" stability, order, and practicality. It is a time to build, organize, and work hard. It is also a time to be realistic, reliable, and diligent. You may face challenges with rigidity, limitation, or boredom.
        Career: You may succeed in fields that require structure, discipline, or management. You may also have a talent for engineering, science, or mathematics. You may need to be more flexible, innovative, and open-minded in your work.
        Marriage and relationship: You may be a loyal, dependable, and responsible partner, who values security and stability. You may also be a good provider, protector, and planner, who can take care of your family and home. You may need to avoid being too controlling, demanding, or critical in your relationship.
        Financial life: You may have a conservative and cautious approach to money, saving more than you spend. You may also have a long-term and realistic vision of your financial goals and plans. You may need to avoid being too stingy, fearful, or pessimistic in your financial matters.
        Social life: You may be a honest, trustworthy, and respectful person, who follows the rules and norms of society. You may also be a good friend, colleague, or mentor, who can offer support and advice. You may need to avoid being too serious, dull, or isolated in your social interactions.
        Spiritual life: You may have a strong sense of order, logic, and rationality, which can help you understand the laws and patterns of the universe. You may also have a strong sense of duty, morality, and justice, which can guide your actions and choices. You may need to avoid being too rigid, dogmatic, or judgmental in your spiritual path.
        Luck and challenges: You may be lucky in building a solid foundation, reputation, or legacy in your life. You may also be lucky in having a stable and secure environment. You may face challenges with adapting to change, embracing diversity, or expressing your emotions.
         """

    elif cnc == 5 or cnc == 14:
        cnc_results = f""" change, freedom, and adventure. It is a time to explore, experiment, and experience new things. It is also a time to be flexible, versatile, and curious. You may face challenges with impulsiveness, restlessness, or instability.
        Career: You may thrive in fields that require variety, excitement, or travel. You may also have a talent for sales, marketing, or media. You may need to be more consistent, committed, and focused in your work.
        Marriage and relationship: You may be a passionate, spontaneous, and adventurous partner, who enjoys diversity and novelty. You may also be a good communicator, who can keep your partner interested and engaged. You may need to avoid being too impulsive, irresponsible, or unfaithful in your relationship.
        Financial life: You may have a adventurous and generous approach to money, spending more than you save. You may also have a short-term and optimistic vision of your financial goals and plans. You may need to avoid being too reckless, wasteful, or extravagant in your financial matters.
        Social life: You may be a fun, lively, and charismatic person, who can make friends easily and charm anyone. You may also be a good storyteller, comedian, or performer, who can entertain and inspire others. You may need to avoid being too boastful, arrogant, or insensitive in your social interactions.
        Spiritual life: You may have a adventurous, playful, and curious attitude towards spirituality, which can make you explore different paths and possibilities. You may also have a creative, expressive, and inspirational gift, which can help you manifest your dreams and visions. You may need to avoid being too scattered, distracted, or egotistical in your spiritual path.
        Luck and challenges: You may be lucky in finding opportunities, resources, or people that can help you experience new things and expand your horizons. You may also be lucky in having a positive and cheerful outlook on life. You may face challenges with being responsible, disciplined, or humble.
         """

    elif cnc == 6 or cnc == 15:
        cnc_results = f""" love, service, and responsibility. It is a time to care, help, and support others. It is also a time to be loyal, compassionate, and generous. You may face challenges with sacrifice, interference, or perfectionism.
        Career: You may excel in fields that require care, healing, or education. You may also have a talent for arts, music, or beauty. You may need to be more assertive, confident, and independent in your work.
        Marriage and relationship: You may be a loving, caring, and supportive partner, who values harmony and intimacy. You may also be a good listener, healer, and teacher, who can help your partner grow and heal. You may need to avoid being too sacrificing, interfering, or demanding in your relationship.
        Financial life: You may have a balanced and generous approach to money, neither too extravagant nor too frugal. You may also have a long-term and realistic vision of your financial goals and plans. You may need to avoid being too insecure, fearful, or pessimistic in your financial matters.
        Social life: You may be a friendly, sociable, and diplomatic person, who gets along well with most people. You may also be a good listener, mediator, and peacemaker, who can resolve conflicts and create harmony. You may need to avoid being too shy, timid, or influenced by others in your social interactions.
        Spiritual life: You may have a strong sense of love, compassion, and service, which can help you connect with others and the divine. You may also have a strong sense of duty, morality, and justice, which can guide your actions and choices. You may need to avoid being too rigid, dogmatic, or judgmental in your spiritual path.
        Luck and challenges: You may be lucky in finding love, happiness, and peace in your life. You may also be lucky in having a harmonious and supportive environment. You may face challenges with setting boundaries, expressing your needs, or accepting yourself.
         """

    elif cnc == 7 or cnc == 16:
        cnc_results = f""" wisdom, spirituality, and introspection. It is a time to learn, analyze, and understand yourself and the world. It is also a time to be calm, reflective, and meditative. You may face challenges with isolation, skepticism, or cynicism.
        Career: You may succeed in fields that require research, analysis, or knowledge. You may also have a talent for science, philosophy, or spirituality. You may need to be more social, practical, and cooperative in your work.
        Marriage and relationship: You may be a deep, mysterious, and intriguing partner, who values privacy and intimacy. You may also be a good thinker, seeker, and learner, who can share your insights and discoveries with your partner. You may need to avoid being too distant, secretive, or critical in your relationship.
        Financial life: You may have a moderate and cautious approach to money, saving more than you spend. You may also have a long-term and visionary vision of your financial goals and plans. You may need to avoid being too frugal, fearful, or pessimistic in your financial matters.
        Social life: You may be a reserved, quiet, and independent person, who prefers quality over quantity in your relationships. You may also be a good observer, listener, and advisor, who can offer wisdom and guidance to others. You may need to avoid being too aloof, detached, or arrogant in your social interactions.
        Spiritual life: You may have a strong intuition, psychic ability, or connection to the spiritual realm. You may also be interested in learning about different religions, philosophies, or cultures. You may need to avoid being too doubtful, fearful, or confused in your spiritual path.
        Luck and challenges: You may be lucky in finding knowledge, wisdom, and truth in your life. You may also be lucky in having a peaceful and serene environment. You may face challenges with connecting with others, trusting yourself, or embracing your emotions.
         """

    elif cnc == 8 or cnc == 17:
        cnc_results = f"""  power, success, and abundance. It is a time to achieve, lead, and prosper. It is also a time to be confident, ambitious, and authoritative. You may face challenges with materialism, domination, or greed.
        Career: You may excel in fields that require leadership, management, or business. You may also have a talent for finance, law, or politics. You may need to be more ethical, compassionate, and balanced in your work.
        Marriage and relationship: You may be a powerful, loyal, and generous partner, who values security and stability. You may also be a good provider, protector, and planner, who can take care of your family and home. You may need to avoid being too controlling, demanding, or possessive in your relationship.
        Financial life: You may have a prosperous and abundant approach to money, earning more than you spend. You may also have a short-term and optimistic vision of your financial goals and plans. You may need to avoid being too reckless, wasteful, or extravagant in your financial matters.
        Social life: You may be a confident, outgoing, and charismatic person, who can influence and inspire others. You may also be a good leader, organizer, and achiever, who can accomplish great things. You may need to avoid being too boastful, arrogant, or insensitive in your social interactions.
        Spiritual life: You may have a strong sense of power, authority, and responsibility, which can help you manifest your goals and dreams. You may also have a strong sense of karma, justice, and balance, which can guide your actions and choices. You may need to avoid being too materialistic, domineering, or greedy in your spiritual path.
        Luck and challenges: You may be lucky in finding success, recognition, and wealth in your life. You may also be lucky in having a powerful and influential environment. You may face challenges with being humble, generous, or compassionate.
         """

    elif cnc == 9 or cnc == 18:
        cnc_results = f""" completion, humanitarianism, and transformation. It is a time to finish, release, and let go of what no longer serves you. It is also a time to be compassionate, altruistic, and visionary. You may face challenges with attachment, loss, or resentment.
        Career: You may excel in fields that require service, healing, or education. You may also have a talent for arts, music, or spirituality. You may need to be more practical, realistic, and grounded in your work.
        Marriage and relationship: You may be a compassionate, generous, and supportive partner, who values harmony and intimacy. You may also be a good listener, healer, and teacher, who can help your partner grow and heal. You may need to avoid being too sacrificing, interfering, or demanding in your relationship.
        Financial life: You may have a balanced and generous approach to money, neither too extravagant nor too frugal. You may also have a long-term and visionary vision of your financial goals and plans. You may need to avoid being too insecure, fearful, or pessimistic in your financial matters.
        Social life: You may be a friendly, sociable, and diplomatic person, who gets along well with most people. You may also be a good listener, mediator, and peacemaker, who can resolve conflicts and create harmony. You may need to avoid being too shy, timid, or influenced by others in your social interactions.
        Spiritual life: You may have a strong sense of love, compassion, and service, which can help you connect with others and the divine. You may also have a strong sense of purpose, destiny, and transformation, which can help you fulfill your mission and vision. You may need to avoid being too rigid, dogmatic, or judgmental in your spiritual path.
        Luck and challenges: You may be lucky in finding completion, fulfillment, and peace in your life. You may also be lucky in having a harmonious and supportive environment. You may face challenges with letting go, forgiving, or accepting yourself. """

    return cnc_results

