#coding=utf-8
#created by yong.a.liang
#created date 2017-04-29
#modified by xxx
#is for filter those info log,is use by debug env
import sublime
import sublime_plugin

class JavaPreEditCommand(sublime_plugin.WindowCommand):
    def run(self, reverse=False):
        window = self.window
        window.run_command("show_panel", {"panel": "find"})
        window.run_command("insert", {"characters": "\@RunWith\(Cucumber.class\)"})
        window.run_command("hide_panel",{"cancel":"true"})
        window.run_command("find_all", {"characters": "n"})
        window.run_command("insert", {"characters": "import org.json.JSONObject;"})
        window.run_command("insert", {"characters": "\n"})
        window.run_command("insert", {"characters": "import org.junit.Assert;"})
        window.run_command("insert", {"characters": "\n"})
        window.run_command("insert", {"characters": "import org.springframework.beans.factory.annotation.Autowired;"})
        window.run_command("insert", {"characters": "\n"})
        window.run_command("insert", {"characters": "import org.springframework.test.context.ContextConfiguration;"})
        window.run_command("insert", {"characters": "\n"})
        window.run_command("insert", {"characters": "import org.springframework.test.context.TestPropertySource;"})
        window.run_command("insert", {"characters": "\n"})
        window.run_command("insert", {"characters": "import com.mce.gems.test.itadmin.Application;"})
        window.run_command("insert", {"characters": "\n"})
        window.run_command("insert", {"characters": "import com.mce.gems.test.itadmin.config.TestConfig;"})
        window.run_command("insert", {"characters": "\n"})
        window.run_command("insert", {"characters": "\n"})
        window.run_command("insert", {"characters": "@ContextConfiguration(classes = Application.class)"})
        window.run_command("insert", {"characters": "\n"})
        window.run_command("insert", {"characters": "@TestPropertySource(\"/application.properties\")"})
        window.run_command("show_panel", {"panel": "find"})
        window.run_command("insert", {"characters": "throw new PendingException\(\);"})
        window.run_command("hide_panel",{"cancel":"true"})
        window.run_command("find_all", {"characters": "n"})
        window.run_command("insert", {"characters": "Assert.assertTrue(true);"})
        window.run_command("show_panel", {"panel": "find"})
        window.run_command("insert", {"characters": "my.package.name"})
        window.run_command("hide_panel",{"cancel":"true"})
        window.run_command("find_all", {"characters": "n"})
        window.run_command("insert", {"characters": "com.mce.gems.test.itadmin.steps"})



        # window.run_command("insert", {"characters": " for US"})

