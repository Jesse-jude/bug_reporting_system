import random
def assign_developer (report_text, classification):

    #Define a mapping of classification to developers expertise
    developer_expertise = {"frontend":["developer@example.com", "developer2@gmail.com"],
                          "backend":["developer3@example.com", "developer4@example.com"],
                          "security":["security_team@example.com",]}
    
    #extract keywords from the report text (using libs like NLTK)
    keyboard = extract_keywords(report_text)

    #Finding matching expertise based on classification and keywords
    assign_developer = None
    for expertise, developers in developer_expertise.item():
        if classification["type"] == expertise and any(keyword in keyword for keyword in expertise):
            assign_developer = random.choice(developers)
            break #stop searching after a match is found
        return assign_developer
   #helper function to extract keywords (implementation omitted for brevity) 
def extract_keywords(text):
    #(use NLTK or other libs to extract keywords from text)
    pass

