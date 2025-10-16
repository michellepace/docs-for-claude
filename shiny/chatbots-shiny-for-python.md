In this article, you’ll learn how to build a chatbot powered by a Large Language Model (LLM) `shiny` and [`chatlas`](https://posit-dev.github.io/chatlas/).

## Get started [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#get-started)

### Choose a template [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#choose-a-template)

Pick from the following LLM providers below to start your chatbot. Copy & paste the relevant `shiny create` terminal command to get the relevant source files on your machine.

- Ollama
- Anthropic
- OpenAI
- Google
- Bedrock Anthropic
- Azure OpenAI
- LangChain
- Other
- Help me choose!

```sourceCode bash
shiny create --template chat-ai-ollama
```

```sourceCode bash
shiny create --template chat-ai-anthropic
```

```sourceCode bash
shiny create --template chat-ai-openai
```

```sourceCode bash
shiny create --template chat-ai-gemini
```

```sourceCode bash
shiny create --template chat-ai-anthropic-aws
```

```sourceCode bash
shiny create --template chat-ai-azure-openai
```

```sourceCode bash
shiny create --template chat-ai-langchain
```

`chatlas` supports a [wide variety](https://posit-dev.github.io/chatlas/#model-providers) of LLM providers including Vertex, Snowflake, Groq, Perplexity, and more. In this case, you can start from any template and swap out the `chat_client` with the relevant chat constructor (e.g., `ChatVertex()`).

If you’re not sure which provider to choose, `chatlas` provides a [great guide](https://posit-dev.github.io/chatlas/#model-choice) to help you decide.

When you run the `shiny create` command, you’ll be provided with some tips on where to obtain the necessary API keys (if any) and how to securely add them to your app.

Also, if you’re not ready to sign up for a cloud provider (e.g., Anthropic, OpenAI, etc.), you can run models locally (for free!) with the Ollama template. This is a great way to get started and learn about LLMs without any cost, and without sharing your data with a cloud provider.

Once your credentials (if any) are in place, [run the app](https://shiny.posit.co/py/get-started/create-run.html#run-your-shiny-application). Congrats, you now have a streaming chat interface powered by an LLM of your choice! 🎉

[![Screenshot of a conversation with the Chat component.](https://shiny.posit.co/py/images/chat-quick-start.png)](https://shiny.posit.co/py/images/chat-quick-start.png "Screenshot of a conversation with the Chat component.")

Screenshot of a conversation with the `Chat` component.

### Inspect the code [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#inspect-the-code)

Go ahead and open the `app.py` file from your template, you’ll see something roughly like this:

- Express
- Core

```sourceCode python
from chatlas import ChatOllama
from shiny.express import ui

# Might instead be ChatAnthropic, ChatOpenAI, or some other provider
chat_client = ChatOllama(model="llama3.2")

chat = ui.Chat(id="my_chat")
chat.ui()

@chat.on_user_submit
async def handle_user_input(user_input: str):
    response = await chat_client.stream_async(user_input)
    await chat.append_message_stream(response)
```

```sourceCode python
from chatlas import ChatOllama
from shiny import ui, App

app_ui = ui.page_fixed(
    ui.chat_ui(id="my_chat")
)

def server(input):
    chat = ui.Chat(id="my_chat")
    chat_client = ChatOllama(model="llama3.2")

    @chat.on_user_submit
    async def handle_user_input(user_input: str):
        response = await chat_client.stream_async(user_input)
        await chat.append_message_stream(response)

app = App(app_ui, server)
```

From here, we can see the key requirements for streaming reponses from an LLM:

1. Initialize a `chat_client` (e.g., `ChatOllama()`) to interact with the LLM.

   - [`chatlas`](https://posit-dev.github.io/chatlas/) isn’t required for this, but it’s highly recommended.
2. Initialize a `Chat()` instance.
3. Display it’s UI element with `chat.ui()`.

   - Here you can specify [startup messages](https://shiny.posit.co/py/docs/genai-chatbots.html#startup-messages), [customize icons](https://shiny.posit.co/py/docs/genai-chatbots.html#custom-icons), and more.
4. Decorate a `@chat.on_user_submit` function to fire when the user submits input.

   - Here, `chat_client` generates a `response` stream, which is passed along to the `.append_message_stream()` method for display.

In this article, our primary focus is the UI portion of the chatbot (i.e., `chat`). That said, since LLM model choice and prompt design are so important for generating good responses, we’ll briefly touch on that first.

### Models & prompts [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#models-prompts)

With `chatlas`, it’s very easy to switch between the model and system prompt behind your `chat_client`. Just change the `model` and `system_prompt` parameters:

```sourceCode python
chat_client = ChatOllama(
  model="llama3.2",
  system_prompt="You are a helpful assistant",
)
```

If you’re new to programming with LLMs, we **highly recommend** visiting the `chatlas` website for guidance on [where to start](https://posit-dev.github.io/chatlas/get-started.html), [choosing a model](https://posit-dev.github.io/chatlas/#model-choice), and [designing an effective system prompt](https://posit-dev.github.io/chatlas/prompt-design.html).

If you’re not yet ready learn about LLMs, that’s okay! We can still dive into `chat` UI features without knowing much about LLMs.

Model playground template

Interactively experiment with different models and prompts with the playground template. It’s also a great learning resource on how to leverage reactivity for dynamic prompts and model selection.

```sourceCode bash
shiny create --template chat-ai-playground
```

## Add messages [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#add-messages)

### On startup [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#startup-messages)

Show message(s) when the chat first loads by providing `messages` to `chat.ui()`. Messages are interpreted as markdown, so you can use markdown (or HTML) to format the text as you like.

Startup messages are a great place to introduce the chatbot with a brief description of what it can do and, optionally, some [input suggestions](https://shiny.posit.co/py/docs/genai-chatbots.html#suggest-input) to help the user get started quickly. Messages can also contain arbitrary Shiny UI [components](https://shiny.posit.co/py/components/), so you could even include something like a [tooltip](https://shiny.posit.co/py/components/display-messages/tooltips/) to provide additional details on demand.

- Express
- Core

```sourceCode python
chat.ui(
  messages=["**Hello!** How can I help you today?"]
)
```

```sourceCode python
ui.chat_ui(
  id="chat",
  messages=["**Hello!** How can I help you today?"],
)
```

[![Screenshot of a chatbot with a welcome message.](https://shiny.posit.co/py/images/chat-hello.png)](https://shiny.posit.co/py/images/chat-hello.png "Screenshot of a chatbot with a welcome message.")

Screenshot of a chatbot with a welcome message.

### On user submit [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#on-user-submit)

Every `chat` instance should have a `@chat.on_user_submit` callback. This is where you’ll receive the user’s input and append a response to the chat. In your started template, the response `stream` is provided by [`chatlas`](https://posit-dev.github.io/chatlas/) via `chat_client.stream_async(prompt)`. As it turns out, `stream` is an [generator](https://stackoverflow.com/q/1756096) of markdown strings, and the `.append_message_stream()` method can work with any generator of strings. This is useful to know if you want to:

1. Use another framework for reponse generation (e.g., [LangChain](https://www.langchain.com/)).
2. Transform the stream as it’s being generated (e.g., capitalize the response).

```sourceCode python
@chat.on_user_submit
async def _(user_input: str):
    stream = stream_generator(user_input)
    await chat.append_message_stream(stream)

# 'Wrap' the stream to capitialize the response
async def stream_generator(user_input):
    stream = await chat_client.stream_async(user_input)
    async for chunk in stream:
        yield chunk.upper()
```

## Bookmark messages [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#bookmark-messages)

When a Shiny app reloads, the app returns to it’s original state, unless the URL includes [bookmarked](https://shiny.posit.co/py/api/express/session.Session.html) state. [1](https://shiny.posit.co/py/docs/genai-chatbots.html#fn1) Automatically updating the URL to include a bookmark of the chat state is a great way to help users return to their work if they accidentally refresh the page or unexpectedly lose their connection.

Adding bookmark support to an app generally requires some extra effort. At the very least, Shiny needs to know where and when to save state, and in some cases, how to save/restore it as well. [2](https://shiny.posit.co/py/docs/genai-chatbots.html#fn2) The `.enable_bookmarking()` method makes this all a bit easier for bookmarking both the `chat` and `chat_client` instances.

- Express
- Core

```sourceCode python
from chatlas import ChatOllama
from shiny.express import ui

chat_client = ChatOllama(model="llama3.2")

chat = ui.Chat(id="chat")
chat.ui(messages=["Welcome!"])

chat.enable_bookmarking(
    chat_client,
    bookmark_store="url", # or "server"
    bookmark_on="response", # or None
)
```

```sourceCode python
from chatlas import ChatOllama
from shiny import ui, App

app_ui = ui.page_fixed(
    ui.chat_ui(id="chat", messages=["Welcome!"])
)

def server(input):
    chat_client = ChatOllama(model="llama3.2")
    chat = ui.Chat(id="chat")

    chat.enable_bookmarking(
        chat_client,
        bookmark_on="response", # or None
    )

app = App(app_ui, server, bookmark_store="url")
```

Adding this `.enable_bookmarking()` call handles the where, when, and how of bookmarking chat state:

1. Where ( `store`)

   - `"url"` store the state in the URL.
   - `"server"` store the state on the server. Consider this over `"url"` if you want to support a large amount of state, or have other bookmark state that can’t be serialized to JSON.
2. When ( `bookmark_on`)

   - `"response"`: triggers a bookmark when an `"assistant"` response is appended.
   - `None`: don’t trigger a bookmark. This assumes you’ll be triggering bookmarks through other means (e.g., a button).
3. How is handled automatically by registering the relevant `on_bookmark` and `on_restore` callbacks.

Also note that when `.enable_bookmarking()` triggers a bookmark for you, it’ll also update the URL query string to include the bookmark state. This way, when the user unexpectedly loses connection, they can load the current URL to restore the chat state, or go back to the original URL to start over.

## Layout [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#layout)

### Fill [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#fill)

Fill the page on desktop (and mobile) with the `fillable=True` (and `fillable_mobile=True`) page options. This way, the input stays anchored to the bottom of the page, and the chat fills the remaining space.

- Express
- Core

```sourceCode python
from shiny.express import ui

ui.page_opts(
  fillable=True,
  fillable_mobile=True,
)

chat = ui.Chat(id="chat")
chat.ui(messages=["Welcome!"])
```

```sourceCode python
from shiny import ui, App

app_ui = ui.page_fillable(
    ui.chat_ui(id="chat", messages=["Welcome!"]),
    fillable_mobile=True,
)

def server(input):
    chat = ui.Chat(id="chat")

app = App(app_ui, server)
```

[![Screenshot of a chatbot filling the page.](https://shiny.posit.co/py/images/chat-fill.png)](https://shiny.posit.co/py/images/chat-fill.png "Screenshot of a chatbot filling the page.")

Screenshot of a chatbot filling the page.

### Card layout [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#card-layout)

Another useful UI pattern is to embed the chat component inside a `ui.card()`. If nothing else, this will help visually separate the chat from the rest of the app. It also provides a natural place to provide a header (with perhaps a [tooltip](https://shiny.posit.co/py/components/display-messages/tooltips/) with more info about your chatbot). [Cards](https://shiny.posit.co/py/layouts/panels-cards/#content-divided-by-cards) also come with other handy features like `full_screen=True` to make the chat full-screen when embedded inside a larger app.

- Express
- Core

```sourceCode python
from shiny.express import ui
from faicons import icon_svg

ui.page_opts(
    fillable=True,
    fillable_mobile=True,
    class_="bg-light",
)

chat = ui.Chat(id="chat")

with ui.card():
    with ui.card_header(class_="d-flex justify-content-between align-items-center"):
        "Welcome to Posit chat"
        with ui.tooltip():
            icon_svg("question")
            "This chat is brought to you by Posit."
    chat.ui(
        messages=["Hello! How can I help you today?"]
    )
```

```sourceCode python
from shiny import ui, App

app_ui = ui.page_fillable(
  ui.card(
      ui.card_header(
          "Welcome to Posit chat",
          ui.tooltip(
              icon_svg("question"),
              "This chat is brought to you by Posit."
          ),
          class_="d-flex justify-content-between align-items-center"
      ),
      ui.chat_ui(
          id="chat",
          messages=["Hello! How can I help you today?"],
      ),
    ),
    fillable_mobile=True,
    class_="bg-light",
)

def server(input):
    chat = ui.Chat(id="chat")

app = App(app_ui, server)
```

[![Screenshot of a chatbot embedded in a card with a header and tooltip.](https://shiny.posit.co/py/images/chat-card-tooltip.png)](https://shiny.posit.co/py/images/chat-card-tooltip.png "Screenshot of a chatbot embedded in a card with a header and tooltip.")

Screenshot of a chatbot embedded in a card with a header and tooltip.

## Theming [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#theming)

### Custom CSS [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#custom-css)

To customize main colors and fonts, provide a `ui.Theme()` to the `theme` page option. Theming customization may be done directly on `ui.Theme()` (e.g., `.add_defaults()`) and/or created from a [brand-yml](https://posit-dev.github.io/brand-yml/) file and applied with `ui.Theme().from_brand()`. Note you can also introduce a dark mode toggle with `ui.input_dark_mode()`.

- Express
- Core

```sourceCode python
from shiny.express import ui

ui.page_opts(
    theme=ui.Theme().add_defaults(primary="#a855f7"),
    title=ui.div(
        "My themed chat app",
        ui.input_dark_mode(mode="dark"),
        class_="d-flex justify-content-between w-100",
    )
)

chat = ui.Chat(id="chat")

with ui.sidebar(width=300, style="height:100%"):
    chat.ui(height="100%", messages=["Welcome!"])

"Main content region"
```

```sourceCode python
from shiny import ui, App

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.chat_ui(id="chat", messages=["Welcome!"], height="100%"),
        width=300, style="height:100%"
    ),
    "Main content region",
    theme=ui.Theme().add_defaults(primary="#a855f7"),  # <<
    title=ui.tags.div(
        "My themed chat app",
        ui.input_dark_mode(mode="dark"),
        class_="d-flex justify-content-between w-100",
    ),
)

def server(input):
    chat = ui.Chat(id="chat")

app = App(app_ui, server)
```

[![Screenshot of a chatbot with a custom theme and dark mode toggle.](https://shiny.posit.co/py/images/chat-themed.png)](https://shiny.posit.co/py/images/chat-themed.png "Screenshot of a chatbot with a custom theme and dark mode toggle.")

Screenshot of a chatbot with a custom theme and dark mode toggle.

### Custom icons [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#custom-icons)

Customize the assistant icon by supplying HTML/SVG to `icon_assistant` when creating the UI element (or when appending a message). The `faicons` package makes it easy to do this for [font awesome](https://fontawesome.com/), but other icon libraries (e.g., [Bootstrap icons](https://shiny.posit.co/py/docs/(https://icons.getbootstrap.com/#usage)), [heroicons](https://heroicons.com/), etc.) or custom SVGs are also possible by providing inline SVGs as a string to `ui.HTML()`.

- Express
- Core

```sourceCode python
from faicons import icon_svg

chat.ui(
  messages=["**Hello!** How can I help you today?"],
  icon_assistant=icon_svg("slack"),
)
```

```sourceCode python
from faicons import icon_svg

ui.chat_ui(
  id="chat",
  messages=["**Hello!** How can I help you today?"],
  icon_assistant=icon_svg("slack"),
)
```

[![Screenshot of a chatbot with a custom (slack) icon.](https://shiny.posit.co/py/images/chat-hello-slack.png)](https://shiny.posit.co/py/images/chat-hello-slack.png "Screenshot of a chatbot with a custom (slack) icon.")

Screenshot of a chatbot with a custom (slack) icon.

Custom `<img>` icons

HTML `<img>` tags also work. By default, they fill their container, and may get clipped by the container’s `border-radius`. To scale down the image, add a `icon` CSS class, or `border-0` to remove the `border` and `border-radius`.

- Express
- Core

```sourceCode python
from faicons import icon_svg

chat.ui(
  messages=["**Hello!** How can I help you today?"],
  icon_assistant=ui.img(
    src="https://raw.githubusercontent.com/posit-dev/py-shiny/c1445b2/tests/playwright/shiny/components/chat/icon/img/shiny.png"
  )
)
```

```sourceCode python
from faicons import icon_svg

ui.chat_ui(
  id="chat",
  messages=["**Hello!** How can I help you today?"],
  icon_assistant=ui.img(
    src="https://raw.githubusercontent.com/posit-dev/py-shiny/c1445b2/tests/playwright/shiny/components/chat/icon/img/shiny.png",
  )
)
```

[![Screenshot of a chatbot with a custom (shiny) image icon.](https://shiny.posit.co/py/images/chat-hello-shiny.png)](https://shiny.posit.co/py/images/chat-hello-shiny.png "Screenshot of a chatbot with a custom (shiny) image icon.")

Screenshot of a chatbot with a custom (shiny) image icon.

## Recommend input [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#recommend-input)

### Suggest input [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#suggest-input)

Help users start or continue a conversation by providing **input suggestions**. To create one, add a `suggestion` CSS class to relevant portion(s) of the message text. You can also add a `submit` class to make the suggestion submit the input automatically. Try clicking on the suggestions (or accessing via keyboard) below to see how they work.

app.py+

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

from shiny.express import ui

welcome = """

\*\*Hello!\*\* How can I help you today?

Here are a couple suggestions:

\\* <span class="suggestion">Tell me a joke</span>

\\* <span class="suggestion submit">Tell me a story</span>

"""

chat = ui.Chat(id="chat")

chat.ui(messages=\[welcome\])

@chat.on\_user\_submit

asyncdef\_(user\_input: str):

await chat.append\_message(f"You said: {user\_input}")

Suggestions are a great way to help guide users throughout a multi-turn conversation (for real examples, see [here](https://shiny.posit.co/py/docs/genai-inspiration.html#guided-exploration-%F0%9F%A7%AD)). To accomplish this, you’ll need to instruct the AI how to generate suggestions itself. We’ve found that adding a section like the one below to your [`system_prompt`](https://shiny.posit.co/py/docs/genai-chatbots.html#models-prompts) to be effective for this:

````sourceCode markdown
## Showing prompt suggestions

If you find it appropriate to suggest prompts the user might want to write, wrap the text of each prompt in `<span class="suggestion">` tags.
Also use "Suggested next steps:" to introduce the suggestions. For example:

```
Suggested next steps:

1. <span class="suggestion">Suggestion 1.</span>
2. <span class="suggestion">Suggestion 2.</span>
3. <span class="suggestion">Suggestion 3.</span>
```
````

Card-based suggestions

Input suggestions can also things other than text, like images or cards. To create one, supply a `data-suggestion` attribute with the suggestion text on the desired HTML element. As shown below, we highly recommend using a `ui.card()` in this scenario – it should be fairly obvious to the user that it’s clickable, and comes with a nice hover effect.

app.py×suggestions.py×+

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

from shiny import reactive

from shiny.express import expressify, ui

from suggestions import card\_suggestions

with ui.hold() as suggestions:

card\_suggestions()

welcome = f"""

\*\*Hello!\*\* How can I help you today?

Here are a couple suggestions:

{suggestions\[0\]}

"""

chat = ui.Chat(id="chat")

chat.ui(messages=\[welcome\])

@chat.on\_user\_submit

asyncdef\_(user\_input: str):

await chat.append\_message(f"You said: {user\_input}")

Keyboard shortcuts

Any suggestion can be auto-submitted by holding `Ctrl/Cmd` when clicking on it. Morever, you can opt-out of auto-submitting any suggestion by holding `Alt/Option` when clicking on a suggestion.

### Update input [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#update-input)

Input suggestions are a great starting point for recommending input to user, but more advanced use cases may require programmatically updating the user input. With `chat.update_user_input()`, you can change placeholder text, the input value, and even focus or submit that value on the user’s behalf.

For example, the app below collects some user input through a set of inputs in the sidebar, which effectively just prepopulates the starting user prompt, which the user can then further modify as they see fit:

[![Screenshot of an app using input controls to populate a user prompt](https://shiny.posit.co/py/images/genai-update-input.png)](https://shiny.posit.co/py/images/genai-update-input.png "Screenshot of an app using input controls to populate a user prompt")

Screenshot of an app using input controls to populate a user prompt

Note

The app above is available as a [template](https://shiny.posit.co/py/templates/):

```sourceCode bash
shiny create --template data-sci-adventure \
    --github posit-dev/py-shiny-templates/gen-ai
```

## Interactive messages [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#interactive-messages)

Messages can contain Shiny UI elements like [inputs](https://shiny.posit.co/py/components/#inputs), [outputs](https://shiny.posit.co/py/components/#outputs), etc. This allows you to collect user input, display rich interactive output (e.g., [Jupyter Widgets](https://shiny.posit.co/py/docs/jupyter-widgets.html)), or provide additional context (e.g. [tooltips](https://shiny.posit.co/py/components/display-messages/tooltips/)) from within the chat.

For example, in the “What’s for Dinner?” app, when the user requests to extract recipe, a message is shown with a human readable version of recipe, as well as a [download button](https://shiny.posit.co/py/api/express/express.render.download.html) to get the recipe in a structured JSON format:

[![Screenshot of a download button included in a chat message](https://shiny.posit.co/py/images/genai-interactive-messages.png)](https://shiny.posit.co/py/images/genai-interactive-messages.png "Screenshot of a download button included in a chat message")

Screenshot of a download button included in a chat message

Note

The app above is available as a [template](https://shiny.posit.co/py/templates/):

```sourceCode bash
shiny create --template dinner-recipe \
    --github posit-dev/py-shiny-templates/gen-ai
```

For a more basic example, here’s a startup message with an input field:

app.py+

9

1

2

3

4

5

6

7

8

from shiny.express import ui

with ui.hold() as welcome:

"\*\*Hello!\*\* What's your name?"

ui.input\_text("name", None, placeholder="Enter name here")

chat = ui.Chat(id="chat")

chat.ui(messages=\[welcome\])

Interactive tool displays

Probably the most interesting way in which interactive messages can be used is from a custom [tool call](https://shiny.posit.co/py/docs/genai-tools.html) display. For example, you could have a tool that displays a [Data Grid](https://shiny.posit.co/py/components/outputs/data-grid/) or [Jupyter Widget](https://shiny.posit.co/py/docs/jupyter-widgets.html) (e.g., a [plotly](https://shiny.posit.co/py/components/outputs/plot-plotly/) graph).

## Message streams [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#message-streams)

### Non-blocking streams [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#non-blocking-streams)

Under-the-hood, `.append_message_stream()` launches a non-blocking [extended task](https://shiny.posit.co/py/docs/nonblocking.html). This allows the app to be responsive while the AI generates the response, even when multiple concurrent users are on a single Python process.

A few other benefits of an extended task is that they make it easy to:

1. Reactively read for the `.result()`.
2. Reactively read for the `.status()`.
3. `.cancel()` the stream.

To grab the latest message stream, read the `.latest_message_stream` property on the `chat` object. This property always points to the most recent message stream, making it easy to work with it in a reactive context. Here’s an example of reactively reading the status and result of the latest message stream:

app.py×app\_utils.py×+

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

from app\_utils import stream\_generator

from shiny.express import render, ui

chat = ui.Chat("chat")

@render.code

defstream\_status():

returnf"Status: {chat.latest\_message\_stream.status()}"

chat.ui(placeholder="Type anything here and press Enter")

@render.text

asyncdefstream\_result():

returnf"Result: {chat.latest\_message\_stream.result()}"

@chat.on\_user\_submit

asyncdef\_(message: str):

await chat.append\_message\_stream(stream\_generator())

Providing good UI/UX for canceling a stream is a bit more involved, but it can be done with a button that cancels the stream and notifies the user. See the example below for an approach to this:

Stream cancellation

app.py×app\_utils.py×+

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

from app\_utils import stream\_generator

from shiny import reactive

from shiny.express import input, ui

ui.input\_action\_button(

"cancel",

"Cancel stream",

class\_="btn btn-danger",

)

chat = ui.Chat("chat")

chat.ui(placeholder="Type anything here and press Enter")

@chat.on\_user\_submit

asyncdef\_(message: str):

await chat.append\_message\_stream(stream\_generator())

@reactive.effect

@reactive.event(input.cancel)

def\_():

chat.latest\_message\_stream.cancel()

ui.notification\_show("Stream cancelled", type="warning")

@reactive.effect

def\_():

ui.update\_action\_button(

"cancel",

disabled=chat.latest\_message\_stream.status() != "running"

)

### Streaming context [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#message-stream-context)

An alternative way to append a streaming messages is through the `.message_stream_context()` context manager. Compared to `.append_message_stream()`, it provides a bit more control over the stream’s lifecycle and content, but has the downside of not being non-blocking by default. You’ll find it useful when you want to:

1. Overwrite/replace content that already exists in a message.
2. Insert a new stream inside an existing stream.

The example below demonstrates both of these use cases. Note how the inner stream is used to show progress, and the outer stream is used to provide context:

app.py+

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

import asyncio

from shiny import reactive

from shiny.express import input, ui

welcome = f"""

\*\*Hello!\*\* Press the button below to append a stream.

{ui.input\_task\_button("do\_stream", "Stream", class\_="btn btn-primary")}

"""

chat = ui.Chat(id="my\_chat")

chat.ui(messages=\[welcome\])

@reactive.effect

@reactive.event(input.do\_stream)

asyncdef\_():

asyncwith chat.message\_stream\_context() as outer:

await outer.append("Starting stream 🔄...\\n\\nProgress:")

asyncwith chat.message\_stream\_context() as inner:

for x in \[0, 50, 100\]:

await inner.replace(f" {x}%")

await asyncio.sleep(1)

await outer.replace("Completed stream ✅")

As you’ll learn in [tool calling](https://shiny.posit.co/py/docs/genai-tools.html), a `.message_stream()` can also be nested inside an non-blocking `.append_message_stream()`, which is primarily useful for showing tool progress/results.

## Troubleshooting [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#troubleshooting)

### Error handling [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#error-handling)

When an error occurs in the `@chat.on_user_submit` callback, the app displays a dismissible notification about the error. When running locally, the actual error message is shown, but in production, only a generic message is shown (i.e., the error is sanitized since it may contain sensitive information). If you’d prefer to have errors stop the app, that can also be done through the `on_error` argument of `Chat` (see [the documentation](https://shiny.posit.co/py/api/ui.Chat.html) for more information).

[![Screenshot of a chatbot with an error message.](https://shiny.posit.co/py/images/chat-error.png)](https://shiny.posit.co/py/images/chat-error.png "Screenshot of a chatbot with an error message.")

Screenshot of a chatbot with an error message.

Custom error messages

Another way to handle error is to catch them yourself and append a message to the chat. This way, you can might provide a better experience with “known” errors, like when the user enters an invalid/unexpected input:

```sourceCode python
def format_as_error(x: str):
    return f'<span class="text-danger">{x}</span>'

@chat.on_user_submit
async def _(user_input: str):
    if not user_input.startswith("http"):
        msg = format_as_error("Please enter a valid URL")
        return await chat.append_message(msg)

    try:
        contents = scrape_page_with_url(input)
    except Exception:
        msg = "I'm sorry, I couldn't extract content from that URL. Please try again."
        return await chat.append_message(format_as_error(msg))

    response = await chat_client.stream_async(contents)
    await chat.append_message_stream(response)
```

### Debugging [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#debugging)

Sometimes response generation from an LLM might not be quite what you expect, leaving you to wonder what went wrong. With `chatlas`, your primary interactive debugging tool is to set `echo="all"` in the `.stream_async()` method to see the context of the chat history (emitted to your Python console). For lower-level debugging, you can also enable logging and/or access the full chat history via the `chat_client.get_turns()` method. For more, see `chatlas`’ [troubleshooting guide](https://posit-dev.github.io/chatlas/#troubleshooting).

Monitoring in production

Since `chatlas` builds on top of official Python SDKs like `openai` and `anthropic`, [monitoring](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/monitor-openai) solutions that integrate with their [logging](https://github.com/openai/openai-python?tab=readme-ov-file#logging) mechanism can be used to monitor and debug your chatbot in production.

## Message history [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#message-history)

The `chat.messages()` method returns a tuple of all the messages appended after startup. Use this if you want to obtain a record of messages as they appear in the UI. This makes implementing something like download feature easy:

app.py+

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

import json

from shiny.express import render, ui

ui.page\_opts(fillable=True, fillable\_mobile=True)

chat = ui.Chat("chat")

chat.ui(messages=\["Welcome!"\])

@render.download(filename="messages.json", label="Download messages")

defdownload():

yield json.dumps(chat.messages())

@chat.on\_user\_submit

asyncdef\_(user\_input: str):

await chat.append\_message(f"You said: {user\_input}")

Front-end vs back-end

Beware that `chat.messages()` only returns only the content sent to the UI, not necessarily the full message content sent/returned by the LLM. This means, if your chat history contains “background” context, you may instead want that full back-end message history. Note that with `chatlas`, you can access and set that additional context via the `.get_turns()` and `.set_turns()` methods on the `chat_client`.

For a more advanced example of how you can combine reactivity with `chat.messages()` to add a “New chat” button with a dropdown to select previous chats, see the example below:

app.py+

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

54

from datetime import datetime

from faicons import icon\_svg

from shiny import reactive

from shiny.express import input, render, ui

ui.page\_opts(fillable=True, fillable\_mobile=True)

chat = ui.Chat(id="chat")

chat.ui(messages=\["\*\*Hello!\*\* How can I help you today?"\])

with ui.layout\_columns(fill=False):

ui.input\_action\_button("new", "New chat", icon=icon\_svg("plus"))

@render.express

defhistory\_ui():

ifnot history():

return

choices = list(history().keys())

choices\_dict = dict(zip(choices, choices))

ui.input\_select(

"previous\_chat", None,

choices={"": "Choose a previous chat", \*\*choices\_dict}

)

@chat.on\_user\_submit

asyncdef\_(user\_input: str):

await chat.append\_message(f"You said: {user\_input}")

\# Track chat history

history = reactive.value({})

\# When a new chat is started, add the current chat messages

\# to the history, clear the chat, and append a new start message

@reactive.effect

@reactive.event(input.new)

asyncdef\_():

stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

hist = {\*\*history(), stamp: chat.messages()}

history.set(hist)

await chat.clear\_messages()

await chat.append\_message(f"Chat started at {stamp}")

\# When a previous chat is selected, clear the current chat,

\# and append the messages from the selected chat

@reactive.effect

@reactive.event(input.previous\_chat)

asyncdef\_():

ifnot input.previous\_chat():

return

msgs = history()\[input.previous\_chat()\]

await chat.clear\_messages()

for msg in msgs:

await chat.append\_message(msg)

## Next steps [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#next-steps)

The [next article](https://shiny.posit.co/py/docs/genai-stream.html) covers a more generic way to stream generative AI: the `ui.MarkdownStream()` component. This component is useful when you don’t want a full chat interface, but still want to stream in some content from an LLM.

Skip to other articles in the series if you want to learn about other generally useful Generative AI techniques like [tool calls](https://shiny.posit.co/py/docs/genai-tools.html), [structured output](https://shiny.posit.co/py/docs/genai-structured-data.html), and [RAG](https://shiny.posit.co/py/docs/genai-rag.html).

## Footnotes [Anchor](https://shiny.posit.co/py/docs/genai-chatbots.html\#footnotes-1)

1. This can be especially frustrating behavior since hosted apps, by default, will close a idle session after a certain ( [configurable](https://docs.posit.co/shinyapps.io/guide/applications/#advanced-settings)) amount of time. [↩︎](https://shiny.posit.co/py/docs/genai-chatbots.html#fnref1)

2. When server-side state can’t be fully determined by the UI’s `input` values alone, you’ll need to register `on_bookmark` and `on_restore` callbacks to save and restore that server-state. [↩︎](https://shiny.posit.co/py/docs/genai-chatbots.html#fnref2)