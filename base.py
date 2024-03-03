from openai import OpenAI
import datetime
from time import sleep
from messaging import send_message, send_group
from database import generate_event, editcsv_event_occured





def generate_response_gpt(prompt, important=False, blank=False):


    api_key = "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"

    client = OpenAI(api_key=api_key)

    context = "Your task is to help the user with their event reminders. The user will provide you with the event details and you will return just what to send to the user."


    if important:
        content  = f"Your prompt is: {prompt}, the event is now, please make it sound more important"
    else:
        content  = f"Your prompt is: {prompt}, please add a joke if appropriate and make it more engaging?"

    if blank:
        context = ""
        content = prompt

    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": context + content}],
        stream=True,
    )
    response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            response += chunk.choices[0].delta.content
            
    return response




            




if __name__ == "__main__":

    events = {}

    while True:

        events = generate_event(events)

        print(events.keys())
        print("----")



        for event_ in events:

            event = events[event_]

            if event["event_occured"]:
                del events[event_]
                break


            if event["event_reminder_time"] == 0:

                # Ask GPT for a suitable diff and message
                diff = generate_response_gpt(f"Can you suggest a reminder time inverval before the event to send a reminder? for event {event['event_message']}. Return a single number in minutes no words", blank=True)

                # In case of an error, set the diff to 30 minutes
                try :
                    diff = int(diff)
                except:
                    diff = 30 # Should be a try again, but dont have enough tokens

                event["event_reminder_time"] = event["event_time"] - datetime.timedelta(minutes=diff)


            if not event["event_occured"]:
  
                if (datetime.datetime.now() > event["event_time"]) and (not event["event_occured"]):
                    event["event_message"] = generate_response_gpt(event["event_message"], important=True)
                    send_message("secret.txt", event["event_message"])
                    event["event_occured"] = True

                    editcsv_event_occured(event_, "data.csv")
                    del events[event_]

                    print(f"Finito {event_}")
                    break
                                

                elif datetime.datetime.now() > event["event_reminder_time"] and (not event["event_reminder_occured"]):
                    true_diff = event["event_time"] - datetime.datetime.now()
                    true_diff = f"{true_diff.seconds//3600} hours and {(true_diff.seconds//60)%60} minutes"

                    event_reminder_message = generate_response_gpt(event["event_message"] + f" in {true_diff}, additionally, {event['extra_info']} " )
                    send_message("secret.txt", event_reminder_message)

                    event["event_reminder_occured"] = True

        if events == {}:
            sleep(10000)
        sleep(10)
                    
