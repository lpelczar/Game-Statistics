# Print all the returns from functions in reports.py in a pretty way
import reports


def print_count_games(file_name):
    count = reports.count_games(file_name)
    print('There are %d games in the file' % count)
    print('')


def print_decide(file_name, year):
    decide = reports.decide(file_name, year)
    if decide:
        print('There is a game from', year, 'in the file')
    else:
        print('There is no game from', year, 'in the file')
    print('')


def print_get_latest(file_name):
    title = reports.get_latest(file_name)
    print('Lastest game title is', title)
    print('')


def print_count_by_genre(file_name, genre):
    genres = reports.count_by_genre(file_name, genre)
    print('There is a', genres, 'games of', genre, 'genre in the file')
    print('')


def print_get_line_number_by_title(file_name, title):
    line = reports.get_line_number_by_title(file_name, title)
    print('Game with title', title, 'is on line', line)
    print('')


def print_sort_abc(file_name):
    sorted_titles = reports.sort_abc(file_name)
    print('Sorted games:')
    for i in sorted_titles:
        print(i)
    print('')


def print_get_genres(file_name):
    genres = reports.get_genres(file_name)
    print('List of sorted genres:')
    for i in genres:
        print(i)
    print('')


def print_when_was_top_sold_fps(file_name):
    year = reports.when_was_top_sold_fps(file_name)
    print('Top sold FPS was from', year)


def main():
    print_count_games('game_stat.txt')
    print_decide('game_stat.txt', 1999)
    print_get_latest('game_stat.txt')
    print_count_by_genre('game_stat.txt', 'RPG')
    print_get_line_number_by_title('game_stat.txt', 'Terraria')
    print_sort_abc('game_stat.txt')
    print_get_genres('game_stat.txt')
    print_when_was_top_sold_fps('game_stat.txt')


if __name__ == '__main__':
    main()
