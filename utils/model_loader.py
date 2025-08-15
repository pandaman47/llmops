import os
from pydantic import BaseModel, Field
from typing import Literal, Optional, Any
from dotenv import load_dotenv
from utils.config_loader import load_config
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

load_dotenv()

class ConfigLoader:
    def __init__(self):
        self.config = load_config()

    def __getitem__(self, key):
        return self.config[key]


class ModelLoader(BaseModel):
    model_provider: Literal["openai","groq"] = "groq"
    config: Optional[ConfigLoader] = Field(default=None, exclude=True)

    def model_post_init(self, context:Any) -> None:
        self.config = ConfigLoader()

    class Config:
        arbitrary_types_allowed = True  ##If you want to use custom classes or types that Pydantic does not recognize

    def load_llm(self):
        """
        Load and return the llm model
        """
        print("Loading LLM..")
        print(f"Loading model from model provider: {self.model_provider}")
        print(type(self.config)) 
        if self.model_provider == "groq":
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config["llm"]["groq"]["model_name"]
            print(model_name)
            llm=ChatGroq(model= model_name, api_key=groq_api_key)
        elif self.model_provider == "openai":
            openai_api_key = os.getenv("OPENAI_API_KEY")
            model_name = self.config["llm"]["openai"]["model_name"]
            llm=ChatOpenAI(model= model_name, api_key=openai_api_key)

        return llm
    
if __name__ == "__main__":
    model_loader = ModelLoader(model_provider="groq")
    llm=model_loader.load_llm()
    print(f"LLM loaded: {llm}")
    


