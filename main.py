import os
from datetime import datetime

import pytz
from supabase import create_client
from dotenv import load_dotenv
from fasthtml.common import *

#load environment variables
load_dotenv()

MAX_NAME_CHAR = 15
MAX_MESSAGE_CHAR = 500
TIMESTAMP_FMT = "%Y-%m-%d %H:%M:%S %p IST"


#Initialize Supabase client
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))


app,rt = fast_app(
    hdrs = (Link(rel="icon", type="assets/x-icon", href="/assets/favicon.png"),),
)

def get_ist_time():
    ist_tz = pytz.timezone("Asia/Kolkata")
    return datetime.now(ist_tz)

def add_message(name, message):
    timestamp = get_ist_time().strftime(TIMESTAMP_FMT)
    supabase.table("MyGuestbook").insert(
        {"name": name, "message": message, "timestamp": timestamp}
    ).execute()

def get_messages():
    #sort by 'id' in descending order to get the latest entries first
    response = (
        supabase.table("MyGuestbook")
        .select("*")
        .order("id", desc=True)
        .execute()
    )
    return response.data

def render_message(entry):
    return Article(
            Header(f"Name: {entry['name']}"),
            P(entry["message"]),
            Footer(Small(Em(f"Posted: {entry['timestamp']}"))),
        ),

def render_message_list():
    messages = get_messages()
    
    return Div(
        *[render_message(entry) for entry in messages],
        id="message-list",
    )

def render_content():
    form = Form(
        Fieldset(
            Input(
                type="text",
                name="name",
                placeholder="Name",
                required=True,
                maxlength=MAX_NAME_CHAR,
            ),
            Input(
                type="text",
                name="message",
                placeholder="Message",
                required=True,
                maxlength=MAX_MESSAGE_CHAR,
            ),
            Button("Submit", type="submit"),
            role="group",
        ),
        method="post",
        hx_post="/submit-message", #Send a post request to the /submit-message endpoint
        hx_target="#message-list", #only swap the message list
        hx_swap="outerHTML", #replace the entire message list
        hx_on__after_request="this.reset()", #Reset the form after submission
    )
    
    return Div(
        P(Em("Write something nice!")),
        form,
        Div(
            "Made with ❤️ by ", # for emojis click(🪟 + .)
            A("Karan", herf="https://github.com/karanop001018", target="blank"),
        ),
        Hr(),
        render_message_list(),
    )
@rt('/')
def get(): 
    return Titled("My GuestBook 📘", render_content())


@rt('/submit-message', methods=["POST"])
def post(name: str, message: str):
    add_message(name, message)
    return render_message_list()

serve()