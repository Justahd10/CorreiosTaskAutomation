# Access tracking code list from enviroment variable
import os
from dotenv import load_dotenv

from flows.bling import (
    copy_customer_email,
    copy_customer_phone_number
)
from flows.omni import (
    send_email_message,
    send_whatsapp_message,
    past_customer_phone_number
)

load_dotenv()

tracking_codes = os.environ.get("tracking_codes").split(",")

# Start automation, running the flows for each tracking code
# All workflow consists of the flow for invoices management
# and customer service platforms

for code in tracking_codes:
    copy_customer_email(code)
    user_have_phone = send_email_message(code)

    if not user_have_phone:
        copy_customer_phone_number()
        past_customer_phone_number()
    
    send_whatsapp_message(code)