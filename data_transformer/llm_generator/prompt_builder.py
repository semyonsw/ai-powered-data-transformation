def build_transform_prompt(user_query: str, df) -> str:
    """
    Build a structured prompt for transform generation

    Returns a prompt that encourages JSON output with transform details
    """
    columns = ", ".join(df.columns)
    return f"""
    Generate a JSON sequence of data transformations for the following query:
    '{user_query}'

    Available columns: {columns}

    Respond with a JSON object with a 'transforms' key containing 
    a list of transforms. Each transform must have:
    - 'type': 'column_select', 'filter', or 'aggregate'
    - Specific parameters for each type

    Example:
    {{
        "transforms": [
            {{
                "type": "filter",
                "condition": "age > 30"
            }},
            {{
                "type": "column_select",
                "columns": ["name", "salary"]
            }}
        ]
    }}
    """
