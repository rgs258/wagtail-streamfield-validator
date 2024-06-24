from wagtail.blocks import ListBlock, StreamBlock, StructBlock


def map_block_def(block_def, **kwargs):
    """
    Maps a block definition to a dictionary containing the definition and the mapped
    children.
    :param block_def: the block definition to map. This may be a StreamField,
        StreamBlock, ListBlock or StructBlock .
    :param kwargs: additional keyword arguments to pass to the mapping functions.
    :return: a dictionary containing the block definition and the mapped children.
    """

    # Depending on whether the block is a ListBlock, StructBlock or StreamBlock, call a
    # different function to map its children.
    result = {
        "definition": block_def,
    }
    if isinstance(block_def, StreamBlock):
        result["children"] = map_stream_block_def(
            block_def=block_def,
            **kwargs,
        )

    elif isinstance(block_def, StructBlock):
        result["children"] = map_struct_block_def(
            block_def=block_def,
            **kwargs,
        )

    elif isinstance(block_def, ListBlock):
        result["children"] = map_list_block_def(
            block_def=block_def,
            **kwargs,
        )

    return result


def map_stream_block_def(block_def, **kwargs):
    """
    Maps each child block in a StreamBlock.
    :param block_def: the StreamBlock definition to map.
    :param kwargs: additional keyword arguments to pass to the mapping functions.
    :return: a dictionary containing the mapped children.
    """

    mapped_value = {}
    for child_block_name, child_block_def in block_def.child_blocks.items():
        mapped_child_value = map_block_def(
            block_def=child_block_def,
            **kwargs,
        )
        mapped_value[child_block_name] = mapped_child_value

    return mapped_value


def map_struct_block_def(block_def, **kwargs):
    """
    Maps each child block in a StructBlock.
    :param block_def: the StructBlock definition to map.
    :param kwargs: additional keyword arguments to pass to the mapping functions.
    :return: a dictionary containing the mapped children.
    """

    mapped_value = {}
    for child_block_name, child_block_def in block_def.child_blocks.items():
        altered_child_value = map_block_def(
            block_def=child_block_def,
            **kwargs,
        )
        mapped_value[child_block_name] = altered_child_value

    return mapped_value


def map_list_block_def(block_def, **kwargs):
    """
    Maps each child block in a ListBlock.
    :param block_def: the ListBlock definition to map.
    :param kwargs: additional keyword arguments to pass to the mapping functions.
    :return: a list containing the mapped children.
    """

    mapped_value = []
    mapped_child_value = map_block_def(
        block_def=block_def.child_block,
        **kwargs,
    )
    mapped_value.append({"name": block_def.name, "value": mapped_child_value})

    return mapped_value
