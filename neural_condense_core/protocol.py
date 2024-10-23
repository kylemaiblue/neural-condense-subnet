from bittensor import Synapse
from typing import List


class Metadata(Synapse):
    metadata: dict = {}


class TextCompressProtocol(Synapse):
    r"""
    Protocol for the Text-Compress task.
    Attributes:
    - Seen by miners
        - context (str): The text to be compressed by miners.
        - prompt_after_context (str): The postfix text to be concatenated with the text_to_compress.
    - Output of miners
        - compressed_tokens (List[List[float]]): The compressed tokens generated by the miner.
    - Ground truth seen by validators
        - expected_generation (str): The original generation.
    """

    context: str = ""
    compressed_tokens: List[List[float]] = []
    expected_completion: str = ""

    def get_miner_payload(self):
        r"""
        Get the input for the miner.
        Returns:
        - miner_payload (dict): The input for the miner.
        """
        return {
            "context": self.context,
        }

    def hide_ground_truth(self):
        r"""
        Hide the ground truth from the miner.
        """
        self.expected_completion = ""

    def deserialize(self) -> Synapse:
        return {
            "context": self.context,
            "compressed_tokens": self.compressed_tokens,
            "expected_completion": self.expected_completion,
        }
