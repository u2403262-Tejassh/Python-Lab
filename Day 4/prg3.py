def search_courses(course_list : list, topic : str, skill_lvl : int) -> tuple:
    best_course = tuple()
    for course in course_list:
        if course[1] == topic and course[2] <= skill_lvl:
            if len(best_course) == 0:
                    best_course = course
            elif course[2] > best_course[2]:
                    best_course = course
            elif course[2] > best_course[2] and course[3] > best_course[3]:
                    best_course = course
    return best_course

Courses = [("Intro to Unity","Game Devlopment",1,8),
           ("Intro to Unreal Engine","Game Development",2,7),
           ("Intro to Godot","Game Development", 1,9),
           ("Unity Advanced","Game Developement",3,6),
           ("Unreal Engine Advanced","Game Development",4,9),
           ("Intro to Machine learning","AI&ML",2,8),
           ("Neural Networks","AI&ML",3,7),
           ("Natural Language Processing","AI&ML",4,8)]

topic_num = int(input("Topics:\n'1' for Game Development\n'2' AI&ML\nEnter number: "))
if topic_num  == 1:
    topic  = "Game Development"
else:
    topic = "AI&ML"
skill = int(input("\nSkill level:\n'1' - Beginner\n'2' - Intermediate\n'3' - Advanced\n'4' - Expert\nEnter Skill level: "))
best_course = search_courses(Courses, topic, skill)
if len(best_course) == 0:
    print("\nNo courses available for current skill level, improve skill level")
else:
    print(f"\nCourse: {best_course[0]}\nTopic: {best_course[1]}\nDifficulty: {best_course[2]}\nRating: {best_course[3]}")
