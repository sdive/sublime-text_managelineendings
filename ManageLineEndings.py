import sublime
import sublime_plugin

class EventListener(sublime_plugin.ViewEventListener):
	
	new_line = "¬";
    
	def __init__(self, view):
		self.view=view
		self.settings= sublime.load_settings('ManageLineEndings.sublime-settings')


	def on_modified(self):
		isenabled=self.settings.get("draw_line_endings");
		self.view.erase_phantoms("retchars");
		if isenabled == "all":
			for retchar in self.view.find_all("\n"):
				self.view.add_phantom("retchars", retchar, self.new_line, sublime.LAYOUT_INLINE)
