# You will be given a question posed by a user (Human) and the response that was given by a generative AI bot (System). 
This task is to check if factual information in the System's reply is grounded.

The information is presented to you in a JSON format below with the following fields:
query: The question posed by the Human.
result: The System's reply.
context: The context of the System's reply based on which the System should generate the reply.

- Background: The System does a database searche before responding to the Human. 
The search results are shown in the context section of the JSON below containing the text that was retrieved.
The System's reply should be directly taken from the page_content of the SearchResults, paraphrased from them, or 
inferred from them using common knowledge. When the System responds to information that is not mentioned or could not be 
inferred from the SearchResults, we call it a groundedness issue.

- Please review the conversation below between the Human and the System, and identify and list any information in the System's
reply that is not grounded. If the information is directly taken from the text of the SearchResults, paraphrased
from them, or inferred from them using common knowledge, we do not need to list it. If the information is from outside 
sources, we need to list it. You should not look at other content, but only the text of the SearchResults. 
You can follow the below steps:

    1. Look for all the factual information in the System's reply and SearchResults.

    2. Compare the facts in the reply with the facts in the SearchResults. Check if there are any facts that are not in the 
    SearchResults at all, or that contradict or distort the facts in the SearchResults. If there are, write them down. If 
    there are none, leave it blank. Note that some facts may be implied or suggested by the SearchResults, but not explicitly
    stated. In that case, use your best judgment to decide if the fact is grounded or not. For example, if the SearchResults 
    mention that a film was nominated for 12 Oscars, and the System states the same, you can consider that fact as grounded, 
    as it is directly taken from the SearchResults. However, if the SearchResults do not mention the film won any awards at
    all, and  the System states that the film won some awards, you should consider that fact as not grounded regardless of 
    whether it wins or not. If the SearchResults mention the film won several awards, but not the exact number, and the System 
    states the exact number, even if the exact number is correct, you should still consider that fact as ungrounded. 
    Subjective claims are considered as grounded if the information is based on the SearchResults, we do not need any evidence.

    3. Carefully check each piece of information in the reply, especially on the **number, date, person name, phone number, 
    etc.** to **make sure to list all the ungrounded facts before writing output**.

    4. Finally, Rate how well the System responds only using information from the SearchResults and common knowledge on a scale 
    of 0-10 in "rating_out_of_10: X" format. If  the System used information from outside sources, or if  the System made claims that are not 
    backed up by the SearchResults, give it a low score. If  the System **only** used information from the SearchResults and general 
    information, give it a 10.

```json
{conversation_json}
```
# Output 

Reminder: please check each piece of information in the reply carefully, especially on the **number, date, person name, 
phone number, etc.** to **make sure to list all the ungrounded facts before writing output**.

In JSON format repeat the User's question and the System's reply, then complete the ungrounded facts task described above. 
If you give a rating of less than 10, you always have to provide ungrounded facts. 
The resulting format should look like this:

```json
{{
    "question": "<question>",
    "reply": "<reply>",
    "ungrounded_facts": [
        "<fact 1>",
        "<fact 2>",
        "..."
    ],
    "rating_out_of_10": X
}}