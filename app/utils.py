def format_script(script):

    formatted = script.replace("Hook:", "\n🎬 Hook:\n")
    formatted = formatted.replace("Main Points:", "\n📌 Main Points:\n")
    formatted = formatted.replace("Ending CTA:", "\n🚀 Call To Action:\n")

    return formatted