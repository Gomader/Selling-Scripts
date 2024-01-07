from blue_ocean_words_processing.read_raw_files import read_raw_files
from blue_ocean_words_processing.related_words_processing import run as process
from blue_ocean_words_processing.save_result import save_result


def main():
    raw_data = read_raw_files()
    data = process(raw_data=raw_data)
    save_result(data=data)


if __name__ == '__main__':
    main()
