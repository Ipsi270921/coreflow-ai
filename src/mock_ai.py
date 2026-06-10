import json
import time

def process_issue_with_mock_ai(raw_text):
    """
    Simulates a high-end AI processing model. 
    It reads the user text locally, determines priority and category,
    and returns a clean, structured python dictionary.
    """
    print("[MOCK AI] Ingesting raw log data...")
    time.sleep(0.8) # Simulates network latency (makes it feel real!)
    
    # Standardizing text to lowercase for simple pattern matching
    clean_text = raw_text.lower()
    
    # 1. Logic Layer: Determine the Category
    if "broken" in clean_text or "error" in clean_text or "crash" in clean_text or "fail" in clean_text:
        assigned_category = "Bug"
    elif "feature" in clean_text or "add" in clean_text or "want" in clean_text or "button" in clean_text:
        assigned_category = "Feature Request"
    elif "color" in clean_text or "font" in clean_text or "layout" in clean_text or "ui" in clean_text:
        assigned_category = "UI Change"
    else:
        assigned_category = "Task"
        
    # 2. Logic Layer: Determine the Priority Level
    if "asap" in clean_text or "money" in clean_text or "urgent" in clean_text or "losing" in clean_text:
        calculated_priority = "Critical"
    elif "broken" in clean_text or "error" in clean_text:
        calculated_priority = "High"
    elif "want" in clean_text or "add" in clean_text:
        calculated_priority = "Medium"
    else:
        calculated_priority = "Low"
        
    # 3. Logic Layer: Generate a clean, structured 1-sentence summary
    words = raw_text.split()
    short_preview = " ".join(words[:6]) + "..." if len(words) > 6 else raw_text
    clean_summary = f"Automated triage for: {short_preview}"
    
    # Construct the final structured dictionary matching our database expectations
    structured_response = {
        "category": assigned_category,
        "priority": calculated_priority,
        "summary": clean_summary
    }
    
    print("[MOCK AI SUCCESS] Processing complete.")
    return structured_response

# Safe sandbox runner to verify this module works independently
if __name__ == "__main__":
    test_message = "CRITICAL: The payment page fails every time a user clicks submit. We are losing money!"
    result = process_issue_with_mock_ai(test_message)
    print("\nResulting Dictionary Structure:")
    print(json.dumps(result, indent=4))