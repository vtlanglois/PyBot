
commands = {
    "ask": "Given a prompt, generate a text response.\nFORMAT: !ask <prompt>",
    "draw": "Given a prompt, generate an image\nFORMAT: !draw <prompt>",
    "help": "Provides explanations and formatting for commands\nFORMAT: !help <-c> <command-name>"
}



def generate_help_response(args):
    nargs = len(args);
    if(nargs == 1):
        return "PyBot is a project by vtlanglois. The goal of this project is to create a general-purpose Discord bot using Python"
    elif(nargs == 3 and args[1] == '-c'):
        if(commands.get(args[2]) == None):
            return "Command not found. Please try again"
        response = "!" + args[2] + "\n" +commands.get(args[2])
        return response

    
    return "Error"
