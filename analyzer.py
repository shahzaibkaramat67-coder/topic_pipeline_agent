from Filnal_prompt import Templater
from model import llm


async def Analyzer(data):

    print(f"this is Analyzer funtion")

    system_prompt = """
You are a professional content analyzer and quality validator.

Your task is to analyze the provided content and determine whether it meets the requirements specified in the input.

RULES:
- Return ONLY a valid JSON object.
- Do not include Markdown, code fences, explanations, or extra text.
- Evaluate the actual content provided; do not confuse the content with the required JSON response format.
- Do not rewrite the content.
- Do not change the original topic.
- Set `Approved` to `true` only when the content meets the requirements.
- If rejected, provide specific, actionable feedback explaining what needs improvement.
- If the input is missing or empty, reject it and explain what is missing.
- The JSON response must contain exactly the keys `Approved` and `Feedback`.

REQUIRED OUTPUT FORMAT:

{{
  "Approved": true,
  "Feedback": ""
}}

OR

{{
  "Approved": false,
  "Feedback": "Explain the specific issue and how to fix it."
}}
    """
    prompt = """
    Analysis of this data  : {data} 
    """
    final_prompt = Templater(system_prompt, prompt)
    result = final_prompt.invoke({"data": data})
    # print("DATA TYPE OF RESULT :", type(result))
    # print("DATA TYPE OF RESULT :", result.to_string())

    response = await llm(result.to_string())
    return response.replace("```json", "").replace("```", "").strip()
