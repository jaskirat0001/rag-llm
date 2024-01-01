# from dotenv import load_dotenv
# import os
# from llm_app.model_wrappers import OpenAIEmbeddingModel, OpenAIChatGPTModel #used to capture semantic similarity between two or more texts and OpenAIChatGPTModel is used for organising and summarizing the text and to write the new text

# load_dotenv()


# embedder_locator = os.environ.get("EMBEDDER_LOCATOR", "text-embedding-ada-002")
# api_key = os.environ.get("OPENAI_API_TOKEN", "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")
# model_locator = os.environ.get("MODEL_LOCATOR", "gpt-3.5-turbo")
# max_tokens = int(os.environ.get("MAX_TOKENS", 200))
# temperature = float(os.environ.get("TEMPERATURE", 0.0))


# def openai_embedder(data):
#     embedder = OpenAIEmbeddingModel(api_key=api_key)

#     return embedder.apply(text=data, locator=embedder_locator)


# def openai_chat_completion(prompt):
#     model = OpenAIChatGPTModel(api_key=api_key)

#     return model.apply(
#             prompt,
#             locator=model_locator,
#             temperature=temperature,
#             max_tokens=max_tokens,
#         )
from dotenv import load_dotenv
import os
from llm_app.model_wrappers import OpenAIEmbeddingModel, OpenAIChatGPTModel

load_dotenv()

embedder_locator = os.environ.get("EMBEDDER_LOCATOR", "text-embedding-ada-002")
api_key = os.environ.get("OPENAI_API_TOKEN", "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")
model_locator = os.environ.get("MODEL_LOCATOR", "gpt-3.5-turbo")
max_tokens = int(os.environ.get("MAX_TOKENS", 200))
temperature = float(os.environ.get("TEMPERATURE", 0.0))


def openai_embedder(flight_data):
    embedder = OpenAIEmbeddingModel(api_key=api_key)

    # Assuming you have appropriate fields in flight_data, modify this accordingly
    text_to_embed = f"Flight Details: {flight_data['source']} to {flight_data['destination']}, Date: {flight_data['date']}, etc."

    return embedder.apply(text=text_to_embed, locator=embedder_locator)


def openai_chat_completion(prompt):
    model = OpenAIChatGPTModel(api_key=api_key)

    return model.apply(
        prompt,
        locator=model_locator,
        temperature=temperature,
        max_tokens=max_tokens,
    )
