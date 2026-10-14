def Json_hendler(data):
    return data.replace("```json", "").replace("```", "").strip()
