from url_decoder import URLDefenseDecoder
from tkinter_gui import DecoderGUIInput, display_result

if __name__ == '__main__':
    # Instantiate Objects
    decoderInput = DecoderGUIInput()
    defenseDecoder = URLDefenseDecoder()

    # Start the tkinter GUI
    result = decoderInput.binding()

    # Attempt to decode the users input/display output
    try:
        output = defenseDecoder.decode(result)
        display_result(output)
    except ValueError as e:
        display_result(e)
