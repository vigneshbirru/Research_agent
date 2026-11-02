import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


def get_llm():

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found")

    models = os.getenv(
        "GROQ_MODELS",
        "openai/gpt-oss-20b,openai/gpt-oss-120b,"
        "llama-3.3-70b-versatile,llama-3.1-8b-instant,"
        "qwen/qwen3-32b"
    ).split(",")

    for model in models:

        model = model.strip()

        if not model:
            continue

        llm = ChatGroq(
            model=model,
            temperature=0,
            api_key=api_key,
            max_retries=0,
        )

        try:
            # Test whether the model is working
            llm.invoke("Hi")

            return llm

        except Exception:
            continue

    raise RuntimeError("All Groq models failed")


llm = get_llm()
