import re
import sublime
import sublime_plugin

class HelloCommand(sublime_plugin.TextCommand):
    def run(self,edit):
        view = self.view
        # region = view.find(r"db\.\w+\.aggregate\s{0, }\(\s{0, }\[",0)
        # if region:
        #     str = view.substr(region)
        #     view.replace(edit, region,"{runCommand:{aggregate:'" +\
        #     str[3:str.index(".agg",0,len(str))] +\
        #     "',pipeline:[")
        #     footer =view.find("\][\s]{0,}\)[\s]{0,}$",0)
        #     if footer:
        #         view.replace(edit, footer,"]}}")
        #     return
        # else:
        #     region = view.find(r"[{\w\s:]+'\w+'[,\s\w_]+:\s{0,}\[",0)
        #     if region:
        #         str = view.substr(region)
        #         print(str)
        #         pattern = re.compile(r"\s{0,}{[{\w\s:]+'")
        #         str = re.sub(pattern, '', str);
        #         pattern = re.compile(r"'[,\s\w:]+\[")
        #         str = re.sub(pattern, '', str);
        #         print("str =",str)
        #         view.replace(edit,region,"db."+str+".aggregate([")
        #         # s = re.sub(pattern, ' ', str);
        #         footer =view.find(r"(^\s+){0,}\][\s]{0,}}[\s]{0,}}[\s]{0,}$",0)
        #         if footer:
        #             view.replace(edit, footer,"])")

        # print("view.id = ",view.id())
        # print("buffer.id = ",view.buffer_id())
        # print("is_primary = ",view.is_primary())

        ##file_name 包含路径 和文件名，如果是未保存的文件，返回None
        path = view.file_name()
        if path:
            pattern = re.compile(r"\\[\w. _-]+$")
            print("path = ",re.sub(pattern, '', path))
            return re.sub(pattern, '', path)
        print("path = ",path)
        return path
        ##return null, the name assigned to the buffer, if any?
        # view.set_name("name")
        # print("view.name = ",view.name())
        # self.random

