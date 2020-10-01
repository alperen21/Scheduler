# Scheduler

##Background

The university offers several different sections of the same courses, this causes an enormous amount of combination of different sections.
Having access to every combinations has several benefits: first of all, one can choose the best schedule for their own individual needs (such as not having to wake up too early or the desire to take a particular section).
and it can enable one to act swiftly during the course registration days (for example, if one section is full; the user can quickly select one of the alternative schedules)
Manually generating all possible combinations is very challenging at best and impossible at worst. Thus, I developed this easy-to-use website to make creating course schedules easier for all students.

##How Does It Work?

Visit http://coursescheduler.pythonanywhere.com
Enter the courses that you plan to take this term, put a "_" between the course code and course field and use lowercase letters (for example, CS 204 would be cs_204).
Separate each course with a comma (for example if you plan to take Math 201 and CS 204 this term, type math_201,cs_204)
For recitation sections, put a R at the end; for discussion sections, put a D at the end; for lab sessions put a L at the end. (for example, due to university rules one would be required to
take CS 204 Lab Session with CS 204, so you should type cs_204,cs_204R if you plan to take CS 204 this term).
