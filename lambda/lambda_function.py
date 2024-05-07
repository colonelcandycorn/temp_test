# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome, let's find a food cart!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Bonjour. "

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class FindACartIntentHandler(AbstractRequestHandler):
    """Handler for Find a Cart Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("FindACartIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        session_attributes = handler_input.attributes_manager.session_attributes
        
        neighborhood = ask_utils.request_util.get_slot(handler_input, "neighborhood")
        country = ask_utils.request_util.get_slot(handler_input, "country")
        food = ask_utils.request_util.get_slot(handler_input, "food")
        drink = ask_utils.request_util.get_slot(handler_input, "drink")
        dessert = ask_utils.request_util.get_slot(handler_input, "dessert")
        cart_name = ask_utils.request_util.get_slot(handler_input, "cartName")
        rating = ask_utils.request_util.get_slot(handler_input, "rating")
        hours = ask_utils.request_util.get_slot(handler_input, "hours")
        
        speak_output = ""
        skip = False
        
        '''buggy'''
        #if (cart_name.value is not None):
            #speak_output += f"The next version of Cart Chart will be able to give you details for {cart_name.value}."
        
        if (neighborhood.value is None):
            if food.value is not None and food.value != "open":
                speak_output += f"The next version of Cart Chart will be able to list nearby carts with {food.value}"
                if not (food.value.endswith("s")):
                    speak_output += "s"
                speak_output += ". "
            if drink.value is not None and drink.value != "open":
                speak_output += f"The next version of Cart Chart will be able to list nearby carts with {drink.value}"
                if not (food.value.endswith("s")):
                    speak_output += "s"
                speak_output += ". "
            if dessert.value is not None and dessert.value != "open":
                speak_output += f"The next version of Cart Chart will be able to list nearby carts with {dessert.value}"
                if not (food.value.endswith("s")):
                    speak_output += "s"
                speak_output += ". "
            if rating.value is not None:
                speak_output += f"The next version of Cart Chart will be able to list nearby carts by rating. "
            if country.value is not None:
                speak_output += f"The next version of Cart Chart will be able to list nearby carts with {country.value} food. "
            if hours.value is not None:
                speak_output += f"The next version of Cart Chart will be able to list nearby carts by their business hours. "
        
        else:
            if (neighborhood.value) == "Woodstock":
                speak_output += "The Heist is"
            elif (neighborhood.value) == "Downtown":
                speak_output += "The Cart Blocks is"
            elif (neighborhood.value) == "Hawthorne":
                speak_output += "Cartopia is"
            elif (neighborhood.value) == "Johnson Creek":
                speak_output += "Cartlandia is"
            elif (neighborhood.value) == "Hillsdale":
                speak_output += "Hillsdale Food Cart Park is"
            else:
                speak_output += "I could not find"
                skip = True
                
            speak_output += f" a food cart pod in the {neighborhood.value} neighborhood. "
            
            if not skip:
                if food.value is not None: 
                    speak_output += f"When I am older, I will know if they have {food.value}"
                    if not (food.value.endswith("s")):
                        speak_output += "s"
                    speak_output += " there. " 
                if country.value is not None: 
                    speak_output += f"When I am older, I will know if they have {country.value} food there. "
                if dessert.value is not None: 
                    speak_output += f"When I am older, I will know if they have {dessert.value}"
                    if not (dessert.value.endswith("s")):
                        speak_output += "s"
                    speak_output += " there. "
                if drink.value is not None: 
                    speak_output += f"When I am older, I will know if they have {drink.value}"
                    if not (drink.value.endswith("s")):
                        speak_output += "s"
                    speak_output += " there. "

        if speak_output == "":
            speak_output = "Sorry, no carts found. "

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("Would you like to continue? ")
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can find a food cart by saying, \"Find a Cart.\" For example: \"Find a taco cart.\""

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(FindACartIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()