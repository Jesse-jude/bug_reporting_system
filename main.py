from .utils import preprocess_text, classify_report, assign_developer

def process_report(report_text):
    #preprocess the text
    preprocessed_text = preprocess_text(report_text)

    #Classify the report
    classification = classify_report (preprocessed_text)

    #Assign a developer
    assigned_developer = assign_developer(preprocessed_text, classification)

    #return the processed report information
    return{
        "text": preprocessed_text,
        "classification": classification,
        "assigned_developer": assigned_developer
    }

#Example usage (assuming this file is outside the django app)
if __name__ == "__main__":
    report_text = "The website is not loading properly on Chrome"
    processed_report = process_report(report_text)
    print(f"preprocessed text: {processed_report['text']}")
    print(f"classification: {processed_report['classification']['type']}")
    print(f"assigned developer: {processed_report['assigned_developer']}")