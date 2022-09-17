"""Module containing the main script content"""

# Local App imports
from resources.url_decoder import URLDefenseDecoder
from resources.tkinter_gui import DecoderGUIInput, display_result
from resources.utils import create_logger

logger = create_logger()

if __name__ == '__main__':
    # Instantiate Objects
    decoderInput = DecoderGUIInput()
    defenseDecoder = URLDefenseDecoder()

    # Start the tkinter GUI
    result = decoderInput.binding()

    # Attempt to decode the users input/display output
    try:
        output = defenseDecoder.decode(result)
        logger.info("[!] Returned result from decoder class")
        display_result(output)
    except ValueError as e:
        logger.error("%s", e)
        display_result(e)
