import reports


def export(export_file, input_file):
    """Export all the returns from functions in reports.py line by line to a file.

    Args:
        export_file: file to which program exports the data
        input_file: file from which program reads the data
    Returns:
        None
    """
    with open(export_file, 'w') as f:
        f.write(str(reports.count_games(input_file)) + '\n')
        f.write(str(reports.decide(input_file, 1999)) + '\n')
        f.write(reports.get_latest(input_file) + '\n')
        f.write(str(reports.count_by_genre(input_file, 'RPG')) + '\n')
        f.write(str(reports.get_line_number_by_title(input_file, 'Terraria')) + '\n')
        for i in reports.sort_abc(input_file):
            f.write(i + ' ')
        f.write('\n')
        for i in reports.get_genres(input_file):
            f.write(i + ' ')
        f.write('\n')
        f.write((str(reports.when_was_top_sold_fps(input_file))))


def main():
    export('export.txt', 'game_stat.txt')


if __name__ == '__main__':
    main()
