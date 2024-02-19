import os
from os import DirEntry
from datetime import datetime

class FileType:
    audio = "AUDIO"
    video = "VIDEO"
    image = "IMAGE"


class MediaFile:
    
    def __init__(self, data_entry:DirEntry, file_format:str, file_type:str) ->None:
        self.file_path = data_entry.path
        self.file_name = data_entry.name
        self.file_format = file_format
        self.file_type = file_type
        self.size = data_entry.stat().st_size
        self.time_a = datetime.fromtimestamp(data_entry.stat().st_atime)
        self.time_b = datetime.fromtimestamp(data_entry.stat().st_mtime)
        self.time_c = datetime.fromtimestamp(data_entry.stat().st_ctime)

    def to_string(self) -> str:
        str_object = f"""
            file_path : {self.file_path}
            file_name : {self.file_name}
            format : {self.file_format}
            type : {self.file_type}
            size : {self.size} bits
            time A : {self.time_a}
            time B : {self.time_b}
            time C : {self.time_c}"""
        return str_object


class FilesManager:

    def __init__(self) -> None:    
        self.files = {
            FileType.audio:[], FileType.video:[], FileType.image:[]
        }

        self.formats = {
            FileType.image : ['jpeg', 'png', 'jpg'],
            FileType.video : ['mp4'],
            FileType.audio : ['ogg', 'mp3', 'opus', 'm4a']
        }

        self.media_types = [FileType.audio, FileType.video, FileType.image]


    def iterate_directory_to_save_file_names(self, origin_path:str) -> tuple:
        contents = os.scandir(origin_path)
        for item in contents:
            if item.is_dir():
                self.iterate_directory_to_save_file_names(origin_path=item.path)
            else:
                size = item.stat().st_size
                if size > 0:

                    file_type, file_format = self.define_type_format_file(file_name=item.name)
                    # print(file_type)
                    if file_type is not None and file_type in self.media_types:
                        media_file  = MediaFile(
                            data_entry=item,
                            file_format=file_format,
                            file_type=file_type
                        )
                        self.files[file_type].append(media_file)
                        # print(media_file.to_string())
    def define_type_format_file(self, file_name:str)->tuple:
        f_type = None
        f_format = file_name[file_name.rfind('.')+1::]
        if f_format in self.formats[FileType.audio]:
            f_type = FileType.audio
        elif f_format in self.formats[FileType.image]:
            f_type = FileType.image
        elif f_format in self.formats[FileType.video]:
            f_type = FileType.video
        return f_type, f_format

    def print_report(self)->None:
        print("   WhatsApp Files tidy up   ")
        report = f"""
            audio : {len(self.files[FileType.audio])} file(s)
            video : {len(self.files[FileType.video])} file(s)
            image : {len(self.files[FileType.image])} file(s)
        """
        print(report)

    def sort_audio_files(self)->tuple:
        sufix = ["AUD-", "PTT-"]
        years = set()
        months = set()
        for file in self.files[FileType.audio]:
            file_name = file.file_name
            if file_name.startswith(sufix[0]) or file_name.startswith(sufix[1]):
                years.add(file_name[4:8:1])
                months.add(file_name[8:10:1])
        return years, months