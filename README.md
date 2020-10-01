# Scheduler

## Background

The university offers several different sections of the same courses, this causes an enormous amount of combination of different sections.
Having access to every combinations has several benefits: first of all, one can choose the best schedule for their own individual needs (such as not having to wake up too early or the desire to take a particular section).
and it can enable one to act swiftly during the course registration days (for example, if one section is full; the user can quickly select one of the alternative schedules)
Manually generating all possible combinations is very challenging at best and impossible at worst. Thus, I developed this easy-to-use website to make creating course schedules easier for all students.

## How To Use It?

Visit http://coursescheduler.pythonanywhere.com

Enter the courses that you plan to take this term, put a "_" between the course code and course field and use lowercase letters (for example, CS 204 would be cs_204).
Separate each course with a comma (for example if you plan to take Math 201 and CS 204 this term, type math_201,cs_204)
For recitation sections, put a R at the end; for discussion sections, put a D at the end; for lab sessions put a L at the end. For example, due to university rules one would be required to
take CS 204 Lab Session with CS 204, so you should type cs_204,cs_204R if you plan to take CS 204 this term. On another example, if you plan to take HUM 207, CS 204 and Math 201 you should also take Math 201 Recitation (Math 201 requires a recitation section), CS 204 Lab (CS 204 requires a lab section) and HUM 207 Discussion (HUM 207 requires a discussion section) and type cs_204,cs_204L,hum_207,hum_207D,math_201,math_201R.

After you are finished, click on schedule button. Depending on how many different sections are offered by the university this year, next page may load instantly or take couple minutes to load.

Each schedule table is a distinct schedule. You can click on view CRNs button to get example CRN codes for this schedule.

## How Does It Work?

This project was developed using Flask Framework, Bootstrap, Custom CSS and HTML. The data comes from a REST Api that I developed (you can view its code on this github account).

## Future Versions

This is a very early version of this project. The reason why I deployed it early was to catch up with registration period of the university. 
In future, I plan to make the user interface more user friendly by removing specific input rules and make the source code more flexible.
I also plan to add a "report a bug" form that automatically sends an email to my personal email account using SMTP port of gmail.
I plan to tweak the design of the app to make it more appealing.
On top of that, I plan to add a "load more button" to the bottom of the page after 3 schedule alternatives to boost the performance because depending on the courses, it sometimes takes too long to render the Jinja Template.
I also plan to run Bootstrap css and javascript files locally to eliminate a whole category of possible issues.
I also plan to add a message on the top of the page if the user selects a class that does not have meeting hour.
