def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    res = []
    step = chunk_size - overlap

    for i in range(0, len(tokens), step):
        chunk = tokens[i:i + chunk_size]
        res.append(chunk)

        # Stop once this chunk reaches or exceeds the end
        if i + chunk_size >= len(tokens):
            break

    return res
