import sublime, sublime_plugin

class PromptMdCodeBlockCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.window.show_input_panel("Language:", "", self.on_done, None, None)
        pass

    def on_done(self, text):
        try:
            if self.window.active_view():
                self.window.active_view().run_command("md_code_block", {"lang": text} )
        except ValueError:
            pass

class MdCodeBlockCommand(sublime_plugin.TextCommand):
    def run(self, edit, lang):
        sels = self.view.sel()
        for sel in sels:
            self.view.insert(edit, sel.end(), "\n```")
            self.view.insert(edit, sel.begin(), "```" + lang + "\n")
