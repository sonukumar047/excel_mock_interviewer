from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseAgent(ABC):
    """
    Abstract base class for all conversational agents.
    Defines a common interface for agent behavior.
    """
    @abstractmethod
    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes the agent's logic.
        :param input_data: A dictionary of input data required by the agent.
        :return: A dictionary of results from the agent's operation.
        """
        pass
