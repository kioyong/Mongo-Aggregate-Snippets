#coding=utf-8
#create by yong.a.liang@accenture.com
#create date 2016-07-06

import sublime
import sublime_plugin

class FmartArrayCommand(sublime_plugin.WindowCommand):
    def run(self, reverse=False):
        window = self.window
        window.run_command("set_file_type",{"syntax":"Packages/SQL/SQL.sublime-syntax"})#for other syntax(text) then will add focus to row end,then revert will hit issue.
        window.run_command("select_all")
        window.run_command("split_selection_into_lines")#add focus to each rows
        window.run_command("move_to",{"to": "bol"})#go to row home
        window.run_command("insert",{"characters": "'"})#add "'" to row home
        window.run_command("move_to",{"to": "eol"})#go to row end
        window.run_command("insert",{"characters": "',"})#add "'," to row end
        window.run_command("right_delete")#changed to single line
        window.run_command("move_to",{"to": "eol"})#move to end
        window.run_command("left_delete")#delete extra ","
"""
this function is for quick treatment sql query result to script "where clmnum in (....)".
for exmaple
before test data
34876756
34726087
34956878
34720164
34589417
after excute this function >>
'34876756','34726087','34956878','34720164','34589417'
>>
revert function>> unfmart_array.py
"""