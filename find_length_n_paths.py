def _helper_find_paths_word(n, word_index, path, valid_paths, word):
    if 'QU' in word and word_index == len(word) - 1:
        if is_valid_path(board, path, word) and len(path) == n:
            valid_paths.add(tuple(path))
        return valid_paths
    if word_index == len(word):
        if is_valid_path(board, path, word) and len(path) == n:
            valid_paths.add(tuple(path))
        return valid_paths
    row, col = path[-1]
    lst_neighbors = _helper_to_find_neighbors(row, col, board)
    for cell in lst_neighbors:
        _helper_find_paths_word(n, word_index + 1, path + [(cell[0], cell[1])],
                                        valid_paths, word)
    return valid_paths


def find_paths_for_word(n, board, word):
    valid_paths = set()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == word[0] or board[row][col] == 'QU':
                valid_paths = _helper_find_paths_word(n, 1, [(row, col)], valid_paths, word)
    lst_path = list(valid_paths)
    return lst_path


def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    lst_paths = []
    for word in words:
        paths = find_paths_for_word(n, board, word)
        for path in paths:
            lst_paths.append(path)
    return lst_paths

