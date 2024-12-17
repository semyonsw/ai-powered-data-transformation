def validate_transforms(transforms_json, df):
    """
    Validate and convert JSON transforms to transform objects
    """
    validated_transforms = []
    for transform in transforms_json.get('transforms', []):
        if transform['type'] == 'column_select':
            validated_transforms.append(
                ColumnSelector(transform['columns'])
            )
        elif transform['type'] == 'filter':
            validated_transforms.append(
                FilterTransform(transform['condition'])
            )
        # Add more transform type validations

    return validated_transforms