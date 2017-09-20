import re
import sublime
import sublime_plugin

class MapFlagCommand(sublime_plugin.TextCommand):
    def run(self,edit):
        view = self.view
        region = view.find(r"db\.\w+\.aggregate\s{0, }\(\s{0, }\[",0)
        if region:
            str = view.substr(region)
            view.replace(edit, region,"{runCommand:{\n\
    aggregate:'"+str[3:str.index(".agg",0,len(str))]+"',\n\
    pipeline:[")
            footer =view.find_all(r"\][\s]{0,}\)[\s]{0,}$",0)
            if footer:
                view.replace(edit, footer[len(footer)-1],"]}}")
            return
        else:
            region = view.find(r"[{\w\s:]+'\w+'[,\s\w_]+:\s{0,}\[",0)
            if region:
                str = view.substr(region)
                print(str)
                pattern = re.compile(r"\s{0,}{[{\w\s:]+'")
                str = re.sub(pattern, '', str);
                pattern = re.compile(r"'[,\s\w:]+\[")
                str = re.sub(pattern, '', str);
                print("str =",str)
                view.replace(edit,region,"db."+str+".aggregate([")
                # s = re.sub(pattern, ' ', str);
                footer =view.find_all(r"(^\s+){0,}\][\s]{0,}}[\s]{0,}}[\s]{0,}$")
                if footer:
                    view.replace(edit, footer[len(footer)-1],"])")