# StyleQuiz
A set of 3 quizzes to give you some style inspiration if you're stuck in a fashion rut.

Disclaimer: 
		I realize that most people who want to take a fashion quiz are not going to be using a command-line tool to do so. I built this project because I wanted to see if it was something I could do exclusively in Python and now that I've built it, I could see a similar format being translatable into other internal business needs. Just change the questions and the output to suit the intended use case!

Quick Start: 
		If you're already familiar with style systems and you'd like to get started right away, just clone this repo, type python style_quiz.py into your terminal, and answer the questions as they come! If you'd like more information on what you can expect to see in the quiz and why I built it, read on.

The Story: 
		A few years ago, I learned about building capsule wardrobes in order to solve the problem of wanting to dress well while also wanting to live more simply and sustainably. There are so many clothing choices out there these days, how do you know that you're selecting something that makes you feel the most like yourself? How do you choose the kind of clothing you'll want to wear over and over again? I wanted to take some of the decision fatigue out of shopping and to be very intentional when selecting items to add to my closet. That's when I discovered David Kibbe's system of image IDs, which naturally led me to other stylists who have iterated upon his work.

  This particular set of quizzes is based on the work of Ellie-Jean Royden, YouTube content creator and author of How to Dress Your Best. I've simplified her style system a bit so that it can be boiled down into a fashion-magazine-style quiz, but there's plenty more to learn on her channel about how it works: https://www.youtube.com/@elliejeanroyden. There are 3 quizzes you can take and each will give you a link to one of her Pinterest boards with style inspiration based on your results:

  1. The Body Matrix Quiz:
			The idea here is that we all have different shapes in our frame and clothing should work with your body type, not against it. Each of us is a combination of 3 main features that need to be considered when selecting clothing: width (wide or narrow), vertical (long or short), and curve (straight or round). Note, these features have nothing to do with size or weight. They're about your proportions within yourself and how clothes fall on you. Larger bodies are not automatically wide or round and smaller bodies are not automatically narrow or straight in this system. Likewise, there are short people who tend to appear taller than they really are in pictures and vice versa.

  2. The Color Season Quiz:
			This quiz is based on the theory that different colors in your features correspond to different "seasons", or families, of colors. You might be familiar with this concept if you (or maybe your mom or grandma) have ever heard of the book Color Me Beautiful by Carole Jackson. Once you know your season, you can select colors in your clothing that complement the colors in your features. You'll be asked questions about warm or cool tones, the lightness and darkness of those shades, and their amount of softness or brightness. Another good resource if you'd like a deep dive on color is Color Your Style by David Zyla.

  3. The Style Roots Quiz:
			An original concept by Ellie-Jean as far as I know, though these somewhat correspond to what are called "essences" in other systems. Each of the style roots are meant to evoke a certain "vibe" about the clothing you wear. For example, clothing with a flower style root might be described as delicate, airy, or intricate. She suggests combining three of them to form a cohesive look with an outfit. The fun difference between this quiz and the other two is that it doesn't matter what your features are. You get to choose whatever you happen to like!

Thoughts for future iterations of this project:
		In this first attempt, I have made the assumption that all of my users are smart people who will only enter values that make sense in order to get their results. I am aware that people make mistakes and that there needs to be a plan in place for that. In my very next commits to this project, I will be adding some checks for valid input and return a helpful error message if something isn't right.
		I'd like to try building this same project to present it in a way that a user of a fashion quiz would typically want to see. It needs an aesthetically pleasing frontend user interface. I would probably choose to build it in just HTML, CSS, and JavaScript, unless I wanted users to be able to save their information and results, in which case a full-stack application would be a better choice. 
