import random
import gradio as gr
from gradio.components import *
import pyshorteners
from pyshorteners.exceptions import BadAPIResponseException, BadURLException, ExpandingErrorException, ShorteningErrorException


"""Random error messages"""
def get_random_error_message():
    error_messages = [
        "Oops, it seems you've taken a wrong turn in the digital labyrinth! Please provide a valid link to navigate back on track.",
        "Hmmm, this doesn't look like a magical gateway to another realm. Let's make sure you enter a valid link to unlock the portal!",
        "Ahoy there, matey! We can't sail the digital seas without a proper link. Drop an anchor and provide a valid one!",
        "Beware the virtual roadblocks! Only with a valid link can you pass through this digital checkpoint.",
        "Your journey in cyberspace requires a valid passkey. Don't forget to enter a valid link to unlock the gate!",
        "Looks like we've hit a pixelated dead-end. Please enlighten us with a valid link to uncover the path forward.",
        "Unleash the power of the internet with a valid link! Without it, we're just lost in the digital wilderness.",
        "We've encountered a binary conundrum! To proceed, you must supply the secret code, aka a valid link.",
        "Climb the virtual tower of links and only the valid one will lead you to the enchanted realm of the web.",
        "Heed this virtual decree: Only by providing a valid link shall you gain passage through this digital gateway.",
        "Oh no! It seems you've entered an invalid link. Let's try again with a valid one, shall we?",
        "Uh-oh! Looks like we're missing a proper link. Let's find a valid one and give it another shot!",
        "Oops! That link doesn't seem to be quite right. How about we try again with a valid URL this time?",
        "Oh dear! It appears that the link you provided isn't valid. Let's find a legitimate URL and give it another go!",
        "Uh-oh! It seems we hit a roadblock with that link. Let's make sure we enter a valid URL to proceed.",
        "Oh my! That link seems to be invalid. Let's find a proper URL and give it another chance, shall we?",
        "Yikes! That doesn't look like a valid link. Let's find a legitimate URL to move forward.",
        "Oopsie-daisy! The link you entered isn't valid. Let's find a genuine URL and try again.",
        "Oh dear me! It appears the link you provided isn't quite right. Let's make sure we enter a valid URL this time around.",
        "Oh no, we seem to have encountered an issue with the link you entered. Let's double-check and provide a valid URL to proceed.",
        "Please forgive me if I made a mistake, but it seems the link you entered isn't valid. Let's find a genuine URL and give it another shot!"
    ]
    return random.choice(error_messages)
random_error = get_random_error_message()

""" function for each link shortner service"""
def bitly_shorten(url):
    if not url.startswith("https://") and not url.startswith("http://"):
        url = "https://" + url
    try:
        s = pyshorteners.Shortener(api_key='Enter your own API key')
        shortened_url = s.bitly.short(url)
        return shortened_url
    except (BadAPIResponseException, BadURLException, ExpandingErrorException, ShorteningErrorException) as e:
        return get_random_error_message()

def tinyurl_shorten(url):
    try:
        s = pyshorteners.Shortener()
        shortened_url = s.tinyurl.short(url)
        return shortened_url
    except (BadAPIResponseException, BadURLException, ExpandingErrorException, ShorteningErrorException) as e:
        return get_random_error_message()

def cuttly_shorten(url):
    try:
        s = pyshorteners.Shortener(api_key="Enter your own API key")
        shortened_url = s.cuttly.short(url)
        return shortened_url
    except (BadAPIResponseException, BadURLException, ExpandingErrorException, ShorteningErrorException) as e:
        return get_random_error_message()
    


"""listed services name"""
services = {
    "Bitly": bitly_shorten,
    "TinyURL": tinyurl_shorten,
    "Cuttly": cuttly_shorten
}


"""main function"""
def shorten_url(url, selected_service):
    shortened_url = services[selected_service](url)
    return shortened_url


"""interfacing using gradio"""
url_input = gr.Textbox(label="Enter the URL to shorten:",placeholder="https://github.com/krsatyam7")

service_dropdown = gr.Dropdown(choices=list(services.keys()), label="Select the URL shortening service:", value="Please select any")

output_text = gr.outputs.Textbox(label="Shortened URL:")

interface = gr.Interface(fn=shorten_url, inputs=[url_input, service_dropdown], outputs=[output_text.style(show_copy_button=True, container=True),], title="Link Shortener 🔗", theme=gr.themes.Soft(),allow_flagging="never")
interface.launch()
