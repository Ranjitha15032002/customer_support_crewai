from crewai import Agent
from langchain_openai import ChatOpenAI
from crewai_tools import (
    FileReadTool,
    DirectoryReadTool,
    SerperDevTool,
    WebsiteSearchTool
)

class CustomAgents:
    def _init_(self):
        #self.gpt_model = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.search_tool = SerperDevTool()
        self.web_tool = WebsiteSearchTool()
        self.knowledge_base_tool = DirectoryReadTool(directory='./knowledge_base')
        self.file_tool = FileReadTool()


    def create_agent(self, role):
        descriptions = {
            "Query Analyzer": "I specialize in analyzing user queries and identifying the core issue.",
            "Problem Solver": "I provide detailed solutions to user queries based on the analysis."
        }
        tools = {
            "Query Analyzer": [self.search_tool, self.web_tool],
            "Problem Solver": [self.knowledge_base_tool, self.file_tool]
        }

        return Agent(
            role=role,
            backstory=descriptions[role],
            goal=f"Efficiently handle {role} tasks to improve customer satisfaction.",
            tools=tools[role],
            verbose=True,
            #llm=self.gpt_model
        )
