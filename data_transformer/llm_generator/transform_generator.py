import json
from typing import List
from openai import OpenAI
from .prompt_builder import build_transform_prompt
from .validator import validate_transforms
from ..transforms import ColumnSelector, FilterTransform, AggregationTransform


class TransformGenerator:
    def __init__(self, api_key):
        """
        Initialize LLM-based transform generator

        Args:
            api_key (str): OpenAI API key
        """
        self.client = OpenAI(api_key=api_key)

    def generate_transforms(self, user_query: str, df) -> List[BaseTransform]:
        """
        Generate a sequence of transforms based on user query

        Args:
            user_query (str): Natural language description of desired transformations
            df (pd.DataFrame): Input DataFrame for context

        Returns:
            List of transform objects
        """
        # Build structured prompt
        prompt = build_transform_prompt(user_query, df)

        # Query LLM
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": "You are a data transformation expert."},
                {"role": "user", "content": prompt}
            ]
        )

        # Parse response
        transforms_json = json.loads(response.choices[0].message.content)

        # Validate and convert to transform objects
        return validate_transforms(transforms_json, df)