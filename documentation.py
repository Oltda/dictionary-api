import justpy as jp


class Doc:

    def serve(self):
        wp = jp.WebPage()



        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Instant Dictionary API", classes="text-4xl m-2")
        jp.Div(a=div, text="Get definitions of words: ", classes="text-lg")
        jp.Hr(a=div)
        jp.Div(a=div, text="www.example.com/api?w=rabbit")
        jp.Hr(a=div)
        jp.Div(a=div, text="""
        {"word": "rabbit", "definition": 
        ["One of several small mammals of the family Leporidae, 
        with long ears, long hind legs and a short, fluffy tail."]}
        """)
        return wp


