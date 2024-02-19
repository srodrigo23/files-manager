

from whatsapp import FilesManager
from directories import create_directory

path1 = "/Users/sergiorodrigo/Desktop/saved/WhatsApp/WhatsApp Voice Notes"
path2 = "/Users/sergiorodrigo/Desktop/saved/WhatsApp"

path3 = "/Users/sergiorodrigo/Desktop/saved"
path4 = '/Users/sergiorodrigo/Downloads/VOICE_NOTES'

result_path = '/Users/sergiorodrigo/Downloads/VOICE_NOTES/results'

fm = FilesManager()
fm.iterate_directory_to_save_file_names(path4)

# fm.print_report()
years, months =  fm.sort_audio_files()
create_directory(root_path=result_path, months=months, years=years)
