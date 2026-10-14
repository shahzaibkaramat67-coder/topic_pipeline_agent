# # from langchain_google_genai import ChatGoogleGenerativeAI
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()


base_url = os.getenv("FREELLMAPI_BASE_URL")
model_name = os.getenv("FREELLMAPI_MODEL")
API_KEY = os.getenv("FREELLMAPI_API_KEY")

print("BASE URL:", base_url)
print("MODEL:", model_name)
print("API KEY EXISTS:", bool(API_KEY))

client = AsyncOpenAI(base_url=base_url, api_key=API_KEY)


async def llm(prompt):
    response = await client.chat.completions.create(
        model=model_name, messages=[{"role": "user", "content": prompt}]
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content


# import asyncio
# from openai import AsyncOpenAI

# client = AsyncOpenAI(base_url="http://127.0.0.1:31415/v1", api_key=API_KEY)


# async def test():

#     response = await client.chat.completions.create(
#         model="glm-4.5-flash", messages=[{"role": "user", "content": "Hello"}]
#     )

#     print(response.choices[0].message.content)


# asyncio.run(test())


# async def llm(prompt):
#     llm = ChatGoogleGenerativeAI(
#         model=os.getenv("GEMINI_API_MODEL_FLASH"),
#     )
#     response = await llm.ainvoke(prompt)
#     return response.content
