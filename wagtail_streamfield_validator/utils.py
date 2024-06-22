from wagtail.blocks import ListBlock, StreamBlock, StructBlock


def map_block_def(block_def, **kwargs):
    """
    Maps the value of a block.

    Args:
        block_value:
            The value of the block. This would be a list or dict of children for structural blocks.
        block_def:
            The definition of the block.
        block_path:
            A '.' separated list of names of the blocks from the current block (not included) to
            the nested block of which the value will be passed to the operation.
        operation:
            An Operation class instance (extends `BaseBlockOperation`), which has an `apply` method
            for mapping values.

    Returns:
        mapped_value:
    """

    # Depending on whether the block is a ListBlock, StructBlock or StreamBlock we call a
    # different function to alter its children.

    result = {
        "definition": block_def,
    }
    if isinstance(block_def, StreamBlock):
        result["children"] = map_stream_block_value(
            block_def=block_def,
            **kwargs,
        )

    elif isinstance(block_def, ListBlock):
        result["children"] = map_list_block_value(
            block_def=block_def,
            **kwargs,
        )

    elif isinstance(block_def, StructBlock):
        result["children"] = map_struct_block_value(
            block_def=block_def,
            **kwargs,
        )
    return result


def map_stream_block_value(block_def, **kwargs):
    """
    Maps each child block in a StreamBlock value.

    Args:
        stream_block_value:
            The value of the StreamBlock, a list of child blocks
        block_def:
            The definition of the StreamBlock
        block_path:
            A '.' separated list of names of the blocks from the current block (not included) to
            the nested block of which the value will be passed to the operation.

    Returns
        mapped_value:
            The value of the StreamBlock after mapping all the children.
    """

    mapped_value = {}
    for child_block_name, child_block_def in block_def.child_blocks.items():
        mapped_child_value = map_block_def(
            block_def=child_block_def,
            **kwargs,
        )
        mapped_value[child_block_name] = mapped_child_value

    return mapped_value


def map_struct_block_value(block_def, **kwargs):
    """
    Maps each child block in a StructBlock value.

    Args:
        stream_block_value:
            The value of the StructBlock, a dict of child blocks
        block_def:
            The definition of the StructBlock
        block_path:
            A '.' separated list of names of the blocks from the current block (not included) to
            the nested block of which the value will be passed to the operation.

    Returns
        mapped_value:
            The value of the StructBlock after mapping all the children.
    """

    mapped_value = {}
    for child_block_name, child_block_def in block_def.child_blocks.items():
        altered_child_value = map_block_def(
            block_def=child_block_def,
            **kwargs,
        )
        mapped_value[child_block_name] = altered_child_value

    return mapped_value


def map_list_block_value(block_def, **kwargs):
    """
    Maps each child block in a ListBlock value.

    Args:
        stream_block_value:
            The value of the ListBlock, a list of child blocks
        block_def:
            The definition of the ListBlock
        block_path:
            A '.' separated list of names of the blocks from the current block (not included) to
            the nested block of which the value will be passed to the operation.

    Returns
        mapped_value:
            The value of the ListBlock after mapping all the children.
    """

    mapped_value = []
    mapped_child_value = map_block_def(
        block_def=block_def.child_block,
        **kwargs,
    )

    mapped_value.append({"name": block_def.name, "value": mapped_child_value})

    return mapped_value
