import os
import pandas as pd
from llm_generator.transform_generator import TransformGenerator


def main():
    # Load sample data
    df = pd.read_csv('sample_data.csv')

    # Initialize transform generator
    api_key = os.getenv('OPENAI_API_KEY')
    generator = TransformGenerator(api_key)

    # User query
    query = "Show me high-performing employees over 40 with salaries above $80,000"

    # Generate and apply transforms
    transforms = generator.generate_transforms(query, df)

    # Apply transforms sequentially
    for transform in transforms:
        df = transform.apply(df)

    print(df)


if __name__ == '__main__':
    main()