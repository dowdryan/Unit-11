# --------------------------------------------------------------------------------------------------------------------------------
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "veryverysecret"
debug = DebugToolbarExtension(app)
# --------------------------------------------------------------------------------------------------------------------------------
class Story:
    """Madlibs story."""

    def __init__(self, words, text):
        """Create story with words and template text."""
        self.prompts = words # Uses this
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""
        text = self.template
        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)
        print(text)
        return text

# --------------------------------------------------------------------------------------------------------------------------------
# Here's a story to get you started

"""Provided answer parameters that go into the story"""
ans = {"verb": "eat", "noun": "mango", "place": "kingdom", "adjective": "swollen", "plural_noun": "other mangos"}


"""Making a new story"""
story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

# """Generate the story"""
# s.generate(ans)
# story.generate(ans)

# --------------------------------------------------------------------------------------------------------------------------------
@app.route("/madlibs")
def my_page():
    prompts = story.prompts
    return render_template("home.html", 
                           prompts = prompts)

@app.route("/madlibs-story")
def get_answers():
    # noun = request.args['noun']
    words = story.generate(request.args)
    return render_template("story.html", words = words)
