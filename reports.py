import re
import operator


def count_games(file_name):
    """Count games in the file

    Args:
        file_name: file from which the program reads data
    Returns:
        number: how many games are in the file
    """
    with open(file_name) as f:
        data = f.readlines()
    return len(data)


def decide(file_name, year):
    """Decide if there is a game for a given name in the file

    Args:
        file_name: file from which the program reads data
        year: year of the game
    Returns:
        boolean value: is the game for a given year in the file?
    """
    with open(file_name) as f:
        data = f.readlines()
    games_list = [re.split(r'\t+', line.rstrip('\n')) for line in data]
    years = [line[2] for line in games_list]
    years_numbers = [int(year) for year in years]
    if year in years or year in years_numbers:
        return True
    else:
        return False


def get_latest(file_name):
    """Get lastest game title from a file

    Args:
        file_name: file from which the program reads data
    Returns:
        string: the title of the latest game
    """
    with open(file_name) as f:
        data = f.readlines()
    games_list = [re.split(r'\t+', line.rstrip('\n')) for line in data]
    years = [line[2] for line in games_list]
    index, value = max(enumerate(years), key=operator.itemgetter(1))
    return games_list[index][0]


def count_by_genre(file_name, genre):
    """Count games by genre without duplicates

    Args:
        file_name: file from which the program reads data
        genre: genre of the game
    Returns:
        number: how many games do we have by genre
    """
    with open(file_name) as f:
        data = f.readlines()
    games_list = [re.split(r'\t+', line.rstrip('\n')) for line in data]
    genres = [line[3] for line in games_list]
    return genres.count(genre)


def get_line_number_by_title(file_name, title):
    """Get line number for given title

    Args:
        file_name: file from which the program reads data
        title: title of the game
    Returns:
        number: line number of the game with a given title
    """
    with open(file_name) as f:
        data = f.readlines()
    games_list = [re.split(r'\t+', line.rstrip('\n')) for line in data]
    titles = [line[0] for line in games_list]
    try:
        number = titles.index(title) + 1
        return number
    except IndexError:
        raise ValueError


def sort_abc(file_name):
    """Sort the game titles alphabetically

    Args:
        file_name: file from which the program reads data
    Returns:
        sorted_titles: list of sorted titles
    """
    with open(file_name) as f:
        data = f.readlines()
    games_list = [re.split(r'\t+', line.rstrip('\n')) for line in data]
    titles = [line[0] for line in games_list]
    sorted_titles = []
    while len(sorted_titles) < len(games_list):
        lowest = 'z'
        for i in titles:
            if i < lowest:
                lowest = i
        sorted_titles.append(lowest)
        titles.remove(lowest)
    return sorted_titles


def get_genres(file_name):
    """Get the list of sorted genres without duplicates

    Args:
        file_name: file from which the program reads data
    Returns:
        list: list of sorted genres without duplicates
    """
    with open(file_name) as f:
        data = f.readlines()
    games_list = [re.split(r'\t+', line.rstrip('\n')) for line in data]
    genres = [line[3] for line in games_list]
    return sorted(set(genres), key=str.lower)


def when_was_top_sold_fps(file_name):
    """When was the top sold fps game

    Args:
        file_name: file from which the program reads data
    Returns:
        number: year of the top sold fps game as integer
    """
    with open(file_name) as f:
        data = f.readlines()
    games_list = [re.split(r'\t+', line.rstrip('\n')) for line in data]
    fps_list = [games_list[i] for i in range(len(games_list)) if 'First-person shooter' in games_list[i]]
    if not fps_list:
        raise ValueError
    copies_sold = [line[1] for line in fps_list]
    index, value = max(enumerate([float(x) for x in copies_sold]), key=operator.itemgetter(1))
    return int(fps_list[index][2])
