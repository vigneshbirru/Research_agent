from typing_extensions import NotRequired, TypedDict, Annotated
from typing import List, Optional
from langgraph.graph import MessagesState
from .objects import Analyst
import operator

class GenerateAnalystsState(TypedDict):
    topic: str # research topic
    max_analysts: int # Number of analysts
    human_analyst_feedback: NotRequired[Optional[str]] # Human feedback for  what is generated
    analysts: NotRequired[List[Analyst]] #  List  of all our Analysts
    
class InterviewState(MessagesState):
    max_num_turns: int # Number turns of conversation
    context: Annotated[list, operator.add] # Source docs
    analyst: Analyst # Analyst asking questions
    interview: str # Interview transcript
    sections: list # Final key we duplicate in outer state for Send() API
    
class ResearchGraphState(TypedDict):
    topic: str # research topic
    max_analysts: int # Number of analysts
    human_analyst_feedback: NotRequired[Optional[str]] # Human feeback
    analysts: List[Analyst] #Analyst asking question
    sections: Annotated[list,operator.add] # send() API key
    introduction: str #Interduction for  the final report
    content: str # Content for the final report
    conclusion: str #conclusion for the final report
    final_report: str # Final report