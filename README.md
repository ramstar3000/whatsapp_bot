##What we built
Our system comprises a robust backend powered by Python, hosted as a Linux bot, and a user-friendly frontend developed using Flask. The backend seamlessly interacts with GreenAPI through HTTP requests to access my phone number. Leveraging the language prowess of GPT 3.5 Turbo, our system excels in multiple aspects:

1. Optimal Reminder Times: GPT predicts the ideal times for sending reminders, eliminating the need for manual selection and ensuring maximum effectiveness.

2. Engaging WhatsApp Prompts: The language model generates captivating WhatsApp messages with just minimal event details. For example, from basic information about the event location and name, GPT crafts engaging prompts like:

``` Reminder: Get ready for Cricket Practice at Fenners in just 30 minutes! Remember to bring your A-game and your sense of humor. As a bonus joke for motivation: Why did the cricket team go to the bank? To get their bowlers back! 😉🏏 #GameOn #CricketTime ```

3. User Input Sanitization: GPT assists in sanitizing user inputs to ensure smooth server functionality. We restrict occurrence frequency inputs to a finite set, predicting values from other cases to enhance user experience.

Challenges we ran into

While implementing our solution, we encountered challenges due to token restrictions, leading us to opt for GPT 3.5 Turbo. However, we envision future enhancements by transitioning to GPT 4 and exploring the incorporation of DALL-E for advanced imaging capabilities.

Additionally, we had the issue of time management which I think was overcome by having to remove some features such as posting the website online for public access.

Accomplishments that we're proud of
Our system has already been successfully deployed on pythonanywhere.com and is actively serving its purpose within my cricket group chat for events starting on Mondays.

What we learned
Technical Skill Development:
API Integration Mastery: Successfully integrating and managing multiple APIs within a single project showcases adeptness in handling diverse technological components.

Server Deployment: Deploying the system on pythonanywhere.com demonstrates proficiency in server deployment, a crucial aspect of turning a project into a functional application.

Flask Framework Expertise: Developing the frontend using Flask indicates a deep understanding of web frameworks, contributing to a smoother user experience.

Problem-Solving and Adaptability:
Token Restrictions Mitigation: Overcoming challenges related to token restrictions by strategically selecting GPT 3.5 Turbo reflects adaptability in finding effective solutions within constraints.

Feature Prioritization: The decision to remove certain features due to time constraints highlights effective project management and the ability to prioritize essential functionalities.

User Experience Enhancement:
Engagement-Focused Design: The emphasis on creating engaging WhatsApp prompts shows a user-centric approach, prioritizing not just functionality but also user experience.

Sanitization for Reliability: Implementing user input sanitization ensures a reliable server function, emphasizing the importance of anticipating and addressing potential issues.

Collaboration and Communication:
API Coordination: Managing various APIs concurrently signifies competence in orchestrating different services, showcasing effective collaboration between technologies.

Ethical and Societal Implications:
User Privacy Considerations: Addressing potential privacy concerns related to accessing personal phone numbers through GreenAPI underscores ethical considerations in system design.



Additionally, how to manage many different APIs in one project at the same time which is very powerful.

What's next for Whatsapp Events
Our roadmap includes potential upgrades to GPT 4, exploring the integration of DALL-E for richer imaging experiences, and continuous refinement based on user feedback and emerging technological advancements. We aim to evolve the system to meet the dynamic needs of our users.

Additionally, we could allow multiple users and allow the bot to switch between processes.
